import random
from django.conf import settings
from django.db import models
from django.db.models import Q #This will help query the lookup with error

# Create your models here.

User = settings.AUTH_USER_MODEL #Auth user

## To tag things to the product class
TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'movies', 'cameras']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2=self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class Product(models.Model):
    #pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) # This basically links the user table to the product table
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return f"/api/products/{self.pk}/"

    @property
    def endpoint(self):
        return f"/products/{self.pk}/"
        
    @property
    def url(self):
        return self.get_absolute_url()

    @property
    def body(self):
        return self.content # This will basically change the content to body in the serializer

    def is_public(self) -> bool:
        return self.public ## This will return true or false
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]

    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8) 
    """ 
    This is used when a seller wants to give percentage discount of te main price 
    by calculating the percentage that is to be given as discount
    """
    def get_discount(self):
        return "122"