from rest_framework_nested import routers
from django.urls import path, include
from .views import CategoryViewSet, RecipeViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'recipes', RecipeViewSet)

# Create a nested router and register the nested viewset with it.
categories_router = routers.NestedDefaultRouter(
    router, r'categories', lookup='category')
categories_router.register(r'recipes', RecipeViewSet,
                           basename='category-recipes')



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('', include(categories_router.urls)),
]
