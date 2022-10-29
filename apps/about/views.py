from django.shortcuts import render
from apps.about.models import About

def about(request):
    about = About.objects.all()
    return render(request, 'about/about.html', {'about':about})