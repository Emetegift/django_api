## General serializer that is link to the product serializer
from rest_framework import serializers

#For  a user to get his or her  other products
class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='product-detail',
        lookup_field = 'pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True) ## This will display the actual user's name
    id = serializers.IntegerField(read_only=True)
    # email =serializers.EmailField(read_only=True)

    # def get_other_products(self, obj):
    #     user = obj
    #     my_products_qs = user.product_set.all()[:5]
    #     return UserProductInlineSerializer(my_products_qs, many=True, context=self.context).data
