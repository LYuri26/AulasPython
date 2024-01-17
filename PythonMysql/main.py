import tkinter as tk
from tkinter import messagebox
import mysql.connector
from create_database import create_database_and_table
from insert_data import insert_data_into_table


def submit_form():
    exercise_name = entry_exercise_name.get()
    repetitions = entry_repetitions.get()
    sets = entry_sets.get()
    muscle_activation = entry_muscle_activation.get()
    load_speed = entry_load_speed.get()
    rest = entry_rest.get()
    notes = entry_notes.get()
    substitute_exercise = entry_substitute_exercise.get()

    data = (exercise_name, repetitions, sets, muscle_activation,
            load_speed, rest, notes, substitute_exercise)

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

# Botão de envio do formulário
submit_button = tk.Button(root, text="Enviar Dados", command=submit_form)
submit_button.pack(pady=10)

# Criar o banco de dados e a tabela
create_database_and_table()

# Iniciar o loop principal
root.mainloop()
