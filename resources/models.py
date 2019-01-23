from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.

class Resources(models.Model):

    # proficiency options
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
# distance to travel
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

# Set up table
    resource = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(("date"), auto_now_add = True)
    date_changed = models.DateTimeField(("changed date"), auto_now = True)
    cv = models.FileField(('Resume / CV'),upload_to='cv/', null=True, blank=True) #CV upload
    street = models.CharField(('Street'), max_length=100, null=True, blank=True)
    city = models.CharField(('City'), max_length=100, null=True, blank=True)
    state = models.CharField(('State'), max_length=100, null=True, blank=True)
    zip =  models.CharField(('Zip code'), max_length=100, null=True, blank=True)
    work_exp = models.PositiveSmallIntegerField(('Years of professional experience'), default=1, blank=True, null=True)
    phone = models.CharField(('Phone'), max_length=20, null=True, blank=True)
    proficiency = MultiSelectField(("Proficiency"), choices=PROFICIENCY)
    distance = MultiSelectField(("Travel Distance"), choices=DISTANCE)
    max_days = models.PositiveSmallIntegerField(('Maximum number of work days per week'), default=5, blank=True, null=True)
    max_hours = models.PositiveSmallIntegerField(('Maximum work hours per day'), default=8, blank=True, null=True)
    days_available = MultiSelectField(("Days available"), choices=DAYS)
    rate = models.PositiveSmallIntegerField(('Rate / hr'), default=50, blank=True, null=True)



    def __str__(self):
        return self.phone
