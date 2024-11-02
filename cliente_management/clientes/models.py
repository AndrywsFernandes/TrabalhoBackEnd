from django.db import models

from django.db import models
from django.db import models
from django.db import models
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    data_de_nascimento = models.DateField(null=True, blank=True) 
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
  
    def __str__(self):
        return self.nome
