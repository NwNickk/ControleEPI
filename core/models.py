from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    status = models.BooleanField(default=True) 
    cargo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
