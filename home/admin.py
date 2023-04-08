from django.contrib import admin
from .models import Task, Product
# Register your models here.
admin.site.register(Task)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)