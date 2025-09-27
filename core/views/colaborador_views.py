from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required
from core.models.colaborador_model import Colaborador
from core.forms.colaborador_form import ColaboradorForm
from django.contrib import messages

#@login_required
def home(request):
    return render(request, 'core/pages/home.html')

# def criar_colaborador(request):
#     if request.method == 'GET':
#         colaboradores = Colaborador.objects.all()
#         return render(request, 'core/pages/colaborador.html', {'colaboradores': colaboradores})
#     elif request.method == 'POST':
#         nome = request.POST.get('nome')
#         email = request.POST.get('email')
#         telefone = request.POST.get('telefone')
#         status = request.POST.get('status') == '1'
#         cargo = request.POST.get('cargo')

#         colaborador = Colaborador(
#             nome=nome,
#             email=email,
#             telefone=telefone,
#             status=status,
#             cargo=cargo
#         )  

#         colaborador.save() 

#         return redirect('criar_colaborador')

def criar_colaborador(request):
    colaboradores = Colaborador.objects.all()

    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Colaborador cadastrado com sucesso!")
            return redirect('criar_colaborador')
    else:
        form = ColaboradorForm()

    return render(request, 'core/pages/colaborador.html', {
        'form': form,
        'colaboradores': colaboradores
    })


def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)

    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('criar_colaborador')
    else:
        form = ColaboradorForm(instance=colaborador)

    return render(request, 'core/pages/editar_colaborador.html', {
        'form': form,
        'colaborador': colaborador
    })
    
def deletar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    colaborador.delete()
    return redirect('criar_colaborador')

def listar_colaboradores(request):
    search_query = request.GET.get('search', '')
    if search_query:
        colaboradores = Colaborador.objects.filter(nome__icontains=search_query)
    else:
        colaboradores = Colaborador.objects.all()

    return render(request, 'core/pages/colaborador.html', {
        'colaboradores': colaboradores,
        'search_query': search_query
    })