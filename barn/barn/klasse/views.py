from django.shortcuts import render, redirect
from django.views import View
from .models import Barn, Klasse, Personale
from .forms import BarnForm, PersonaleForm

# Create your views here.
class Base(View):
    def get(self, request, *args, **kwargs):
        Barn.objects.all()
        form = BarnForm(request.POST)
        forms = PersonaleForm(request.POST)

        context = {
            'form' : form,
            'forms': forms,
        }

    

        return render(request, 'klasse/base.html', context)
    
    def post(self, request, *args, **kwargs):
    
        form = BarnForm(request.POST)
        
        if form.is_valid():
            form.save()
        
            return redirect('/')
    def post(self, request, *args, **kwargs):    
        forms = PersonaleForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')

class Barnview(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'klasse/barn.html')