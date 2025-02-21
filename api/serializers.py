from rest_framework import serializers
from .models import Category, Recipe
from backend.settings import MEDIA_URL


class SimpleRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "title", "image", "description",
                  "categories", "created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    recipes = SimpleRecipeSerializer(many=True, required=False)

    def get_image(self, obj):
        if obj.image:
            return f"{MEDIA_URL}{obj.image}"

        return None

    class Meta:
        model = Category
        fields = ["id", "title", "image", "recipes", "date_created"]


class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, required=False)
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            return f"{MEDIA_URL}{obj.image}"

        return None

    class Meta:
        model = Recipe
        fields = ["id", "title", "image", "description",
                  "categories", "created_at", "updated_at"]

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        recipe = Recipe.objects.create(**validated_data)
        for category_data in categories_data:
            Category.objects.create(recipe=recipe, **category_data)
        return recipe
