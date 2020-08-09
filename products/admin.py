from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_nocost')
    list_filter = ('category', 'is_published', 'is_nocost')
    list_editable = ('is_published', 'is_nocost')

admin.site.register(Category)
admin.site.register(Laptop)
admin.site.register(Mobile)
admin.site.register(Sensor)
admin.site.register(ElectronicComponent)
admin.site.register(Product, ProductAdmin)
admin.site.register(Seller)
