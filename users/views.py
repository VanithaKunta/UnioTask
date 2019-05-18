import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'vidyaConnect.settings'
import django

django.setup()
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.urls import reverse
from .forms import NameForm
from .models import Details

def homeView(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            if Details.objects.count()==1:
                deletion()
            form.save()
            return HttpResponseRedirect(reverse("name1"))
        else:
            print(form.errors)
    else:
        form = NameForm()
        return render(request, 'name1.html', {'form':form})

def deletion():
        Details.objects.all().delete()
        return HttpResponse('deleted')
