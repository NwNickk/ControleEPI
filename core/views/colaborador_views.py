from django.shortcuts import render, redirect
from core.models.colaborador_model import Colaborador

def home(request):
    return render(request, 'core/pages/home.html')

def criar_colaborador(request):
    if request.method == 'GET':
        colaboradores = Colaborador.objects.all()
        return render(request, 'core/pages/colaborador.html', {'colaboradores': colaboradores})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        status = request.POST.get('status') == '1'
        cargo = request.POST.get('cargo')

        colaborador = Colaborador(
            nome=nome,
            email=email,
            telefone=telefone,
            status=status,
            cargo=cargo
        )  

        colaborador.save() 

        return redirect('criar_colaborador')
    
def editar_colaborador(request, id):
    colaborador = Colaborador.objects.get(id=id)

    if request.method == 'GET':
        return render(request, 'core/pages/editar_colaborador.html', {'colaborador': colaborador})
    elif request.method == 'POST':
        colaborador.nome = request.POST.get('nome')
        colaborador.email = request.POST.get('email')
        colaborador.telefone = request.POST.get('telefone')
        colaborador.status = request.POST.get('status') == '1'
        colaborador.cargo = request.POST.get('cargo')

        colaborador.save() 

        return redirect('criar_colaborador')
    
def deletar_colaborador(request, id):
    colaborador = Colaborador.objects.get(id=id)
    colaborador.delete()
    return redirect('criar_colaborador')