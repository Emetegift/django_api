from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

## To create generic API views
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    ##To authenticate a user
    authentication_classes = [authentication.SessionAuthentication]
    ## To add permission to API
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        # serializer.save(username.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        # or None
        if content is None:
            content=title
        serializer.save(content=content)
        # send a Django signal


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content=instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def perform_destroy(self, instance):
       #instance
       super().perform_destroy(instance)



# class ProductListAPIView(generics.ListAPIView):
#     """
#     Not using this
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer






# # Mxins and a generic class view

class ProductMixin(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='pk'

    #To define the get method using the generic class view
    def get(self, request,*args, **kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs) ## This will return the the retrieve function if pk is present
        return self.list(request,*args, **kwargs)
    
    ##To define the post method using the generic class view
    def post(self, request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(username.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        # or None
        if content is None:
            content="This is me"
        serializer.save(content=content)
        # send a Django signal





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
