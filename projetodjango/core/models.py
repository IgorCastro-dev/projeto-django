import email
from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome',max_length=255)
    preco = models.DecimalField('Preço',decimal_places=2,max_digits=8)
    estoque = models.IntegerField('Estoque')
    def __str__(self):
        return self.nome