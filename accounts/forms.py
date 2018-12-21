from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',



        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    # template_name='/something/else'
    email = forms.EmailField(required=True)
    # website = forms.URLField(required=False)
    # title = forms.CharField(required=False)
    # company = forms.CharField(required=False)


    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            # 'company',
            # 'website',
            # 'title',
            'password',

)
    # def save(self, commit=True):
    #     profile = super(EditProfileForm, self).save(commit=False)
    #     profile.company = self.cleaned_data['company']
    #     profile.title = self.cleaned_data['title']
    #     profile.website = self.cleaned_data['website']
    #
    #     if commit:
    #         profile.save()
    #
    #     return profile
