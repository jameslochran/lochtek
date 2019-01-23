from django import forms
from .models import Resources
from django.contrib.auth.models import User

class ResourceForm(forms.ModelForm):

    PROFICIENCY = (
            ('project_mgmt', 'Project Management'),
            ('construction_mgmt', 'Construction Management'),
            ('architectural', 'Architectural'),
            ('mechanical', 'Mechanical'),
            ('electrical', 'Electrical'),
            ('construction', 'Construction'),
            ('engineering', 'Engineering'),
            ('aviation', 'Aviation'),
            ('r_d', 'R&D'),
            ('power_energy', 'Power / Energy'),
            ('manufacturing', 'Manufacturing'),
            ('process', 'Process'),
            ('environmental', 'Environmental'),
            ('maritime_marine', 'Maritime / Marine'),
            ('military', 'Military'),
            ('multi_eng_construction', 'Multidiscipline engineering / construction')
            )

    DISTANCE = (
            ('less_ten', '< 10 miles'),
            ('ten_twenty', '10 to 20 miles'),
            ('twenty_plus', '> 20 miles'),
            ('unlimited', 'Unlimited with expenses')
            )
# days able to work
    DAYS = (
            ('monday_friday', 'Monday to Friday'),
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
            ('Saturday', 'Saturday'),
            ('Sunday', 'Sunday')
            )

    # phone = forms.CharField(required=True)

    proficiency = forms.MultipleChoiceField(
                    choices=PROFICIENCY,
                    initial='Project Management',
                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'special'}),
                    required=True,
                    label='Proficiency (select all that apply)',
                    )

    distance= forms.MultipleChoiceField(
                    choices=DISTANCE,
                    initial='Unlimited with expenses',
                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'special'}),
                    required=False,
                    label='Distances you\'re willing to travel (select all that apply)',
                    )
    days_available = forms.MultipleChoiceField(
                    choices=DAYS,
                    initial='Monday to Friday',
                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'special'}),
                    required=False,
                    label='Days you\'re available (select all that apply)',
                    )








    #  = forms.CharField(widget=forms.Textarea(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Provide a description of your project...',
    #         'rows' :'3',
    #     }
    # ))
    # location = forms.CharField(widget=forms.Textarea(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Provide a location for your project...',
    #         'rows' :'3',
    #     }
    # ))

    class Meta:
        model = Resources
        fields = ['phone', 'street', 'city', 'state', 'zip','cv', 'proficiency', 'work_exp', 'distance', 'max_days', 'max_hours', 'days_available', 'rate']
