from django.shortcuts import render
from account.models import Account


def home_screen_view(request):
    accounts = Account.objects.all()
    return render(request, 'personal/home.html', {'accounts': accounts})
