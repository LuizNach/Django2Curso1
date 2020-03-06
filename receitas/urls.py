from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="nome-index"),
    path('receita/', views.receita, name="nome-receita"),
]