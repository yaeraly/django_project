from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import edit


from .models import Employee
from .mixins import ModelMixin
from .forms import EmployeeForm
from .ajax_views import (AjaxCreateView, AjaxDetailView, AjaxUpdateView, AjaxDeleteView)


class EmployeeListView(ModelMixin, generic.ListView):
	model = Employee
	template_name = 'modal/home.html'


class CreateEmployeeView(AjaxCreateView, ModelMixin, edit.CreateView):
	model = Employee
	form_class = EmployeeForm
	ajax_partial = 'modal/partial/employee_form_partial.html'
	ajax_list_partial = 'modal/partial/employee_list_partial.html'


class UpdateEmployeeView(AjaxUpdateView, ModelMixin, edit.UpdateView):
	model = Employee
	form_class = EmployeeForm
	template_name = 'modal/employee_form.html'
	ajax_partial = 'modal/partial/employee_form_partial.html'
	ajax_list_partial = 'modal/partial/employee_list_partial.html'


class DeleteEmployeeView(AjaxDeleteView, ModelMixin, edit.DeleteView):
	model = Employee
	ajax_partial = 'modal/partial/employee_form_partial.html'
	ajax_list_partial = 'modal/partial/employee_list_partial.html'
	success_url = reverse_lazy('modal:home')
