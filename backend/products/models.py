from django.conf import settings
from django.db import models


# Create your models here.

User = settings.AUTH_USER_MODEL #Auth user

class Product(models.Model):
    #pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) # This basically links the user table to the product table
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

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