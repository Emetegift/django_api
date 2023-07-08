# Create the API endpoint view
import json
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


# define the function views
@api_view(["GET"])
def api_home(request, *args, **kwargs ): 

    """
    This is a Django Rest API view
    """
    instance = Product.objects.all().order_by("?").first()
    data ={}
    # # The code below takes a model instance i.e, model_data in this case, turn it into a python dictionary and returns a JSON to the client
    # data['title'] = model_data.title
    # data['content'] = model_data.content
    # data['price'] =model_data.price

    ## The code commented above can simply be written as follow using the model_to_dict function

    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)

