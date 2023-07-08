# Create the API endpoint view
from django.http import JsonResponse

# define the function views

def api_home(self, *args, **kwargs ): 
    return JsonResponse({"message":"Hi"})
