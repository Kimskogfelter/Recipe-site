from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.shortcuts import render
from django.views.generic import TemplateView,  FormView
from django.urls import reverse_lazy
from .forms import ContactUsForm


# Create your views here.

#view for contact form
class ContactUsView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('successform')  

    def form_valid(self, form):
        firstname = form.cleaned_data.get("firstname")
        lastname = form.cleaned_data.get("lastname")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {email}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super().form_valid(form)


# view when the form message is successfully sent
class SuccessFormView(TemplateView):
    template_name = 'contact/successform.html'