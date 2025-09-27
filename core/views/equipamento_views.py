from django.shortcuts import render, redirect, get_object_or_404
from core.models.equipamento_model import Equipamento
from core.forms.equipamento_form import EquipamentoForm
from django.contrib import messages


def criar_equipamento(request):
    equipamentos = Equipamento.objects.all()

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipamento cadastrado com sucesso!")
            return redirect('criar_equipamento')
    else:
        form = EquipamentoForm()

    return render(request, 'core/pages/equipamento.html', {
        'form': form,
        'equipamentos': equipamentos
    })


def editar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)

    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('criar_equipamento')
    else:
        form = EquipamentoForm(instance=equipamento)

    return render(request, 'core/pages/editar_equipamento.html', {
        'form': form,
        'equipamento': equipamento
    })


def deletar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    equipamento.delete()
    return redirect('criar_equipamento')

def listar_equipamentos(request):
    search_query = request.GET.get('search', '')
    if search_query:
        equipamentos = Equipamento.objects.filter(nome__icontains=search_query)
    else:
        equipamentos = Equipamento.objects.all()

    return render(request, 'core/pages/equipamento.html', {
        'equipamentos': equipamentos,
        'search_query': search_query
    })