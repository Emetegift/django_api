from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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


# class ProductListAPIView(generics.ListAPIView):
#     """
#     Not using this
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


##To write create, retireve and list endpoints using a single function

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method=="GET":
        if pk is not None:
            #detail view, that is to get an item by id
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        #List view, that is to get all items
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)


    if method=="POST":
         #create an item. i.e, a post method
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content =  serializer.validated_data.get('content')
            # or None
            if content is None:
                content=title
                serializer.save(content=content)
                return Response(serializer.data)
            return Response({"invalid": "Not a good data"}, status=400)
