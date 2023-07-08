from django.urls import path
from . import views


urlpatterns=[
    path('', views.ProductListCreateAPIView.as_view()),
    # path('', views. product_alt_view), # This url is for the single function endpoints for list and create
    # path('<int:pk>/', views. product_alt_view), #This url is for the single function endpoints for retrieve
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
]

