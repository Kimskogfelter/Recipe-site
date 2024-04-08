from django import forms
from .models import ProfileModel


class ProfileForm(forms.ModelForm):
    """Form to create a profile"""

    class Meta:
        model = ProfileModel
        fields = ["image", "bio"]

        labels = {"image": "Avatar", "bio": "Bio"}
