from django.shortcuts import render
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
