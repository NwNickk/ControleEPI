from django import forms
from core.models.emprestimo_model import Emprestimo
from django.utils import timezone

class EmprestimoForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('fornecido', 'Fornecido'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'equipamento', 'quantidade', 'data_prevista_devolucao', 'condicao_equipamento', 'status']
        widgets = {
            'colaborador': forms.Select(attrs={'class': 'form-control'}),
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade aqui'}),
            'data_prevista_devolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'condicao_equipamento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a condição do equipamento aqui'}),
        }

    #verifica se a data prevista para devolução é posterior à data e hora atuais
    def clean_data_prevista_devolucao(self):
        data_prevista_devolucao = self.cleaned_data.get('data_prevista_devolucao')
        data_emprestimo = self.instance.data_emprestimo or timezone.now().date()

        if data_prevista_devolucao and data_prevista_devolucao < data_emprestimo:
            raise forms.ValidationError(
                "A data prevista para devolução não pode ser anterior à data de empréstimo."
            )   
        return data_prevista_devolucao
        
    #valida se a quantidade é maior que zero
    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade

class UpdateEmprestimoForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('fornecido', 'Fornecido'),
        ('devolvido', 'Devolvido'),
        ('danificado', 'Danificado'),
        ('perdido', 'Perdido'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Emprestimo
        fields = ['quantidade', 'data_prevista_devolucao', 'condicao_equipamento', 'status', 'data_devolucao', 'observacao']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade aqui'}),
            'data_prevista_devolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_devolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'condicao_equipamento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a condição do equipamento aqui'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite uma observação aqui', 'rows': 3}),
        }

    #verifica se a data prevista para devolução é posterior à data e hora atuais
    def clean_data_prevista_devolucao(self):
        data_prevista_devolucao = self.cleaned_data.get('data_prevista_devolucao')
        if data_prevista_devolucao and data_prevista_devolucao < self.instance.data_emprestimo:
            raise forms.ValidationError("A data prevista para devolução não pode ser anterior à data de empréstimo.")
        return data_prevista_devolucao
        
    #valida se a quantidade é maior que zero
    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade
    
    # #valida se a data de devolução é maior que a data de empréstimo
    # def clean_data_devolucao(self):
    #     data_devolucao = self.cleaned_data.get('data_devolucao')
    #     if data_devolucao and data_devolucao < self.instance.data_emprestimo:
    #         raise forms.ValidationError("A data de devolução não pode ser anterior à data de empréstimo.")
    #     return data_devolucao
    
    #valida se o equipamento está disponível
    # def clean(self):
        # cleaned_data = super().clean()
        # equipamento = cleaned_data.get('equipamento')
        # quantidade = cleaned_data.get('quantidade')
# 
        # if equipamento and quantidade:
            # total_emprestado = Emprestimo.objects.filter(equipamento=equipamento).exclude(id=self.instance.id).aggregate(models.Sum('quantidade'))['quantidade__sum'] or 0
            # if total_emprestado + quantidade > equipamento.quantidade:
                # raise forms.ValidationError(f"Quantidade indisponível. Disponível: {equipamento.quantidade - total_emprestado}")
        # return cleaned_data

    # #se a data de devolução for preenchida, o status muda para True 
    # def save(self, commit=True):
    #     emprestimo = super().save(commit=False)
    #     if emprestimo.data_devolucao:
    #         emprestimo.status = True
    #     if commit:
    #         emprestimo.save()
    #     return emprestimo
    