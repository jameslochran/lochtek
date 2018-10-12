from django import forms
from .models import Project
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):

    title = forms.CharField(required=False)

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Provide a description of your project...',
            'rows' :'3',
        }
    ))
    location = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Provide a location for your project...',
            'rows' :'3',
        }
    ))

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'location', 'support', 'estimated_time','sitetime', 'paymentterms', 'phone', 'contact_me', 'timeframe']



class ContactForm(forms.Form):
    # from_email = forms.EmailField(required=True)
    # subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Please provide any additional information...',
            'rows' :'3',
}



    ), required=True)
    # project_Name = forms.CharField(required=True)



    class Meta:
        model = Project
        fields = ['message']
