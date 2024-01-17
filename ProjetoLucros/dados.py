import tkinter as tk
from tkinter import ttk

def criar_formulario(root, enviar_dados):
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
        entry_ano, entry_meses, nomes_meses))
    btn_enviar.grid(row=len(entry_meses) + 2, column=0, columnspan=2, pady=10)

    label_status = tk.Label(root, text="", fg="red")
    label_status.grid(row=len(entry_meses) + 3, column=0, columnspan=2, pady=5)
