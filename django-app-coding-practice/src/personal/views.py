from django.shortcuts import render

def home_screen_view(request):
    string_value = 'eraly TOktonazarov'
    return render(request, 'personal/home.html', {'string_value': string_value})
