from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nome_cliente} - {self.produto.nome}'
