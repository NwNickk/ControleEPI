from django import forms
from core.models.colaborador_model import Colaborador

class ColaboradorForm(forms.ModelForm):
    STATUS_CHOICES = [
        (True, 'Ativo'),
        (False, 'Inativo'),
    ] 

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Colaborador
        fields = ['nome', 'email', 'telefone', 'status', 'cargo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome aqui'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o email aqui'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone aqui'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o cargo aqui'}),
        }

    def clean_status(self):
        return self.cleaned_data['status'] == 'True'
