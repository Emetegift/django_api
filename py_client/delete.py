import requests

product_id =input("What is the product id you want to use? \n")


try:
    product_id = int(product_id)
except:
    product-id==None
    print(f'{product_id} is not a valid id')
if product_id:
    endpoint ="http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint) # This is a delete request
    print(get_response.status_code, get_response.status_code==204)