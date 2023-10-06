from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as django_logout
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Ja existe um usuario com esse username')
        
        user = User.objects.create_user(username = username, email = email, password = senha)
        user.save()

        return HttpResponse('Cadastro realizado')

def login(request):
    if request.method =="GET":
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha invalidos')

@login_required(login_url='/auth/login')
def plataforma(request):
    return HttpResponse('plat')

@login_required(login_url='/auth/login')
def logout(request):
    django_logout(request)
    return HttpResponse('Deslogado com sucesso')