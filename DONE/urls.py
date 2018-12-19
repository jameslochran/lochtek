from django.urls import path
from .views import list_projects, create_project, update_project, delete_project, home, emailView, successView, contactView, aboutView, base_layout

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', list_projects, name='list_projects'),
    path('new', create_project, name='create_project'),
    path('update/<int:id>/', update_project, name='update_project'),
    path('delete/<int:id>/', delete_project, name='delete_project'),
    path('email/<int:id>/', emailView, name='email'),
    path('success/', successView, name='success'),
    path('contact/', contactView, name='contact'),
    path('about/', aboutView, name='about'),

]
