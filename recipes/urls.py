from django.urls import path
from .views import AddRecipe, Recipes, RecipeDetail, DeleteRecipe, EditRecipe, EditComment, DeleteComment


urlpatterns = [
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetail, name="recipe_detail"),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path(
        "edit/<slug:pk>/",
        EditRecipe.as_view(),
        name="edit_recipe",
    ),
    path(
        "edit/<slug:pk>/",
        EditComment.as_view(),
        name="edit_comment",
    ),
    path(
        "edit/<slug:pk>/",
        DeleteComment.as_view(),
        name="delete_comment",
    ),
]