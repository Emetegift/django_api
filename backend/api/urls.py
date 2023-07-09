from django.urls import path
# from django.urls import path, include # All the urls can also be written herer and linked the to home url with the include function

from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns=[
    path('auth/', obtain_auth_token),
    path('', views.api_home)  ## This is the url for our localhost:8000
    #  path('/products/', include('products.urls')),
]