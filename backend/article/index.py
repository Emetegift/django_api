from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from.models import Article

@register(Article)
class ArticleIndex(AlgoliaIndex):
    # shoul_index ='is_public'
    fields = [
        'title',
        'body', 
        'user',
        'make_public',
        'publish_date',
        'endpoint',
    ]
    
    settings ={
         "searchableAttributes" : ['title', 'body'],
        "attributesForFaceting" : ['user','public'],
        "ranking":['asc(publish_date)'],
    }
    
    
    tags = 'get_tags_list'