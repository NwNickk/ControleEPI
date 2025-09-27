from django.urls import path
from .views import colaborador_views, equipamento_views, emprestimo_views, relatorio_emprestimos_views

urlpatterns = [
    path('', colaborador_views.home, name='home'),
    path('colaborador/', colaborador_views.criar_colaborador, name='criar_colaborador'),
    path('colaborador/<int:id>/deletar', colaborador_views.deletar_colaborador, name='deletar_colaborador'),
    path('colaborador/<int:id>/editar', colaborador_views.editar_colaborador, name='editar_colaborador'),
    path('colaborador/listar/', colaborador_views.listar_colaboradores, name='listar_colaboradores'),
    path('equipamentos/', equipamento_views.criar_equipamento, name='criar_equipamento'),
    path('equipamentos/<int:id>/editar/', equipamento_views.editar_equipamento, name='editar_equipamento'),
    path('equipamentos/<int:id>/deletar/', equipamento_views.deletar_equipamento, name='deletar_equipamento'),
    path('equipamentos/listar/', equipamento_views.listar_equipamentos, name='listar_equipamentos'),
    path('emprestimos/', emprestimo_views.criar_emprestimo, name='criar_emprestimo'),
    path('emprestimos/<int:id>/editar/', emprestimo_views.editar_emprestimo, name='editar_emprestimo'),
    path('emprestimos/<int:id>/deletar/', emprestimo_views.deletar_emprestimo, name='deletar_emprestimo'),
    path('emprestimos/listar/', emprestimo_views.listar_emprestimos, name='listar_emprestimos'),
    path('relatorio/emprestimos/', relatorio_emprestimos_views.relatorio_emprestimos, name='relatorio_emprestimos'),
]