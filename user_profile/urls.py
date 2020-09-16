from django.contrib import admin
from django.urls import path, include
from .views import *
app_name= 'user_profile'

urlpatterns = [
    path("profile/", my_profile, name='profile'),
    path("del_card/<int:id>/", del_card, name='del_card'),
    path("del_addr/<int:id>/", del_addr, name='del_addr'),
    path("edit_addr/<int:id>/", edit_addr, name='edit_addr'),
    # path("del_addr/<int:id>/", del_addr, name='del_addr'),
]