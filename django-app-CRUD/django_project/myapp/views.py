from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import Author



class HomeListView(ListView):
    model = Author
    template_name = 'myapp/home.html'


class ContactView(FormView):
    template_name = 'myapp/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


class CreateAuthorView(CreateView):
    model = Author
    fields = ['name',]
    template_name = 'myapp/create.html'
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('home')


class UpdateAuthorView(UpdateView):
    model = Author
    fields = ['name',]
    template_name = 'myapp/update.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')


class DeleteAuthorView(DeleteView):
    model = Author
    template_name = 'myapp/delete.html'
    template_name_suffix = '_check_delete'
    success_url = reverse_lazy('home')
