Atividade prática – Painel de Alunos com Django




A proposta é criar um Painel de Alunos, no qual o sistema apresenta uma lista de estudantes, suas notas e situações acadêmicas.


1. Objetivos da atividade
Ao final, o aluno deverá saber:

Utilizar {% for %} para percorrer uma lista de alunos.
Utilizar {% if %}, {% elif %} e {% else %} para verificar condições.
Exibir informações dinâmicas no HTML.
Aplicar CSS para melhorar a apresentação da página.
Entendendo os comandos utilizados
Comando	Finalidade
{% if alunos %}	Verifica se existem alunos
{% else %}	Executa quando não existem alunos
{% elif %}	Verifica outra condição
{% for aluno in alunos %}	Percorre a lista de alunos
{{ aluno.nome }}	Exibe o nome do aluno
{{ aluno.nota }}	Exibe a nota do aluno

Dados:

from django.shortcuts import render



def painel(request):

    alunos = [

        {'nome': 'João', 'nota': 8.5},

        {'nome': 'Maria', 'nota': 9.5},

        {'nome': 'Pedro', 'nota': 4.0},

        {'nome': 'Ana', 'nota': 6.0},

        {'nome': 'Carlos', 'nota': 3.5},

    ]



    return render(request, 'painel.html', {

        'alunos': alunos

    })