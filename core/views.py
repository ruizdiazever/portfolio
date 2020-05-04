from django.shortcuts import render
from .models import Blog

def home(request):
    blog = Blog.objects.all()
    return render(request, 'core/home.html', {'blog':blog})


