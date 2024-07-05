# diferenca_datas.py
from datetime import datetime


def diferenca_entre_datas(data1, data2):
    diff = abs(data1 - data2)
    return diff.days


# Solicita as datas ao usuário
data_str1 = input("Digite a primeira data (formato dd/mm/aaaa): ")
data_str2 = input("Digite a segunda data (formato dd/mm/aaaa): ")

# Converte as strings para objetos datetime
data1 = datetime.strptime(data_str1, "%d/%m/%Y")
data2 = datetime.strptime(data_str2, "%d/%m/%Y")

# Calcula e exibe a diferença em dias
diferenca = diferenca_entre_datas(data1, data2)
print(f"Diferença entre as datas: {diferenca} dias.")
