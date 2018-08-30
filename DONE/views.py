from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.utils import timezone

# Create your views here.
def list_projects(request):
    projects = Project.objects.all()
    return render(request, 'myprojects.html', {'projects' : projects})


def create_project(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():

        form.save()
        return redirect('list_projects')

    return render(request, 'project-form.html', {'form' : form})

def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect('list_projects')

    return render(request, 'project-form.html', {'form' : form, 'project' : project})


def delete_project(request, id):
    project = Project.objects.get(id=id)

    if request.method == 'POST':
        project.delete()
        return redirect('list_projects')

    return render(request, 'proj-delete-confirm.html' , {'project' : project})
