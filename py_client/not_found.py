import requests


endpoint ="http://localhost:8000/api/products/13567881765451/"

get_response = requests.get(endpoint) # This is a get request

print(get_response.json())
# print(get_response.status_code)