from django.db import models
import datetime

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class TokenSenha(models.Model):
    user = models.IntegerField()
    token = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    expirado_em = models.DateTimeField()

    @property
    def is_expired(self):
        return self.expirado_em.date() > datetime.datetime.now().date()