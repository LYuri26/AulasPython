# maior_menor_elemento.py

def maior_menor_elemento(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor


# Exemplo de uso
lista_numeros = [15, 7, 25, 12, 18]
maior, menor = maior_menor_elemento(lista_numeros)
print(f"Maior elemento da lista: {maior}")
print(f"Menor elemento da lista: {menor}")
