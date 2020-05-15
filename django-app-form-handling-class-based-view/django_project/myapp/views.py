from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import NameForm


def home(request):
    return render(request, 'myapp/home.html')

class ContactView(FormView):
    template_name = 'myapp/contact.html'
    form_class = NameForm
