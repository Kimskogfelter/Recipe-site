from django.urls import path
from .views import ProfilesView


urlpatterns = [
    path("user/<slug:pk>/", ProfilesView.as_view(), name="profile"),

]
