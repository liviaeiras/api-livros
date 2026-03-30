from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Livro


def listar_livros(request):
    livros = list(Livro.objects.values())
    return JsonResponse(livros, safe=False)


def livros_disponiveis(request):
    livros = list(Livro.objects.filter(status='DISPONIVEL').values())
    return JsonResponse(livros, safe=False)