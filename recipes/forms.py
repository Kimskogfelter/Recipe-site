from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe, CommentRecipe


class RecipeForm(forms.ModelForm):
    """Form to create a recipe"""

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_description",
            "meal_type",
            "food_type",
            "calories",
        ]

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "image_description": "Describe Image",
            "meal_type": "Meal Type",
            "food_type": "Food Type",
            "calories": "Calories",
        }


class CommentRecipeForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here!',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = CommentRecipe
        fields =['content']