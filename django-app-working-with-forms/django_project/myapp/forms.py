import datetime
from django import forms

from .models import Reporter, Article

class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


ArticleFormSet = forms.formset_factory(ArticleForm)


class ReporterModelForm(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = ['name',]


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
