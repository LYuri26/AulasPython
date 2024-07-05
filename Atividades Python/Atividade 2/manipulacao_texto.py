# manipulacao_texto.py

# Solicita ao usuário uma frase
frase = input("Digite uma frase: ")

# Conta o número total de caracteres na frase (sem espaços)
num_caracteres = len(frase.replace(' ', ''))

# Converte todas as palavras para maiúsculas
frase_maiuscula = frase.upper()

# Substitui todas as letras 'a' por '*'
frase_substituida = frase.replace('a', '*')

# Exibe os resultados
print(f"Número total de caracteres na frase (sem espaços): {num_caracteres}")
print(f"Frase em maiúsculas: {frase_maiuscula}")
print(f"Frase com 'a' substituído por '*': {frase_substituida}")
