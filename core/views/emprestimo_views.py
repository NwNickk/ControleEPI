from django.shortcuts import render, redirect, get_object_or_404
from core.models.emprestimo_model import Emprestimo
from core.forms.emprestimo_form import EmprestimoForm, UpdateEmprestimoForm
from django.contrib import messages

def criar_emprestimo(request):
    emprestimos = Emprestimo.objects.all()

    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Empréstimo cadastrado com sucesso!")
            return redirect('criar_emprestimo')
    else:
        form = EmprestimoForm()

    return render(request, 'core/pages/emprestimo.html', {
        'form': form,
        'emprestimos': emprestimos
    })

def editar_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)

    if request.method == 'POST':
        form = UpdateEmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('criar_emprestimo')
    else:
        form = UpdateEmprestimoForm(instance=emprestimo)

    return render(request, 'core/pages/editar_emprestimo.html', {
        'form': form,
        'emprestimo': emprestimo
    })

def deletar_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.delete()
    return redirect('criar_emprestimo')

def listar_emprestimos(request):
    search_query = request.GET.get('search', '')
    if search_query:
        emprestimos = Emprestimo.objects.filter(colaborador__nome__icontains=search_query)
    else:
        emprestimos = Emprestimo.objects.all()

    return render(request, 'core/pages/emprestimo.html', {
        'emprestimos': emprestimos,
        'search_query': search_query
    })