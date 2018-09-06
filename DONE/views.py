from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
    return render(request, 'home.html')


def list_projects(request):
    User = get_user_model()
    projects = Project.objects.filter(customer = request.user).order_by('-id')




    return render(request, 'myprojects.html', {'projects' : projects})


def create_project(request):
    User = get_user_model()
    form = ProjectForm(request.POST or None)



    if form.is_valid():
        post = form.save(commit=False)
        post.customer = request.user
        post.save()

        # form.save()
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
