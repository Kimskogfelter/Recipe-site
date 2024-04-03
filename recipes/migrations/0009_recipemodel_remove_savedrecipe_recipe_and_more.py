# Generated by Django 4.2.10 on 2024-04-03 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0008_rename_body_commentrecipe_text_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecipeModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("description", models.CharField(max_length=600)),
                ("ingredients", djrichtextfield.models.RichTextField(max_length=9000)),
                ("instructions", djrichtextfield.models.RichTextField(max_length=9000)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[400, None],
                        upload_to="recipes/",
                    ),
                ),
                ("image_description", models.CharField(max_length=150)),
                (
                    "meal_type",
                    models.CharField(
                        choices=[
                            ("breakfast", "Breakfast"),
                            ("lunch", "Lunch"),
                            ("dinner", "Dinner"),
                            ("snack", "Snack"),
                        ],
                        default="lunch",
                        max_length=45,
                    ),
                ),
                (
                    "food_type",
                    models.CharField(
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
                ("calories", models.IntegerField()),
                ("posted_date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipe_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-posted_date"],
            },
        ),
        migrations.RemoveField(
            model_name="savedrecipe",
            name="recipe",
        ),
        migrations.RemoveField(
            model_name="savedrecipe",
            name="user",
        ),
        migrations.RenameModel(
            old_name="CommentRecipe",
            new_name="CommentRecipeModel",
        ),
        migrations.DeleteModel(
            name="Recipe",
        ),
        migrations.DeleteModel(
            name="SavedRecipe",
        ),
        migrations.AlterField(
            model_name="commentrecipemodel",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="recipes.recipemodel"
            ),
        ),
    ]
