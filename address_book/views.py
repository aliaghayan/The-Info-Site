from django.shortcuts import render , redirect
from .models import Address
from .forms import InfoForm
from django.contrib import messages


def home(request):
    return render(request,'home.html',{})

def addresses(request):
    addresses = Address.objects.all
    return render(request,'addresses.html',{'addresses':addresses})

def add_address(request):
    if request.method == 'POST':
        form = InfoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Info Has Been Added'))
            return redirect('addresses')
        else:
            messages.success(request,('Seems Like There Was A MIstake , Try Again Please...'))
            return render(request,'add_address.html',{})
    else:
        return render(request,'add_address.html',{})

def edit(request,list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(pk=list_id)
        form = InfoForm(request.POST or None, instance=current_address)
        if form.is_valid():
            form.save()
            messages.success(request,('Info Has Been Edited'))
            return redirect('addresses')
        else:
            messages.success(request,('Seems Like There Was A MIstake , Try Again Please...'))
            return render(request,'edit.html',{})
    else:
        get_address = Address.objects.get(pk=list_id)
        return render(request,'edit.html',{'get_address':get_address})

# Create your views here.
