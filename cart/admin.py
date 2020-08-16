from django.contrib import admin
from .models import Cart

# class CartAdmin(admin.ModelAdmin):
#     list_display = ('user.first_name',' user.email')

admin.site.register(Cart)
