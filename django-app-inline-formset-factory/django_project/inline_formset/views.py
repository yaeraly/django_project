from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory

from .models import Programmer, Language


def home(request):
    programmers = Programmer.objects.all()
    return render(request, 'inline_formset/home.html', {'programmers': programmers})


def create(request, pk):
    programmer = Programmer.objects.get(id=pk)
    # LanguageFormSet = modelformset_factory(Language, fields=('name',))
    LanguageFormSet = inlineformset_factory(Programmer, Language, fields=('name',), can_delete=False)

    if request.method == 'POST':
        # form = ProgrammerFormSet(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        form = LanguageFormSet(request.POST, instance=programmer)

        if form.is_valid():
            form.save()
            # intances = form.save(commit=False)
            # for intance in intances:
                # intance.programmer_id = programmer.id
                # intance.save()
            return redirect('home')
    else:
        # form = LanguageFormSet(queryset=Language.objects.filter(programmer__id=programmer.id))
        form = LanguageFormSet(instance=programmer)

    return render(request, 'inline_formset/create.html', {'form': form})
