## for custom validation

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product


# def validate_title(value):
#         qs = Product.objects.filter(title__iexact=value) # This will querry the exact value in the database
#         if qs.exists():
#             raise serializers.ValidationError(F"{value} is already a product name.")
#         return value 


## This validation function below can be used when you want a particular type of input from users, e.g using no_hello
def validate_title_no_hello(value):
      if "hello"in value.lower():
            raise serializers.ValidationError(f" {value}: Hello is not allowed")
      return value


unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')


