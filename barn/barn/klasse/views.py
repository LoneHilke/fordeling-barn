from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class Base(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'klasse/base.html')