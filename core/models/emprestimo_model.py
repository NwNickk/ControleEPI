from django.db import models
from core.models.colaborador_model import Colaborador
from core.models.equipamento_model import Equipamento
from django.utils import timezone
from django.core.exceptions import ValidationError

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('fornecido', 'Fornecido'),
        ('devolvido', 'Devolvido'),
        ('danificado', 'Danificado'),
        ('perdido', 'Perdido'),
    ]

    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_prevista_devolucao = models.DateField(default=timezone.now)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(blank=True, null=True)
    condicao_equipamento = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='emprestado')
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Empréstimo de {self.equipamento} para {self.colaborador}"

    def save(self, *args, **kwargs):
        # Detecta se é criação ou atualização
        is_new = self.pk is None

        # Se for atualização, precisamos saber o status anterior e a quantidade anterior
        old_status = None
        old_quantidade = None
        if not is_new:
            old = Emprestimo.objects.get(pk=self.pk)
            old_status = old.status
            old_quantidade = old.quantidade

        # Caso novo empréstimo: tirar do estoque
        if is_new:
            if self.equipamento.estoque < self.quantidade:   
                raise ValidationError("Quantidade solicitada maior do que o disponível em estoque!")
            self.equipamento.estoque -= self.quantidade       
            self.equipamento.save()

        else:
            # Atualização do empréstimo
            # Se quantidade mudou, ajusta diferença
            if self.quantidade != old_quantidade:
                diferenca = self.quantidade - old_quantidade
                if diferenca > 0:  # aumentou quantidade emprestada
                    if self.equipamento.estoque < diferenca:  
                        raise ValidationError("Quantidade adicional solicitada maior que o estoque disponível!")
                    self.equipamento.estoque -= diferenca     
                elif diferenca < 0:  # diminuiu quantidade emprestada
                    self.equipamento.estoque += abs(diferenca) 
                self.equipamento.save()

            # Se status mudou:
            if self.status != old_status:
                # Se estava emprestado e passou para devolvido → devolve para o estoque
                if old_status in ['emprestado', 'fornecido'] and self.status == 'devolvido':
                    self.equipamento.estoque += self.quantidade 
                    self.equipamento.save()

                # Se estava emprestado e passou para danificado ou perdido → não devolve
                elif old_status in ['emprestado', 'fornecido'] and self.status in ['danificado', 'perdido']:
                    pass  # não faz nada

                # Se estava devolvido e voltou a emprestado → tira novamente do estoque
                # elif old_status == 'devolvido' and self.status in ['emprestado', 'fornecido']:
                #     if self.equipamento.estoque < self.quantidade:  
                #         raise ValueError("Estoque insuficiente para re-emprestar o equipamento.")
                #     self.equipamento.estoque -= self.quantidade      
                #     self.equipamento.save()

        super().save(*args, **kwargs)

    