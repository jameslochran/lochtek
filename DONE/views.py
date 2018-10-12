from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm, ContactForm
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError

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
        #return redirect('list_projects')
        from_email = request.user.email
        subject = 'Please send me a quote'
        message = 'Project title: ' +  post.title + '\n How I want to be contacted: ' + post.contact_me  + '\n Description: ' + post.description + '\n Type: ' + post.type +  '\n Support: ' + post.support +  '\n Timeframe: '+ post.timeframe +  '\n Login to DONE admin for details http://127.0.0.1:8000/admin/'
        recipient_list = ['jlochran@gmail.com']
        # html_message = '<h2> Please review project</h2>'

        try:
            send_mail (subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('success')

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


@login_required
def emailView(request, id):
    User = get_user_model()
    project = Project.objects.get(id=id)
    print (project.paymentterms)
    if request.method == 'GET':
        form = ContactForm()
        # form.from_email = request.user.email
        # print(form.from_email)


    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = request.user.email
            subject = 'Please send me a quote'
            message = 'Client message: ' + form.cleaned_data['message'] + '\n Project title: ' + project.title +  '\n How I want to be contacted: ' + project.contact_me + '\n Description: ' + project.description + '\n Type: ' + project.type + '\n Support: ' + project.support + '\n Timeframe: ' + project.timeframe + '\n Login to DONE admin for details http://127.0.0.1:8000/admin/'
            recipient_list = ['jlochran@gmail.com']
            # html_message = '<h2> Please review project</h2>'

            try:
                send_mail (subject, message, from_email, recipient_list)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return render(request, "success.html")
