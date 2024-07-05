# calculadora_idade.py
from datetime import date


def calcular_idade(ano_nascimento, mes_nascimento, dia_nascimento):
    data_atual = date.today()
    data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
    idade = data_atual.year - data_nascimento.year - \
        ((data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento))
    meses = data_atual.month - mes_nascimento
    if meses < 0:
        idade -= 1
        meses += 12
    dias = data_atual.day - dia_nascimento
    if dias < 0:
        meses -= 1
        dias += 30
    return idade, meses, dias


# Solicita a data de nascimento ao usuário
ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))

# Calcula a idade
idade, meses, dias = calcular_idade(ano, mes, dia)
print(f"Idade: {idade} anos, {meses} meses e {dias} dias.")
