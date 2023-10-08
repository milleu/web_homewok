from django.contrib import admin

# Register your models here.
from django.contrib import admin

from main.models import Product, Category

# Register your models here.


#admin.site.register(Student)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description')