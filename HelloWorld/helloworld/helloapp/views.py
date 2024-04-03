# from django.shortcuts import render

from django.http import HttpResponse


def hello_view(request):
    return HttpResponse('Hello, World!')

def name_view(request):
    return HttpResponse('Филип Васић')