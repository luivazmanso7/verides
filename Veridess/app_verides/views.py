from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def contribuir(request):
    return render(request,'contribuir.html')

def inscricao(request):
    return render(request,'inscricao.html')

def doacoes(request):
    return render(request,'doacoes.html')

def catalogo(request):
    return render(request,'catalogo.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def sobrenos(request):
    return render(request, 'sobrenos.html')
