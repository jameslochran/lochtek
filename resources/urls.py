from django.urls import path
from .views import create_resource, delete_resource, update_resource, list_resources, resourceView

urlpatterns = [
    path('new/', create_resource, name='create_resource'),
    path('delete/<int:id>/', delete_resource, name='delete_resource'),
    path('update/<int:id>/', update_resource, name='update_resource'),
    path('myprofile', list_resources, name='my_profile'),
    # path('resource/', resourceView, name='resource'),
    path('', resourceView, name='resource'),



]
