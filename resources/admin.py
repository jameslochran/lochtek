from django.contrib import admin
from .models import Resources

# Register your models here.

# Register your models here.
class ResouceDetailAdmin(admin.ModelAdmin):
    list_display = ('resource','phone','date_changed','street','city', 'state', 'zip', 'cv', 'proficiency', 'distance', 'days_available', 'work_exp' )

    def project_info(self, obj):
        return obj.work_exp

    def get_queryset(self, request):
        queryset = super(ResouceDetailAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-date_changed')
        return queryset

    # user_info.short_description = 'Info'
admin.site.register(Resources, ResouceDetailAdmin)
