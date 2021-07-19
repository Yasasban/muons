from django.http.response import HttpResponse 
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView


def index(request):
    print(request.user)
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def profile(request):
    return render(request, 'profile.html')

