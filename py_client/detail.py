import requests


enpoint ="http://localhost:8000/api/products/1/"

get_response = requests.get(enpoint) # This is a get request

print(get_response.json())
# print(get_response.status_code)