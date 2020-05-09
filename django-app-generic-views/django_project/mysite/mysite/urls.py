"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views as books_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', books_views.PublisherListView.as_view(), name='home'),


    path('publisher_create/', books_views.PublisherCreateView.as_view(), name='publisher_create'),
    path('publisher_delete/<int:pk>/', books_views.PublisherDeleteView.as_view(), name='publisher_delete'),
    path('publisher_detail/<int:pk>/', books_views.PublisherDetailView.as_view(), name='publisher_detail'),

    path('book_create/', books_views.BookCreateView.as_view(), name='book_create'),
    path('book_detail/<int:pk>/', books_views.BookDetailView.as_view(), name='book_detail'),

    path('author_create/', books_views.AuthorCreateView.as_view(), name='author_create'),
    path('author_delete/<int:pk>/', books_views.AuthorDeleteView.as_view(), name='author_delete'),
    path('author_detail/<int:pk>/', books_views.AuthorDetailView.as_view(), name='author_detail'),
]
