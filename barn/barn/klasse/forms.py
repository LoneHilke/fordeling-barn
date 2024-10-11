from django import forms
from django.forms import ModelForm
from .models import Barn, Personale 

class BarnForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'Tilføj barn...'}))

  class Meta:
    model = Barn 
    fields = '__all__'

class PersonaleForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'Tilføj Personale...'}))

  class Meta:
    model = Personale 
    fields = '__all__'