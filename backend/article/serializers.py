from rest_framework import serializers
from api.serializers import UserPublicSerializer ## This is regarded as the general serializer linked to the one above
from .models import Article
from rest_framework.reverse import reverse
from products import validators


## Related fields and foreign key serializer. this will basicall list all the users products links and title
class ArticleInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='article-detail',
        lookup_field = 'pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class ArticleSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True) #This will call all the values in the general serializers
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='article-detail',
        lookup_field = 'pk'
    )
  
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    class Meta:
        model = Article
        fields =[
            'author',
            'url',
            'pk',
            'title',
            'body',
            'tags',
            'make_public',
            'publish_date',
            'endpoint',
        ]

    def  get_my_user_data(self, obj):
        return {
            "username": obj.user.username ## This will basically get the actual username
        }
    