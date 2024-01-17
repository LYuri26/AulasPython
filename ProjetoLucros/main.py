import tkinter as tk
from tkinter import ttk
from dados import criar_formulario
from grafico import gerar_graficos
import locale

# Configurar a localização para o formato de moeda brasileira
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


def enviar_dados(entry_ano, entry_meses, nomes_meses):
    ano = entry_ano.get()
    valores_meses = [entry.get() for entry in entry_meses]

    lucros = [float(valor.replace(",", "."))
              if valor else 0 for valor in valores_meses]

    label_status = root.nametowidget(root.winfo_children()[-1])

    if "" in valores_meses or ano == "":
        label_status.config(text="Preencha todos os campos!", fg="red")
    else:
        label_status.config(text="")
        gerar_graficos(ano, nomes_meses, lucros)


# Criar a janela principal
root = tk.Tk()
root.title("Aplicação de Lucros")

# Chamar a função para criar o formulário
criar_formulario(root, enviar_dados)

# Iniciar o loop da janela
root.mainloop()
