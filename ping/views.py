from datetime import datetime
from django.shortcuts import render, redirect
from requests import request
from ping.models import presence
from compte.models import users
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.


def ping(request):
    if request.method == 'POST':
        date = datetime.now()
        arr = presence.objects.create(date=date, user=request.user, matin=datetime.now())
        arr.save()
        return redirect('hello')
    

def soir(request):
    if request.method == 'POST':
        date = datetime.now()
        arr = presence.objects.get(date=date, user=request.user,)
        if arr:
            arr.soir = date
            arr.save()
            return redirect('hello')
        else:
            messages.error(request, "vous n'etes pas connecté")
            return redirect('hello')

        
    
@login_required(login_url='acces')

def chef(request):
    presenceChef = presence.objects.all().order_by('date')#(merci emre)
    context = {'presenceChef': presenceChef}
    return render(request, 'compte/chef.html', context)