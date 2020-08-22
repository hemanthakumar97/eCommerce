from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
app_name = 'accounts'

urlpatterns = [
#     path('signup/', views.signup, name='signup'),
    path('signup/', views.signup1, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', 
            views.activate, name='activate'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('new_password/', views.new_password, name='new_password'),
    path('change_password/', views.change_password, name='change_password'),
    path('deactivate/', views.deactivate, name='deactivate'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)