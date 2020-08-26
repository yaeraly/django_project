from django.shortcuts import render, redirect
from django.views.generic import View
from django.forms.models import model_to_dict
from django.http import JsonResponse


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
			new_form = form.save()
			return JsonResponse({'person': model_to_dict(new_form)}, status=200)
		else:
			return redirect('form')


class DeleteView(View):
	def post(self, request, id):
		person = Person.objects.get(id=id)
		person.delete()

		return JsonResponse({'result': 'ok'}, status=200)