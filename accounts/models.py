from django.db import models
from django.contrib.auth.models import User, AbstractUser

class EmailOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    trans_id = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    otp = models.IntegerField()
    def __str__(self):
        return str(self.otp)