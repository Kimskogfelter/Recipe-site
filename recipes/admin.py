from django.contrib import admin
from .models import RecipeModel

# Register your models here.


@admin.register(RecipeModel)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "meal_type",
        "calories",
        "instructions",
        "ingredients",
        "image",
    )
    list_filter = ("meal_type",)
