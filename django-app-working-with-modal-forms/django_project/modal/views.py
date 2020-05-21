from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


from .models import Employee


class HomeListView(generic.ListView):
	model = Employee
	template_name = 'modal/home.html'


class CreateEmployeeView(generic.CreateView):
	model = Employee
	fields = ['first_name', 'last_name', 'email']
	template_name = 'modal/create.html'
	success_url = reverse_lazy('modal:home')


class DeleteEmployeeView(generic.DeleteView):
	model = Employee
	template_name = 'modal/delete.html'
	success_url = reverse_lazy('modal:home')


class UpdateEmployeeView(generic.UpdateView):
	model = Employee
	fields = ['first_name', 'last_name', 'email']
	template_name = 'modal/update.html'
	success_url = reverse_lazy('modal:home')