from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string


from .forms import BookForm
from .models import Book

def book_list(request):
	books = Book.objects.all()
	context = {'books': books}

	return render(request, 'crud/book_list.html', context)


def create_book(request):
	form = BookForm()
	context = {
		'form': form,
	}

	html_form = render_to_string('bool_create.html', context, request=request)
	return JsonResponse({'html_form': html_form})