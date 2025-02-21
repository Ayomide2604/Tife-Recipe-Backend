from django.db import models
from django.conf import settings
import os
from cloudinary.models import CloudinaryField


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    if os.getenv('CLOUDINARY_CLOUD_NAME'):
        image = CloudinaryField('image', null=True, blank=True)
    else:
        image = models.ImageField(
            upload_to="categories/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    if os.getenv('CLOUDINARY_CLOUD_NAME'):
        image = CloudinaryField('image', null=True, blank=True)
    else:
        image = models.ImageField(
            upload_to="recipes/", null=True, blank=True)
    description = models.TextField()
    categories = models.ManyToManyField(
        Category, related_name="recipes", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
