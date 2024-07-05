# funcionario.py

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus_desempenho(self):
        raise NotImplementedError("Método não implementado.")


class Gerente(Funcionario):
    def calcular_bonus_desempenho(self):
        return self.salario * 0.15


class Operario(Funcionario):
    def calcular_bonus_desempenho(self):
        return self.salario * 0.1


# Exemplo de uso
gerente1 = Gerente("Ana", 5000, "Gerente de Projetos")
operario1 = Operario("Carlos", 3000, "Operário de Produção")

print(f"Bônus de desempenho do(a) {gerente1.nome}: R${
      gerente1.calcular_bonus_desempenho():.2f}")
print(f"Bônus de desempenho do(a) {operario1.nome}: R${
      operario1.calcular_bonus_desempenho():.2f}")
