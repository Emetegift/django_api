from rest_framework import serializers
from api.serializers import UserPublicSerializer ## This is regarded as the general serializer linked to the one above
from .models import Product
from rest_framework.reverse import reverse
# from .validators import validate_title
from . import validators


## Related fields and foreign key serializer. this will basicall list all the users products links and title
class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='product-detail',
        lookup_field = 'pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True) #This will call all the values in the general serializers
    # related_product = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url =  serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='product-detail',
        lookup_field = 'pk'
    )
    # email = serializers.EmailField(write_only=True) # Please note that this can be anything besides email
    # title = serializers.CharField(validators=[validate_title])
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    # email = serializers.CharField(source='user.email', read_only=True)
    body = serializers.CharField(source='content') ## This will enable the content field that has been changed to body to reflect
    class Meta:
        model = Product
        fields =[
            'owner',
            'url',
            'edit_url',
            # 'email',
            'pk',
            'title',
            # 'name',
            'body',
            'price',
            'sale_price',
            # 'my_discount',
            # 'related_product',
            # # 'my_user_data',
            'public',
            'endpoint',
        ]

    def  get_my_user_data(self, obj):
        return {
            "username": obj.user.username ## This will basically get the actual username
        }
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
    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
