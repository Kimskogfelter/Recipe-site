from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Profile(TemplateView):
    template_name = 'profile_page.profile.html'