from django.shortcuts import render
from .models import Blog
from .models import Certificates
from .models import Docs

def home(request):
    blog = Blog.objects.all()
    return render(request, 'core/home.html', {'blog':blog})

def certificates(request):
    certificates = Certificates.objects.all()
    return render(request, 'core/certificates.html', {'certificates':certificates})

def docs(request):
    docs = Docs.objects.all()
    return render(request, 'core/docs.html', {'docs':docs})