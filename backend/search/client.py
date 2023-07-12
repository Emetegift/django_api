# Algolia search client for Django
from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client

def get_index(index_name='cfe_Product'):
    client = get_client()
    index = client.init_index(index_name)
    return index

# function that will perform search
def perform_search(query, **kwargs):
    index = get_index()
    tags = ""
    params = {}
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or [] 
        if len(tags) !=0:
            params['tagFilters']=tags
    index_filters = [f"{k}:{v}" for k,v in kwargs.items() if v]
    if len(index_filters) !=0:
        params['facetFilter'] = index_filters ## This is another way to filter items
    results = index.search(query), params
    return results
##GO and implement this on the search views


