from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    mobile = models.IntegerField(blank=True)
    locality = models.CharField(max_length=50)
    area = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    pin = models.IntegerField(blank=True)
    landmark = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    card_no = models.IntegerField()
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    cvv = models.IntegerField()
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

class ProfileInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
