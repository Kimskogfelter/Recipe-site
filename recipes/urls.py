from django.urls import path
from .views import (AddRecipeView, RecipesView, RecipeDetailView,
                    DeleteRecipeView, EditRecipeView,
                    EditCommentView, DeleteCommentView)


urlpatterns = [
    path("add/", AddRecipeView.as_view(), name="add_recipe"),
    path("", RecipesView.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetailView, name="recipe_detail"),
    path("delete/<slug:pk>/", DeleteRecipeView.as_view(),
         name="delete_recipe"),
    path(
        "edit/<slug:pk>/",
        EditRecipeView.as_view(),
        name="edit_recipe",
    ),
    path(
        "comment/edit/<slug:pk>/",
        EditCommentView.as_view(),
        name="edit_comment",
    ),
    path(
        "comment/delete/<slug:pk>/",
        DeleteCommentView.as_view(),
        name="delete_comment",
    ),
]
