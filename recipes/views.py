from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
""" checks if the user in logged in """
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .models import RecipeModel, CommentRecipeModel
from .forms import RecipeForm, CommentRecipeForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse


class RecipesView(ListView):
    """View all recipes"""
    template_name = "recipes/recipes.html"
    model = RecipeModel
    context_object_name = "recipes"
    """ query for the search bar in the header """
    def get_queryset(self, **kwargs):
        search_query = self.request.GET.get("searchquery")
        if search_query:
           recipes = self.model.objects.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(instructions__icontains=search_query) |
                Q(food_type__icontains=search_query) |
                Q(meal_type__icontains=search_query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes


def RecipeDetailView(request, pk):
    """View a single recipe"""
    template_name = "recipes/recipe_detail.html"
    recipe = get_object_or_404(RecipeModel, pk=pk)
    comment = None
    comments = CommentRecipeModel.objects.filter(recipe=recipe)
    if request.method == "POST":
        comment_form = CommentRecipeForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user
            comment.save()
            comment_form = CommentRecipeForm()
    else:
        # Handle invalid form submission here, if needed
        comment_form = CommentRecipeForm()
    return render(
        request,
        template_name,
        {
            "recipe": recipe,
            "comments": comments,
            "comment_form": comment_form,
            "template_name": template_name
        }
    )


class AddRecipeView(LoginRequiredMixin, CreateView):
    """Add recipe view"""
    template_name = "recipes/add_recipe.html"
    model = RecipeModel
    form_class = RecipeForm
    success_url = "/recipes/"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipeView, self).form_valid(form)


class EditRecipeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit recipe"""
    template_name = "recipes/edit_recipe.html"
    model = RecipeModel
    form_class = RecipeForm
    success_url = "/recipes/"
    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRecipeView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete recipe"""
    model = RecipeModel
    success_url = "/recipes/"
    template_name = 'recipes/recipe_confirm_delete.html'
    def test_func(self):
        return self.request.user == self.get_object().user


class EditCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit comment made on a recipe"""
    template_name = "recipes/edit_comment.html"
    model = CommentRecipeModel
    form_class = CommentRecipeForm
    success_url = "/recipes/"
    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete comment made on a recipe"""
    template_name = "recipes/comment_confirm_delete.html"
    model = CommentRecipeModel
    success_url = "/recipes/"
    def test_func(self):
        return self.request.user == self.get_object().user
