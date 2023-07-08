import requests

# This is a proces used to access external APIs
# enpoint ="https://httpbin.org/status/200"
enpoint ="https://httpbin.org/anything"

get_response = requests.get(enpoint, json={"query": "Hello world"}) # This http request will return the data in a json format thats similar to a python dictionary
print(get_response.text)

#HTTP Request---> returns HTML, while
#REST API HTTP requests ---> JSON

print(get_response.json())
print(get_response.status_code)