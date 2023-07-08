from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(username.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        # or None
        if content is None:
            content=title
        serializer.save()
        # send a Django signal


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """
    Not using this
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
