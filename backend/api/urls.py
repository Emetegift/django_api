from django.urls import path
from . import views



urlpatterns=[
    path('', views.api_home)  ## This is the url for our localhost:8000
]