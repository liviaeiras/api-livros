from django.db import models

# Create your models here.
from django.db import models

class Livro(models.Model):

    STATUS = [
        ('DISPONIVEL', 'Disponível'),
        ('INDISPONIVEL', 'Indisponível'),
    ]

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return self.titulo