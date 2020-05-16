import datetime
from django.shortcuts import render, redirect

from .forms import ArticleFormSet, ReporterModelForm, ArticleModelForm

def home_view(request):

    return render(request, 'myapp/home.html')


data = {
    'form-TOTAL_FORMS': '1',
    'form-INITIAL_FORMS': '1',
    'form-MAX_NUM_FORMS': '',
    'form-0-title': 'Django is cool cool',
    'form-0-pub_date': datetime.date.today()
}

def name_view(request):
    if request.method == 'POST':
        formset = ArticleFormSet(data)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data.get('title'))
                print(form.cleaned_data.get('pub_date'))
            return redirect('home')
        else:
            print(formset.errors)
    else:
        formset = ArticleFormSet(data)

    return render(request, 'myapp/name.html', {'formset': formset})


def new_view(request):
    context = {}
    if request.method == 'POST':
        reporterform = ReporterModelForm(request.POST)
        articleform = ArticleModelForm(request.POST)
        if reporterform.is_valid() and articleform.is_valid():
            reporter = reporterform.save()
            article = articleform.save(False)
            article.reporter = reporter
            article.save()
            return redirect('home')

    else:
        reporterform = ReporterModelForm()
        articleform = ArticleModelForm()

    context['reporter'] = reporterform
    context['article'] = articleform

    return render(request, 'myapp/form.html', context)
