from django import forms
from core.models.emprestimo_model import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'equipamento', 'quantidade']
        widgets = {
            'colaborador': forms.Select(attrs={'class': 'form-control'}),
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade aqui'}),
        }

class UpdateEmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['quantidade', 'data_devolucao']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade aqui'}),
            'data_devolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    #valida se a quantidade é maior que zero
    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade
    
    #valida se a data de devolução é maior que a data de empréstimo
    def clean_data_devolucao(self):
        data_devolucao = self.cleaned_data.get('data_devolucao')
        if data_devolucao and data_devolucao < self.instance.data_emprestimo:
            raise forms.ValidationError("A data de devolução não pode ser anterior à data de empréstimo.")
        return data_devolucao
    
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

    #se a data de devolução for preenchida, o status muda para True 
    def save(self, commit=True):
        emprestimo = super().save(commit=False)
        if emprestimo.data_devolucao:
            emprestimo.status = True
        if commit:
            emprestimo.save()
        return emprestimo
    