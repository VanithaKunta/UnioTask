from django import forms
from .models import Details
from django.forms import ModelForm

class NameForm(ModelForm):
    class Meta:
        model=Details
        exclude=()