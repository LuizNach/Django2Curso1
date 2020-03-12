from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="nome-index"),
    path('receita/<int:receita_id>', views.receita, name="nome-receita"),
]