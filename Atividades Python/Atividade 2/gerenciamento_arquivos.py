# gerenciamento_arquivos.py
import os

# Diretório específico para listar os arquivos
diretorio = "caminho/do/diretorio"

# Lista todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Exibe o tamanho de cada arquivo em bytes
for arquivo in arquivos:
    caminho_completo = os.path.join(diretorio, arquivo)
    if os.path.isfile(caminho_completo):
        tamanho = os.path.getsize(caminho_completo)
        print(f"Arquivo: {arquivo}, Tamanho: {tamanho} bytes")
