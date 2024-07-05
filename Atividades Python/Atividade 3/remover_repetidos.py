# remover_repetidos.py

def remover_elementos_repetidos(lista):
    lista_sem_repeticao = list(set(lista))
    return lista_sem_repeticao


# Exemplo de uso
lista_numeros = [10, 20, 30, 10, 20, 40, 50, 30]
lista_sem_repeticao = remover_elementos_repetidos(lista_numeros)
print(f"Lista sem elementos repetidos: {lista_sem_repeticao}")
