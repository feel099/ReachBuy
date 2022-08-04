from django.contrib import admin

from .models import Product, Review, Category, User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'manufacturer', 'city']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'published', 'rating', 'product']


admin.site.register(User)

