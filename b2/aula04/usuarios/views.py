from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from . models import Usuario
import hashlib

# Create your views here.


def cadastro(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def login(request: HttpRequest) -> HttpResponse:
    status = request.GET.get('status', '')
    
    if request.session.get('usuario'):
        return redirect('/home/')
    return render(request, 'login.html', {'status': status})


def valida_cadastro(request: HttpRequest) -> HttpResponse:
    nome = request.POST.get('nome', '')
    email = request.POST.get('email', '')
    senha = request.POST.get('senha', '')

    # request.session['user'] = nome # isso cria uma variável de sessão

    usuario = Usuario.objects.filter(email= email)

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=1')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=2')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome,
                          email=email,
                          senha=senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

def valida_login(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    email = request.POST.get('email', '')
    senha = request.POST.get('senha', '')

    senha = hashlib.sha256(senha.encode()).hexdigest()
    usuarios = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuarios) <= 0:
        return redirect('/auth/login/?status=1')
    else:
        request.session['usuario'] = usuarios[0].pk
        return redirect('/home/')

