from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    title = 'Página inicial'
    usuario = 'João Henrique'
    return render(request, 'index.html', {'title': title, 'usuario': usuario})

def cadastro(request) -> HttpResponse:
    title = 'Cadastro de usuários'
    usuario = 'João Henrique'
    dados = {}

    if request.method == 'POST':
        nome = request.POST.get('nome')
        tarefa = request.POST.get('tarefa')

        dados = {
            'nome': nome,
            'tarefa': tarefa
        }

    return render(request, 'cadastro.html', {'title': title, 'usuario': usuario, 'dados': dados})
