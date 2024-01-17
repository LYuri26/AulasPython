import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import locale

# Configurar a localização para o formato de moeda brasileira
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


def formatar_moeda(valor):
    return locale.currency(valor, grouping=True)


def gerar_graficos(ano, nomes_meses, lucros):
    fig, ax = plt.subplots()

    # Configurar gráfico
    ax.bar(nomes_meses, lucros, color=np.where(
        np.array(lucros) >= 0, 'green', 'red'))

    # Adicionar rótulos formatados como moeda
    ax.set_yticklabels([formatar_moeda(y) for y in ax.get_yticks()])

    # Adicionar rótulos personalizados para os meses na parte inferior do gráfico
    # Ajuste para rotacionar os rótulos e alinhá-los à direita
    ax.set_xticklabels(nomes_meses, rotation=45, ha="right")
    ax.set_xlabel("Meses")
    ax.set_ylabel("Lucro (R$)")

    # Adicionar texto "Lucro" acima de cada barra
    for i, valor in enumerate(lucros):
        ax.text(i, max(lucros) * 1.1, formatar_moeda(valor),
                ha="center", va="bottom")

    # Configurar título
    ax.set_title(f"Resultados DS {ano}")

    # Adicionar legenda
    ax.legend(["Lucros"])

    # Mostrar gráfico
    plt.show()


def criar_formulario(root):
    # Adicionar widgets
    label_ano = tk.Label(root, text="Ano:")
    label_ano.grid(row=0, column=0, padx=10, pady=5, sticky="e")

    entry_ano = ttk.Entry(root)
    entry_ano.grid(row=0, column=1, padx=10, pady=5)

    label_meses = tk.Label(root, text="Lucros Mensais:")
    label_meses.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    entry_meses = []

    nomes_meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    for i, mes in enumerate(nomes_meses):
        label_mes = tk.Label(root, text=f"{mes}:")
        label_mes.grid(row=i + 2, column=0, padx=10, pady=5, sticky="e")

        entry_mes = ttk.Entry(root)
        entry_mes.grid(row=i + 2, column=1, padx=10, pady=5)
        entry_meses.append(entry_mes)

    btn_enviar = tk.Button(root, text="Enviar", command=lambda: enviar_dados(
        root, entry_ano, entry_meses, nomes_meses))
    btn_enviar.grid(row=len(entry_meses) + 2, column=0, columnspan=2, pady=10)

    label_status = tk.Label(root, text="", fg="red")
    label_status.grid(row=len(entry_meses) + 3, column=0, columnspan=2, pady=5)


def enviar_dados(root, entry_ano, entry_meses, nomes_meses):
    ano = entry_ano.get()
    valores_meses = [entry.get() for entry in entry_meses]

    # Adicionar "R$" e converter para float
    lucros = [float(valor.replace(",", "."))
              if valor else 0 for valor in valores_meses]

    label_status = root.nametowidget(root.winfo_children()[-1])

    # Verificar se todos os campos foram preenchidos
    if "" in valores_meses or ano == "":
        label_status.config(text="Preencha todos os campos!", fg="red")
    else:
        label_status.config(text="")
        gerar_graficos(ano, nomes_meses, lucros)


# Criar a janela principal
root = tk.Tk()
root.title("Aplicação de Lucros")

# Chamar a função para criar o formulário
criar_formulario(root)

# Iniciar o loop da janela
root.mainloop()
