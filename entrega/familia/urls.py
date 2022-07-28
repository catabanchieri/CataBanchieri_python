from django.urls import path

from familia.views import create_member, list_family


urlpatterns = [path('create-member/',create_member,name='create_member'),
path('family-list/',list_family,name='family list')]