from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserCreationForm


def home(request):
    users = User.objects.all()
    return render(request, 'auth_app/home.html', {'users': users})


def delete(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, f'Successfully deleted "{user}" user.')
        return redirect('home')

    return render(request, 'auth_app/delete.html', {'user': user})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'The user “{username}” was added successfully.')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
