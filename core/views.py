from django.shortcuts import render
from portfolio import urls

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')
