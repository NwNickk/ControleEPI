from django.urls import path
from .views import colaborador_views, equipamento_views

urlpatterns = [
    path('', colaborador_views.home, name='home'),
    path('criar_colaborador/', colaborador_views.criar_colaborador, name='criar_colaborador'),
    path('deletar_colaborador/<int:id>', colaborador_views.deletar_colaborador, name='deletar_colaborador'),
    path('editar_colaborador/<int:id>', colaborador_views.editar_colaborador, name='editar_colaborador'),
    path('criar_equipamento/', equipamento_views.criar_equipamento, name='criar_equipamento'),
    path('deletar_equipamento/<int:id>', equipamento_views.deletar_equipamento, name='deletar_equipamento'),
    path('editar_equipamento/<int:id>', equipamento_views.editar_equipamento, name='editar_equipamento'),
] 