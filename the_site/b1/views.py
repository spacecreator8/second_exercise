from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView



def index(request):
    return render(request, 'index.html')


