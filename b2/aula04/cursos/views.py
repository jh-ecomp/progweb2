from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Cursos, Aulas

# Create your views here.

def home(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.session.get('usuario'):
        cursos =  Cursos.objects.all()
        request_usuario = request.session.get('usuario', '')
        return render(request, 'home.html', {'cursos': cursos, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')

def sair(request: HttpRequest) -> HttpResponseRedirect:
    request.session.flush()
    return redirect('/auth/login/')

def curso(request: HttpRequest, id: int) -> HttpResponse | HttpResponseRedirect:
    if request.session.get('usuario'):
        aulas = Aulas.objects.filter(curso = id)
        reques_usuario = request.session.get('usuario')
        return render(request, 'curso.html', {'aulas': aulas, 'reques_usuario': reques_usuario})
    else:
        return redirect('/auth/login?status=2')

def aula(request: HttpRequest, id: int) -> HttpResponse | HttpResponseRedirect:
    if request.session.get('usuario'):
        aula = Aulas.objects.get(id = id)
        return render(request, 'aula.html', {'aula': aula})
    else:
        return redirect('/auth/login/?status=2')