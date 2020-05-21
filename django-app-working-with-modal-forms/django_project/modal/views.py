from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Post, Comment


class HomeListView(generic.ListView):
	model = Post
	template_name = 'modal/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comment_list'] = Comment.objects.all()
		return context


class CreatePostView(generic.CreateView):
	model = Post
	fields = ['title']
	template_name = 'modal/create.html'
	success_url = reverse_lazy('modal:home')


class CreateCommentView(generic.CreateView):
	model = Comment
	fields = ['content', 'post']
	template_name = 'modal/create.html'
	success_url = reverse_lazy('modal:home')


class DeletePostView(generic.DeleteView):
	model = Post 
	template_name = 'modal/delete.html'
	success_url = reverse_lazy('modal:home')


class DeleteCommentView(generic.DeleteView):
	model = Comment
	template_name = 'modal/delete.html'
	success_url = reverse_lazy('modal:home')