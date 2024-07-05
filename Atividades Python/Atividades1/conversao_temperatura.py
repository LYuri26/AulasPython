# conversao_temperatura.py

# Solicita a temperatura em graus Celsius ao usuário
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte a temperatura para Fahrenheit
fahrenheit = celsius * (9/5) + 32

# Exibe a temperatura convertida
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
