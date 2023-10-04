from django.db import models


class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade_disponivel = models.IntegerField()


def __str__(self):
    return self.nome
