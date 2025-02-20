from django.contrib import admin
from .models import Category, Recipe
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title",  "created_at", "updated_at")
    search_fields = ("title", "categories__title")
    list_per_page = 10
