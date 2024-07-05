# classe_pessoa.py

# Define a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Cria uma instância da classe Pessoa
pessoa1 = Pessoa("Maria", 30)

# Chama o método para apresentar a pessoa
pessoa1.apresentar()
