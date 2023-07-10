from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url =  serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='product-detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Product
        fields =[
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_edit_url(self, obj):
         # return f"/api/v2/products/{obj.pk}"  # OR
        request = self.context.get('request') # This is a get request because it is how serializers work 
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request) # This will handle the update endpoint
        # return reverse("product-detail", kwargs={"pk":obj.pk}, request=request)
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
