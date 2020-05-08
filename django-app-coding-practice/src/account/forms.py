from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models import Account


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'password1', 'password2']
