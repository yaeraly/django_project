from django.forms import ModelForm
from .models import Programmer, Language


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['programmer', 'name']
