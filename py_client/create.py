import requests


enpoint ="http://localhost:8000/api/products/"
data ={
    'title': 'This field has been created',
    'price': 32.99
}
get_response = requests.post(enpoint, json=data) # This is a get request

print(get_response.json())
# print(get_response.status_code)