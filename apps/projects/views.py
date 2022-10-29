from django.shortcuts import render
from apps.projects.models import Projects


def projects(request):
    projects = Projects.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})
