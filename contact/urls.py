from django.urls import path
from .views import ContactUsView, SuccessFormView


urlpatterns = [
    path('', ContactUsView.as_view(), name='contact'),
    path('successform/', SuccessFormView.as_view(), name='successform'),
]