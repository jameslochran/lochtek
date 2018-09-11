from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import (
    RegistrationForm,
    EditProfileForm,

)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

# Create your views here.
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(reverse('accounts:view_profile'))
            return redirect('accounts:login')
        return render(request, 'accounts/reg_form.html', {'form': form})


    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        # profile = UserProfile.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            # return redirect('list_projects')
            return redirect(reverse('accounts:view_profile'))
        return render(request, 'accounts/edit_profile.html', {'form': form})


    else:
        form = EditProfileForm(instance=request.user)


        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'accounts/profile.html')
        else:
            return render(request, 'accounts/change_password.html', {'form' :form })
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)



    #HttpResponse('Success! Thank you for your message.')

    # template_name = "accounts/edit_profile.html"
    # http_method_names = ['get', 'post']
    #
    # def get(self, request, *args, **kwargs):
    #     user = self.request.user
    #     if "user_form" not in kwargs:
    #         kwargs["RegistrationForm"] = forms.RegistationForm(instance=user)
    #     if "EditProfileForm" not in kwargs:
    #         kwargs["profile_form"] = forms.EditProfileForm(instance=user.profile)
    #     return super().get(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     user = self.request.user
    #     user_form = forms.RegistationForm(request.POST, instance=user)
    #     profile_form = forms.EditProfileForm(request.POST,
    #                                      request.FILES,
    #                                      instance=user.profile)
    #     if not (user_form.is_valid() and profile_form.is_valid()):
    #         messages.error(request, "There was a problem with the form. "
    #                        "Please check the details.")
    #         user_form = forms.RegistationForm(instance=user)
    #         profile_form = forms.EditProfileForm(instance=user.profile)
    #         return super().get(request,
    #                            user_form=user_form,
    #                            profile_form=profile_form)
    #     # Both forms are fine. Time to save!
    #     user_form.save()
    #     profile = profile_form.save(commit=False)
    #     profile.user = user
    #     profile.save()
    #     messages.success(request, "Profile details saved!")
    #     return redirect("accounts:view_profile")

# def signup(request):
#     if request.method=='POST':
#         try:
#             if request.POST['password1'] == request.POST['password2']:
#                 user = User.objects.get(username=request.POST['username'])
#                 return render(request, 'accounts/signup.html', {'error':'User Name has already been taken'})
#
#         except User.DoesNotExist:
#             user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
#             auth.login(request, user)
#             return redirect('list_projects')
#         else:
#             return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
#
#     else:
#         return render(request, 'accounts/signup.html')
#
# def login(request):
#     if request.method=='POST':
#         user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
#
#         if user is not None:
#             auth.login(request, user)
#             return redirect('list_projects')
#         else:
#             return render(request, 'accounts/login.html', {'error':'username or password is incorrect'})
#
#     else:
#         return render(request, 'accounts/login.html')
#
#
#
#
# def logout(request):
#     if request.method =='POST':
#         auth.logout(request)
#         return redirect('list_projects')
