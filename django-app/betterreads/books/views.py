from django.shortcuts import render

from books.models import Book


def about(request):
	return render(request, 'books/about.html')


def get_all_books(request):
	books = Book.objects.all()
	return render(request, 'books/book.html', {'data': books})


def get_one_book(request, **kwargs):
	book = Book.objects.get(pk=kwargs['pk'])
	return render(request, 'books/book.html', {'data': book})


def get_old_books(request):
	books = Book.objects.filter(in_print=True)
	return render(request, 'books/book.html', {'data': books})
