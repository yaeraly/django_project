from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView

)
from .models import Book, Author, Publisher


class PublisherListView(ListView):
    model = Publisher
    template_name = 'books/home.html'
    context_object_name = 'my_favorite_publishers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['author_list'] = Author.objects.all()
        return context


class PublisherCreateView(CreateView):
    model = Publisher
    fields = ['name', 'address', 'city', 'state_province', 'country', 'website']
    template_name = 'books/create.html'
    success_url = reverse_lazy('home')


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'books/delete.html'
    success_url = reverse_lazy('home')


class PublisherDetailView(DetailView):
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()




class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'authors', 'publisher', 'pub_date']
    template_name = 'books/create.html'
    success_url = reverse_lazy('home')


class BookDetailView(DetailView):
    context_object_name = 'book'
    queryset = Book.objects.all()




class AuthorCreateView(SuccessMessageMixin, CreateView):
    model = Author
    fields = ['salutation', 'name', 'email']
    template_name = 'books/create.html'
    success_message = '%(name)s was created successfully'
    success_url = reverse_lazy('home')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
        )

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'books/delete.html'
    success_url = reverse_lazy('home')
    success_message = '%(name) was deleted successfully'

    def get_success_message(self, cleaned_data):
        return self.success_message %dict(
            cleaned_data,
        )


class AuthorDetailView(DetailView):
    context_object_name = 'author'
    queryset = Author.objects.all()
