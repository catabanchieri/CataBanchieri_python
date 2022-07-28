from django.shortcuts import render
from familia.models import family_members

# Create your views here.

def create_member(request):
    new_member=family_members.objects.create(relation='Madre', name='Virginia', age= 63, gender= 'femenino')
    
    context={'new_member':new_member}
    
    return render(request,'new_member.html',context=context)

def list_family(request):
    family=family_members.objects.all()
    context={'family_members':family}
    return render(request,'family_list.html',context=context)