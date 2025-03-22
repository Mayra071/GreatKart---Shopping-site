from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug_field':('Category_name',)}
    list_display = ('Category_name','slug_field')
admin.site.register(Category, CategoryAdmin)