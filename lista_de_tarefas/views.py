from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import TarefaForm
# Create your views here.

def tarefas_home(request):
    contexto = {
        'nome':'Alex'
    }
    return render(request, 'lista_de_tarefas/home.html', contexto)

def tarefas_adicionar(request:HttpRequest):
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_de_tarefas:home')
    contexto = {
        "form" : TarefaForm
    }
    return render(request, 'lista_de_tarefas/adicionar.html', contexto)
