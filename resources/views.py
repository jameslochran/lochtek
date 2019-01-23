from django.shortcuts import render, redirect
from .models import Resources
from .forms import ResourceForm
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required



# Create your views here.


def create_resource(request):
    User = get_user_model()
    form = ResourceForm(request.POST, request.FILES)

    if form.is_valid():
        post = form.save()
        post.resource = request.user
        post.save()

        # form.save()
        return redirect('my_profile')
        # from_email = request.user.email
        # subject = 'Please send me a quote'
        # message = 'Project title: ' +  post.title + '\n How I want to be contacted: ' + post.contact_me  + '\n Description: ' + post.description + '\n Type: ' + post.type +  '\n Support: ' + post.support +  '\n Timeframe: '+ post.timeframe +  '\n Login to DONE admin for details http://127.0.0.1:8000/admin/'
        # recipient_list = ['jlochran@gmail.com']
        # html_message = '<h2> Please review project</h2>'

        # try:
        #     send_mail (subject, message, from_email, recipient_list)
        # except BadHeaderError:
        #     return HttpResponse('Invalid header found.')
        # return redirect('success')
    return render(request, 'resource-form.html', {'form' : form})

#edit resource
def update_resource(request, id):
    rprofile = Resources.objects.get(id=id)
    form = ResourceForm(request.POST or None, instance=rprofile)

    if form.is_valid():
        form.save()
        return redirect('my_profile')

    return render(request, 'resource-form.html', {'form' : form, 'rprofile' : rprofile})
#
# delete resource
def delete_resource(request, id):
    rprofile = Resources.objects.get(id=id)

    if request.method == 'POST':
        rprofile.delete()
        return redirect('my_profile')

    return render(request, 'resource-delete.html' , {'rprofile' : rprofile})

#List resources
def list_resources(request):
    User = get_user_model()
    rprofile = Resources.objects.filter(resource = request.user)
    # rprofile = Resources.objects.all()

    return render(request, 'myprofile.html', {'rprofile' : rprofile})


# resouce view
def resourceView(request):
    # template='about.html'
    return render(request, 'resource.html')
