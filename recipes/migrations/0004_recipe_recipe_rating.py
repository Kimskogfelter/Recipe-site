# Generated by Django 4.2.10 on 2024-03-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0003_alter_recipe_food_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="recipe_rating",
            field=models.IntegerField(default=0),
        ),
    ]