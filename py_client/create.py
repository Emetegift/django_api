import requests



headers = {'Authorization': 'Bearer 72abf3b0ee147b017d54349aabf5c4f3d4e065bc'}
endpoint ="http://localhost:8000/api/products/"
data ={
    'title': 'This field has been created',
    'price': 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers) # This is a get request

print(get_response.json())
# print(get_response.status_code)