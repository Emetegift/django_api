from django.urls import path
from . import views


urlpatterns=[
    path('', views.ProductListCreateAPIView.as_view(), name="product-list"),
    # path('', views. product_alt_view), # This url is for the single function endpoints for list and create
    # path('<int:pk>/', views. product_alt_view), #This url is for the single function endpoints for retrieve
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name ="product-edit"),
    # path('', views.ProductMixin.as_view()),# Url for create and get list method using the generic class view
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="product-detail"),
    #  path('<int:pk>/', views.ProductMixin.as_view()), # Url for detail  get (by_id) method using the generic class view
]



