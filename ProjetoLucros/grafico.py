import matplotlib.pyplot as plt
import numpy as np
import locale

def formatar_moeda(valor):
    return locale.currency(valor, grouping=True)

def gerar_graficos(ano, nomes_meses, lucros):
    fig, ax = plt.subplots()

    ax.bar(nomes_meses, lucros, color=np.where(
        np.array(lucros) >= 0, 'green', 'red'))

    ax.set_yticklabels([formatar_moeda(y) for y in ax.get_yticks()])
    ax.set_xticklabels(nomes_meses, rotation=45, ha="right")
    ax.set_xlabel("Meses")
    ax.set_ylabel("Lucro (R$)")

    for i, valor in enumerate(lucros):
        ax.text(i, max(lucros) * 1.1, formatar_moeda(valor),
                ha="center", va="bottom")

    ax.set_title(f"Resultados DS {ano}")
    ax.legend(["Lucros"])

    plt.show()
