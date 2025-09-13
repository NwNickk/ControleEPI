from django.shortcuts import render, redirect
from core.models.equipamento_model import Equipamento

def criar_equipamento(request):
    if request.method == 'GET':
        equipamentos = Equipamento.objects.all()
        return render(request, 'core/pages/equipamento.html', {'equipamentos': equipamentos})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        codigo = request.POST.get('codigo')
        validade = request.POST.get('validade')
        estoque = request.POST.get('estoque')

        equipamento = Equipamento(
            nome=nome,
            tipo=tipo,
            codigo=codigo,
            validade=validade,
            estoque=estoque
        )  

        equipamento.save() 

        return redirect('criar_equipamento')
    
def editar_equipamento(request, id):
    equipamento = Equipamento.objects.get(id=id)

    if request.method == 'GET':
        return render(request, 'core/pages/editar_equipamento.html', {'equipamento': equipamento})
    elif request.method == 'POST':
        equipamento.nome = request.POST.get('nome')
        equipamento.tipo = request.POST.get('tipo')
        equipamento.codigo = request.POST.get('codigo')
        equipamento.validade = request.POST.get('validade')
        equipamento.estoque = request.POST.get('estoque')

        equipamento.save() 

        return redirect('criar_equipamento')

def deletar_equipamento(request, id):
    equipamento = Equipamento.objects.get(id=id)
    equipamento.delete()
    return redirect('criar_equipamento')