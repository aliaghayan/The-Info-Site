from django.shortcuts import render , redirect
from .models import Address

def home(request):
    return render(request,'home.html',{})

def add_address(request):
    return render(request,'add_address.html',{})

def addresses(request):
    return render(request,'addresses.html',{'addresses':addresses})

# Create your views here.
