from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from myapp.models import Author

def home(request):
    authors = Author.objects.all()
    return render(request, 'myapp/home.html', {'authors': authors})


class AuthorCreateView(CreateView):
    model = Author
    template_name_suffix = '_create_form'
    template_name = 'myapp/author_create_form.html'
    fields = ['name']
    success_url = reverse_lazy('home')


class AuthorUpdateView(UpdateView):
    model = Author
    template_name_suffix = '_update_form'
    template_name = 'myapp/author_update_form.html'
    fields = ['name']
    success_url = reverse_lazy('home')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name_suffix = '_confirm_delete'
    template_name = 'myapp/author_delete_form.html'
    success_url = reverse_lazy('home')
