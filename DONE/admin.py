from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ('date_changed','title','summary', 'estimatedProjectCost')

    def project_info(self, obj):
        return obj.estimatedProjectCost

    def get_queryset(self, request):
        queryset = super(ProjectDetailAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-date_changed')
        return queryset

    # user_info.short_description = 'Info'
admin.site.register(Project, ProjectDetailAdmin)
