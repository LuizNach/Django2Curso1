from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Receita


# Create your views here.
def index(request):

     """
          view function are used on the urls.py
          we can import models and database data by getting all objects
          from data base using ModelName.objects.all()
     """

     receitas = Receita.objects.all()

     dados = {
          "receitas": receitas,
     }

     return render(request, 'index.html', context=dados)

def receita(request, receita_id):
     receita_object = get_object_or_404(Receita, pk=receita_id)
     receita_a_exibir = {
          'receita': receita_object
     }
     return render(request, 'receita.html', context=receita_a_exibir)