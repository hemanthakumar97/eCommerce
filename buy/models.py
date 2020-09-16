from django.db import models
from products.models import *
from user_profile.models import *
from django.contrib.auth.models import User, AbstractUser


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=1, null=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    payment_status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.user.username