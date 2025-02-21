from rest_framework import viewsets, parsers
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    # Custom unpaginated endpoint

    # 👈 Disable pagination
    @action(detail=False, methods=['get'], pagination_class=None)
    def all(self, request):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    parser_classes = [parsers.MultiPartParser,
                      parsers.FormParser]
