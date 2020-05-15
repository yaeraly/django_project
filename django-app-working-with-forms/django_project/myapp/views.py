import datetime
from django.shortcuts import render, redirect

from .forms import ArticleFormSet

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
