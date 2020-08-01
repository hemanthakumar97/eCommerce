from django.contrib import admin
from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', 
            views.activate, name='activate'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]