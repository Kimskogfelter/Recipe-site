from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import RecipeModel, CommentRecipeModel


class RecipeForm(forms.ModelForm):
    """Form to create a recipe"""
    class Meta:
        model = RecipeModel
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
    class Meta:
        model = CommentRecipeModel
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CommentRecipeForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = False
        # makes the width of the form smaller
        self.fields['text'].widget.attrs.update({'style': 'width: 95%;'})
