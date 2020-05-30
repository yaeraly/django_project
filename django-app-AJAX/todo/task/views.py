from django.shortcuts import render, redirect
from django.views.generic import View


from .models import Task 
from .forms import TaskForm


class TaskList(View):
	def get(self, request):
		context = {}
		form = TaskForm()
		tasks = Task.objects.all()

		context['form'] = form
		context['tasks'] = tasks
		return render(request, 'task/task_list.html', context)


	def post(self, request):
		form = TaskForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('task_list_url')
		else:
			return redirect('task_list_url')