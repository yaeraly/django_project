from django.urls import path

from . import views

app_name = 'crud'
urlpatterns = [
	path('', views.book_list, name='book_list'),
	path('create/', views.create_book, name='book_create'),
]