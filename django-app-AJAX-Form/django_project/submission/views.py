from django.shortcuts import render
from django.views.generic import View


class FormView(View):
	def get(self, request):
		return render(request, 'submission/submission_form.html')
