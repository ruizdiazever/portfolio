from django.shortcuts import render
from portfolio import urls
from about import urls

def home(request):
    return render(request, 'core/home.html')


