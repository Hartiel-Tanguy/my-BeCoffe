from atexit import register
from multiprocessing import context
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import creerUtilisateur
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from compte.models import users
from ping.models import presence




# Create your views here.
def inscriptionPage(request):
    form = creerUtilisateur()
    if request.method == 'POST':
        form = creerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acces')
    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


def accesPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Identifiant ou mot de passe incorrect')
    return render(request, 'compte/acces.html', context)


def logoutUser(request):
    logout(request)
    return redirect('acces')


@login_required(login_url='acces')
def hello(request):
    return render(request, 'compte/hello.html',)



def index_profile(request,id):
    userr = users.objects.get(id=id)
    form = creerUtilisateur(instance=userr)
    presencess = presence.objects.filter(user=id)
    
    if request.method == 'POST':
        form = creerUtilisateur(request.POST, instance=userr)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.success(request, "non d'utilisateur deja utilisé ou mot de passe tros court")
    return render(request, 'compte/index_profile.html', {'form': form, 'userr':userr ,'presencess': presencess})
    

    