from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pongal(request):
    return HttpResponse('Happy pongal sajid sir')
