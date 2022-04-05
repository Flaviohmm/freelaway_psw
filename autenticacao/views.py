from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def cadastro(request):
    return HttpResponse('Cadastro')


def logar(request):
    return HttpResponse('Logar')