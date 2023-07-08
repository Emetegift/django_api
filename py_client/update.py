import requests


endpoint ="http://localhost:8000/api/products/1/update/"
data ={
    'title': 'This field has been updated',
    'price':90.900
}
get_response = requests.put(endpoint, json=data) # This is a get request

print(get_response.json())
# print(get_response.status_code)