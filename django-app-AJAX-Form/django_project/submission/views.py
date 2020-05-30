from django.shortcuts import render, redirect
from django.views.generic import View


from .models import Person
from .forms import PersonForm


class FormView(View):
	def get(self, request):
		context = {}
		form = PersonForm()
		people = Person.objects.all()
		context['people'] = people
		context['form'] = form
		return render(request, 'submission/submission_form.html', context)

	def post(self, request):
		form = PersonForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('form')
		else:
			return redirect('form')