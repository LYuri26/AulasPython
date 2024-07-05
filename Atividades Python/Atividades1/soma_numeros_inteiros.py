# soma_numeros_inteiros.py

# Solicita ao usuário números inteiros até que ele digite 'fim'
numeros = []
while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    numeros.append(int(entrada))

# Calcula a soma dos números fornecidos
soma = sum(numeros)

# Exibe a soma
print(f"A soma dos números fornecidos é: {soma}")
