from django.shortcuts import render, redirect
from django.contrib import messages

from account.forms import RegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'The username "{username}" was added successfully')
            return redirect('home')

    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
