from django.urls import path
from . import views

urlpatterns = [
    path('criar_colaborador/', views.criar_colaborador, name='criar_colaborador'),
    path('deletar_colaborador/<int:id>', views.deletar_colaborador, name='deletar_colaborador'),
    path('editar_colaborador/<int:id>', views.editar_colaborador, name='editar_colaborador'),
] 