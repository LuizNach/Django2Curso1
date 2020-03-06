from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

     receitas = {
          1: "Lasanha",
          2: "Sorvete",
          3: "Bolo de Cenoura",
          4: "Bolo Chocolate"
     }
     
     dados = {
          "nome_das_receitas" :  receitas,
     }

     return render(request, 'index.html', context=dados)

def receita(request):
     return render(request, 'receita.html')