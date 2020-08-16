from django.conf import settings
from django.db import models

from products.models import Product

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,  null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
