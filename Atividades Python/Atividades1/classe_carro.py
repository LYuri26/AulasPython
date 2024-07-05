# classe_carro.py

# Define a classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")

# Cria uma instância da classe Carro
carro1 = Carro("Toyota", "Corolla", 2020)

# Exibe os valores dos atributos do carro
carro1.exibir_detalhes()
