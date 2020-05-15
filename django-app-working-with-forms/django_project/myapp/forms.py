import datetime
from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


ArticleFormSet = forms.formset_factory(ArticleForm)
