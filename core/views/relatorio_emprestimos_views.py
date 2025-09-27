from django.shortcuts import render
from core.models.emprestimo_model import Emprestimo

def relatorio_emprestimos(request):
    emprestimos = Emprestimo.objects.all()

    equipamento = request.GET.get('equipamento', '').strip()
    colaborador = request.GET.get('colaborador', '').strip()
    status = request.GET.get('status', '').strip()

    # Filtro AND
    if equipamento:
        emprestimos = emprestimos.filter(equipamento__nome__icontains=equipamento)
    if colaborador:
        emprestimos = emprestimos.filter(colaborador__nome__icontains=colaborador)
    if status:
        emprestimos = emprestimos.filter(status=status)

    return render(request, 'core/pages/relatorio_emprestimos.html', {
        'emprestimos': emprestimos,
        'equipamento': equipamento,
        'colaborador': colaborador,
        'status': status,
    })

# def relatorio_estoque(request):
#     equipamentos = Equipamento.objects.all()
#     return render(request, 'core/pages/relatorio_estoque.html', {
#         'equipamentos': equipamentos
#     })
