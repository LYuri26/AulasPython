import tkinter as tk
from tkinter import messagebox
import mysql.connector
from create_database import create_database_and_table
from insert_data import insert_data_into_table


def validate_integer(input_text):
    try:
        int(input_text)
        return True
    except ValueError:
        return False


def update_descanso(event):
    # Atualizar o valor do campo descanso ao sair do campo
    descanso_value = entries[5].get().strip()
    if descanso_value and validate_integer(descanso_value):
        entries[5].delete(0, tk.END)
        entries[5].insert(0, f"{descanso_value} segundos")


def submit_form():
    # Obter valores dos campos do formulário
    nome_do_exercicio = entries[0].get()
    repeticoes = entries[1].get()
    series = entries[2].get()
    ativacao_muscular = entries[3].get()
    carga_velocidade = entries[4].get()
    descanso = entries[5].get()
    anotacoes = entries[6].get()
    exercicio_substituto = entries[7].get()

    # Ajustar valores antes de enviar para o banco de dados
    if not anotacoes:
        anotacoes = "Sem anotações."

    # Converter descanso para formato desejado
    descanso = descanso.strip()  # Remover espaços em branco extras
    if descanso and validate_integer(descanso):
        descanso = f"{descanso} segundos."
    elif not descanso:
        descanso = None  # Deixe como None se o campo estiver vazio
    else:
        messagebox.showerror(
            "Erro", "O campo de descanso deve ser um número inteiro.")
        return

    data = (nome_do_exercicio, repeticoes, series, ativacao_muscular,
            carga_velocidade, descanso, anotacoes, exercicio_substituto)

    # Verificar se todos os campos foram preenchidos
    if not all(data):
        messagebox.showerror("Erro", "Preencha todos os campos do formulário.")
        return

    try:
        insert_data_into_table(data)
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror(
            "Erro", f"Erro ao inserir dados no banco de dados:\n{err}")


# Criação da janela principal
root = tk.Tk()
root.title("Formulário de Academia")

# Labels e Entry widgets para cada campo
labels = ["Nome do Exercício", "Repetições", "Vezes de Repetições", "Ativação Muscular",
          "Carga/Velocidade", "Descanso", "Anotações do Aluno", "Exercício Substituto"]

entries = []
for label in labels:
    frame = tk.Frame(root)
    frame.pack(pady=5)
    lbl = tk.Label(frame, text=label)
    lbl.pack(side=tk.LEFT)
    entry = tk.Entry(frame, width=30)
    entry.pack(side=tk.RIGHT)
    entries.append(entry)

# Preenchimento automático para campo de anotações
entries[6].insert(0, "Sem anotações.")

# Adicionar validação para o campo de descanso
descanso_validation = root.register(validate_integer)
entries[5].config(validate="key", validatecommand=(descanso_validation, "%P"))
entries[5].bind("<FocusOut>", update_descanso)

# Botão de envio do formulário
submit_button = tk.Button(root, text="Enviar Dados", command=submit_form)
submit_button.pack(pady=10)

# Criar o banco de dados e a tabela
create_database_and_table()

# Iniciar o loop principal
root.mainloop()
