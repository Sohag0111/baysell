from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'customer/index.html')

def about(request):
    return render(request, 'customer/about.html')    