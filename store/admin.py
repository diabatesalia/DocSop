from django.contrib import admin
from store.models import Product, Category

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_ajou')

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description', 'date_ajou')

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
