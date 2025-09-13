from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    validade = models.DateField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome