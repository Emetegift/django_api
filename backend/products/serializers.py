from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
# from .validators import validate_title
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url =  serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='product-detail',
        lookup_field = 'pk'
    )
    # email = serializers.EmailField(write_only=True) # Please note that this can be anything besides email
    # title = serializers.CharField(validators=[validate_title])
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    # email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Product
        fields =[
            # 'user',
            'url',
            'edit_url',
            # 'email',
            'pk',
            'title',
            # 'name',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # # To validate a particular value in a database, e.g;
    # def validate_title(self, value):
    #     request = self.context.get(request)
    #     user = request.user
    #     qs = Product.objects.filter(title__iexact=value) # This will querry the exact value in the database
    #     if qs.exists():
    #         raise serializers.ValidationError(F"{value} is already a product name.")
    #     return value 
#  # This is basically how a new field can be added and updated using serializers
#     def create(self, validated_data):
#     #   return  Product.objects.create(**validated_data) OR
#         # email = validated_data.pop('email')
#         obj = super().create(validated_data)
#         # print(email, obj)
#         return obj

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
