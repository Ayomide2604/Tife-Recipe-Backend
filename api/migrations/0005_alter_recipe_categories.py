# Generated by Django 5.1.6 on 2025-02-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_category_recipe_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='recipes', to='api.category'),
        ),
    ]
