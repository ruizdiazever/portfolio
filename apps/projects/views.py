from django.shortcuts import render
from .models import Projects

def projects(request):
    projects = Projects.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})
