from django.shortcuts import render
from rest_framework import generics

from products.models import Product
from products.serializers import ProductInlineSerializer

class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductInlineSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs) ## This is calling the queryset default value which is thw queryset above
        q = self.request.GET.get('q')
        results = Product.objects.none()
        if q is not None:
            user=None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results