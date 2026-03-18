from django.urls import path
from . import views

app_name="lista_de_tarefas"

urlpatterns = [
    path("", views.tarefas_home, name='home'),
    path("adicionar/", views.tarefas_adicionar, name="adicionar"),
    path("remover/<int:id>", views.tarefas_remover, name="remover")
]
