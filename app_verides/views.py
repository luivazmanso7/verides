from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def contribuir(request):
    return render(request,'contribuir.html')

def inscricao(request):
    return render(request,'inscricao.html')


