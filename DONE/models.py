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
    sales = 'Technical Sales'
    SUPPORT = (
        (project_manager, 'Project Manager'),
        (construction_manager, 'Construction Manager'),
        (admin,'Admin'),
        (sales, 'Technical Sales')
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

    etdays = 'Less than 1 month'
    etmonth = '1 month'
    et3months = '3 months'
    et6months = '6 months'
    et12months = "12 months"
    ESTIMATED_TIME = (
        (etdays, 'Less than 1 month'),
        (etmonth, '1 month'),
        (et3months, '3 months'),
        (et6months, '6 months'),
        (et12months, '12 months')
        )

    pt30days = 'Net 30 days'
    pt15days = 'Net 15 days'
    pt45days = 'Net 45 days'
    pt90days = 'Net 90 days'
    pt120days = "Net 120 days"
    pt180days = "Net 180 days"
    PAYMENTTERMS = (
        (pt30days, 'Net 30 days'),
        (pt15days, 'Net 15 days'),
        (pt45days, 'Net 45 days'),
        (pt90days, 'Net 90 days'),
        (pt120days, 'Net 120 days'),
        (pt180days, 'Net 180 days')
        )

    stfulltime = 'Onsite'
    sthalftime = 'Offsite'
    stquartertime = 'Both'
    SITETIME = (
        (stfulltime, 'Onsite'),
        (sthalftime, 'Offsite'),
        (stquartertime, 'Both')
        )



    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(("description"), max_length=2000, null=True, blank=True)
    date_created = models.DateTimeField(("date"), auto_now_add = True)
    date_changed = models.DateTimeField(("changed date"), auto_now = True)
    type = models.CharField(("Project Type"), max_length=100, choices=PROJTYPE, default='Architectural')
    location = models.TextField(('location'), max_length=500, null=True, blank=True)
    support = models.CharField(("Support Needed"), max_length=100, choices=SUPPORT, default='Project Manager')
    estimated_time =  models.CharField(("Estimated project duration"), max_length=100, choices=ESTIMATED_TIME, default='1 month')
    sitetime = models.CharField(("Support Location"), max_length=100, choices=SITETIME, default='Onsite')
    paymentterms = models.CharField(("Payment terms"), max_length=100, choices=PAYMENTTERMS, default='Net 30 days ')
    phone = models.CharField(('Phone'), max_length=20, null=True, blank=True)
    contact_me = models.CharField(("Best Way to Contact Me"), max_length=100, choices=CONTACT_ME, default='Email')
    timeframe = models.CharField(("When do you need help"), max_length=100, choices=WHEN, default='Weeks')
    # pub_date = models.DateTimeField(null=True, blank=True)
    baserate = models.PositiveSmallIntegerField(default=90, blank=True, null=True)
    apr = models.FloatField(('Cost of money'),null=True, blank=True, default=0.2674)
    aprh = models.FloatField(('APR per hour'), null=True, blank=True, default=0.000093)
    aprd = models.FloatField(('APR per day'), null=True, blank=True, default=0.0008)
    hpd = models.PositiveSmallIntegerField(('Hours per day'), default=8, blank=True, null=True)



    def __str__(self):
        return self.title


    def summary(self):
        return self.description[:100]

    def estimatedProjectCost(self):
        #transform terms into an integer
        if self.paymentterms == 'Net 30 days':
            pt = 30;
        elif self.paymentterms == 'Net 15 days':
            pt = 15;
        elif self.paymentterms == 'Net 60 days':
            pt = 60;
        elif self.paymentterms == 'Net 90 days':
            pt = 90;
        elif self.paymentterms == 'Net 120 days':
            pt = 120;
        elif self.paymentterms == 'Net 180 days':
            pt = 180;


#transform the duration into an integer
        if self.estimated_time == 'Less than one month':
            et = 10;
        elif self.estimated_time == '1 month':
            et = 20;
        elif self.estimated_time == '3 months':
            et = 60;
        elif self.estimated_time == '6 months':
            et = 120;
        elif self.estimated_time == '12 months':
            et = 240;

#cost per day
        cpd = ((self.aprd * pt)+1)*(self.baserate*self.hpd);
#Estimated project cost
        epc = round(cpd * et);
        return epc



    # def pub_date_pretty(self):
    #     return self.pub_date.strftime('%b %e %Y')
