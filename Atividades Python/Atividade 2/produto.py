# produto.py

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}"

    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco}, {self.quantidade})"


# Exemplo de uso
produto1 = Produto("Notebook", 3500.99, 5)
print(str(produto1))
print(repr(produto1))
