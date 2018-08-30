from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
                    
    title = forms.CharField()

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
        fields = ['title', 'description', 'type', 'location', 'support', 'phone', 'contact_me', 'timeframe']
