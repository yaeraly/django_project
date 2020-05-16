from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Article, Reporter
from .forms import ArticleForm


class HomeListView(generic.ListView):
    model = Reporter
    template_name = 'myapp/home.html'


class CreateReporterView(generic.CreateView):
    model = Reporter
    fields = ['first_name']
    template_name = 'myapp/create.html'
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('home')


class UpdateReporterView(generic.UpdateView):
    model = Reporter
    fields = ['first_name']
    template_name = 'myapp/update.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')


class DeleteReporterView(generic.DeleteView):
    model =  Reporter
    template_name = 'myapp/delete.html'
    template_name_suffix = '_check_delete'
    success_url = reverse_lazy('home')
