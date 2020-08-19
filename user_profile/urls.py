from django.contrib import admin
from django.urls import path, include
from .views import *
app_name= 'user_profile'

urlpatterns = [
    path("profile/", my_profile, name='profile'),
]