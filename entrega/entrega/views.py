from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def bienvenida(request):
    return HttpResponse('BIENVENIDO A ESTA PAGINA')

def template1(request):
    context={'nombre': 'catalina', 'apellido':'banchieri'}
    return render(request,'template1.html',context=context)   