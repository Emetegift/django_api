const contentContainer = document.getElementById('content-container')

const loginForm = document.getElementById('login-form')

const searchForm = document.getElementById('search-form')
const baseEndpoint = "http://localhost:8000/api"
if (loginForm){
    // handle this login form,i.e it should submit this form if its a login form
    loginForm.addEventListener('submit', handleLogin)
}

if (searchForm){
    // handle this login form,i.e it should submit this form if its a login form
    searchForm.addEventListener('submit', handleSearch)
}

function handleLogin(event) {
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    console.log(loginObjectData)
    const options = {
        method : "POST",
        headers :{
            "Content-Type": "application/json"
        },
        body:bodyStr

    }
    fetch(loginEndpoint, options) // This fetch is running the request.Posts endpoint called the promise
    .then(response=>{
        return response.json()
    })
    .then(authData=>{
        handleAuthData(authData, getProductList)
    })
    .catch(err=>{
        console.log('err', err)
    })
}

function handleSearch(event) {
    event.preventDefault()
    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    const headers = {
        "Content-Type": "application/json",
    }
    const authToken = localStorage.getItem('access')
    if (authToken){
        headers['Authorization'] =`Bearer ${authToken}`
    }
    const options = {
        method : "GET",
        headers :headers

    }
    fetch(endpoint, options) // This fetch is running the request.Posts endpoint called the promise
    .then(response=>{
        return response.json()
    })
    .then(data=>{
        // writeToContainer(data)
        const validData = isTokenNotValid(data)
        if (validData && contentContainer){
            contentContainer.innerHTML = ""
            if (data && data.hits) {
                let htmlStr = ""
                for (let result of data.hits) {
                    htmlStr += "<li>"+ result.title + "</li>"
                }
                contentContainer.innerHTML = htmlStr
                if (data.hits.length===0) {
                    contentContainer.innerHTML = "<p>No results found</p>"
                }
            } else {
                contentContainer.innerHTML = "<p> No results found </p>"
            }
        }
        
    })
    .catch(err=>{
        console.log('err', err)
    })
}



function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access) //This will handle the access token request
    localStorage.setItem('refresh',authData.refresh)  //This will handle the refresh token request
    if (callback) {
        callback()  // This will call the getProductList function
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        (contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null,4)+ "</pre>")
    }
}

function getFetchOptions(method, body) { //This method is placed here because the required wll not always be a get method
    return {
        method: method===null? "GET":method, // this imply that a get method will be received if no method i sspecified
        headers:{
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}` // This will help get all the items in the productlist
        }, 
        body: body ? body:null
    }
}
function isTokenNotValid(jsonData) {
    if (jsonData.code && jsonData.code ==="token_not_valid"){
            //run a refresh token query or fetch
        alert("Please login again")
        return false
    }
    return true
}
function validateJWTToken(){
    //fetch
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method:"POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            {
                token:localStorage.getItem('access')
            })
    }
    fetch(endpoint, options)
    .then(response=>response.json())
    .then(x=>{
            //refresh token
            isTokenNotValid(x)
    })
}

function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options =getFetchOptions()
    fetch (endpoint, options)
    .then(response=>{
        return response.json()
        })

    .then(data=>{
        const validData = isTokenNotValid(data)
        if (validData){
            writeToContainer(data)
        }
        
    })  
}   
validateJWTToken()
// handleSearch()