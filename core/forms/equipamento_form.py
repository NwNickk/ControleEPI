from django import forms
from core.models.equipamento_model import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'tipo', 'codigo', 'validade', 'estoque']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome aqui'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o tipo aqui'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o código aqui'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade em estoque'}),
        }
