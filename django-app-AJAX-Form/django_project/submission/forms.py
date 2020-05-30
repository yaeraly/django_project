from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
	first_name = forms.CharField(
		widget=forms.TextInput(attrs={
			'class': 'form-control', 
			'type': 'text',
			'placeholder': 'First Name'
		})
	)
	last_name = forms.CharField(
		widget=forms.TextInput(attrs={
			'class': 'form-control', 
			'type': 'text',
			'placeholder': 'Last Name'
		})
	)
	class Meta:
		model = Person 
		fields = ['first_name', 'last_name']