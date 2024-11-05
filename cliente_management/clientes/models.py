from django.db import models

from django.db import models

class Cliente(models.Model):
    MASCULINO = 'M'
    FEMININO = 'F'
    OUTRO = 'O'
    
    SEXO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino'),
        (OUTRO, 'Outro'),
    ]
    
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    data_de_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.nome

