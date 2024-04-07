from django import forms


class ContactUsForm (forms.Form):
    firstname = forms.CharField(label='First Name',
        widget=forms.TextInput(attrs={"placeholder": "First name"}))
    lastname = forms.CharField(label='Last Name',
        widget=forms.TextInput(attrs={"placeholder": "Last name"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )
