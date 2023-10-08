from django.contrib import admin

# Register your models here.
from django.contrib import admin

from main.models import Product, Category

# Register your models here.


#admin.site.register(Student)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')