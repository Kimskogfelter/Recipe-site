from django.urls import path
from .views import Contact, SuccessForm


urlpatterns = [
    path('', Contact.as_view(), name='contact')
    path("successform/", SuccessForm.as_view(), name="successform"),
]