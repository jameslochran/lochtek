from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):

    architectural = 'Architectural'
    electrical =  'Electrical'
    mechanical = 'Mechanical'
    structural = 'Structural build or Demo'
    multi_discipline = 'Multi-discipline'
    PROJTYPE = (
                (architectural, 'Architectural'),
                (electrical,  'Electrical'),
                (mechanical, 'Mechanical'),
                (structural, 'Structural build or Demo'),
                (multi_discipline, 'Multi-discipline')
                )

    project_manager = 'Project Manager'
    construction_manager = 'Construction Manager'
    admin = 'Admin'
    SUPPORT = (
        (project_manager, 'Project Manager'),
        (construction_manager, 'Construction Manager'),
        (admin,'Admin')
         )

    email_me = 'Email'
    call_me = 'Call'
    both = 'Both'
    CONTACT_ME = (
                (email_me, 'Email'),
                (call_me, 'Call'),
                (both, 'Both')
                )

    weeks = 'Less than 2 weeks'
    month = '1 month'
    months = '1 to 3 months'
    WHEN = (
        (weeks, 'Less than 2 Weeks'),
        (month, '1 Month'),
        (months, '1 to 3 months')
        )



    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(("description"), max_length=2000, null=True, blank=True)
    date_created = models.DateTimeField(("date"), auto_now_add = True)
    date_changed = models.DateTimeField(("changed date"), auto_now = True)
    type = models.CharField(("Project Type"), max_length=100, choices=PROJTYPE, default='Architectural')
    location = models.TextField(('location'), max_length=500, null=True, blank=True)
    support = models.CharField(("Support Needed"), max_length=100, choices=SUPPORT, default='Project Manager')
    phone = models.CharField(('Phone'), max_length=20, null=True, blank=True)
    contact_me = models.CharField(("Best Way to Contact Me"), max_length=100, choices=CONTACT_ME, default='Email')
    timeframe = models.CharField(("When do you need help"), max_length=100, choices=WHEN, default='Weeks')
    # pub_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title


    def summary(self):
        return self.description[:100]


    # def pub_date_pretty(self):
    #     return self.pub_date.strftime('%b %e %Y')
