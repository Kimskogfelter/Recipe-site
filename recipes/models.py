from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField



# Meal Type Choice Fields
MEAL_TYPE = (
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("snack", "Snack"),
)

# Food Type Choice Fields
FOOD_TYPE = (
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
)

# Create your models here.


class Recipe(models.Model):
    """
    A model to create and change/delete recipes
    """

    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.CharField(max_length=600, null=False, blank=False)
    ingredients = RichTextField(max_length=9000, null=False, blank=False)
    instructions = RichTextField(max_length=9000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_description = models.CharField(max_length=150, null=False, blank=False)
    meal_type = models.CharField(max_length=45, choices=MEAL_TYPE, default="lunch")
    food_type = models.CharField(max_length=45, choices=FOOD_TYPE, default="sandwich")
    calories = models.IntegerField()
    posted_date = models.DateTimeField(auto_now=True) # posted date for the recipe
    recipe_rating = models.IntegerField(default=0)  # recipe star rating

    class Meta:
        ordering = ["-posted_date"]

    def _str__(self):
        return str(self.title)

# model for the comment section
class Comment(models.Model):

    """
    A model for the comment section in the recipe detail view
    """

    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.recipe.id)])


# model for saved recipes with heart icon
class SavedRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)