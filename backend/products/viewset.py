from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

class ProuductViewSet(viewsets.ModelViewSet):
    """
    get -->list-->queryset
    get --> retrieve -->product instance Detail view
    post -->create a new item or instance
    put --> update an instance
    patch --> partial update
    delete --> destroy an instance or item
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk" #default
