from django.db import models
from core.models.colaborador_model import Colaborador
from core.models.equipamento_model import Equipamento

class Emprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_emprestimo = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)
    data_devolucao = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Empréstimo de {self.equipamento} para {self.colaborador}"
    
    def get_status_display(self):
        return "Devolvido" if self.status else "Emprestado"
