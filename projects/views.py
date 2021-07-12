from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Unsere Projekte')

def project(request, pk):
    return HttpResponse('Ein einzelnes Projekt' + ' ' + str(pk))
