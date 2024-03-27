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
from .models import Recipe, SavedRecipe, CommentRecipe
from .forms import RecipeForm, CommentRecipeForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse


def save_recipe(request):
    """ saves the recipe with the heart icon """
    if request.method == 'POST' and request.user.is_authenticated:
        recipe_id = request.POST.get('recipe_id')
        saved_recipe, created = SavedRecipe.objects.get_or_create(
            user=request.user,
            recipe_id=recipe_id
        )
        if not created:
            saved_recipe.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


class Recipes(ListView):
    """View all recipes"""
    template_name = "recipes/recipes.html"
    model = Recipe
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


def RecipeDetail(request, pk):
    """View a single recipe"""
    template_name = "recipes/recipe_detail.html"
    recipe = get_object_or_404(Recipe, pk=pk)
    comment = None
    comments = CommentRecipe.objects.filter(recipe=recipe)
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


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add recipe view"""
    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit recipe"""
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"
    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete recipe"""
    model = Recipe
    success_url = "/recipes/"
    def test_func(self):
        return self.request.user == self.get_object().user

