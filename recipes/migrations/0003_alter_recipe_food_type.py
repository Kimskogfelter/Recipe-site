# Generated by Django 4.2.10 on 2024-03-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_rename_image_alt_recipe_image_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="food_type",
            field=models.CharField(
                choices=[
                    ("bread", "Bread"),
                    ("fish", "Fish"),
                    ("meat", "Meat"),
                    ("pork", "Pork"),
                    ("chicken", "Chicken"),
                    ("Chocolate", "Chocolate"),
                    ("cake", "Cake"),
                    ("Sallad", "Sallad"),
                    ("pasta", "Pasta"),
                    ("rice", "Rice"),
                    ("fruit", "Fruit"),
                ],
                default="sandwich",
                max_length=45,
            ),
        ),
    ]
