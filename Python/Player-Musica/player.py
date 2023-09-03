import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import Listbox, Scrollbar, ttk

# Inicializa o Pygame.
pygame.init()

# Cria uma janela.
janela = tk.Tk()
janela.title("Player de Música")

# Cria uma lista para armazenar as músicas.
lista_de_reproducao = []

# Função para carregar uma música.
def carregar_musica():
    caminho_do_arquivo = filedialog.askopenfilename(title="Selecione uma música", filetypes=[("Arquivos de áudio", "*.mp3")])
    if caminho_do_arquivo:
        pygame.mixer.music.load(caminho_do_arquivo)
        lista_de_reproducao.append(caminho_do_arquivo)
        lista_musicas.insert(tk.END, caminho_do_arquivo)

# Função para tocar a música selecionada na lista.
def tocar_musica():
    indice_selecionado = lista_musicas.curselection()
    if indice_selecionado:
        musica_selecionada = lista_de_reproducao[indice_selecionado[0]]
        pygame.mixer.music.load(musica_selecionada)
        pygame.mixer.music.play()

# Função para interromper a música atual.
def parar_musica():
    pygame.mixer.music.stop()

# Função para avançar para a próxima música.
def proxima_musica():
    indice_atual = lista_musicas.curselection()
    if indice_atual:
        indice_proxima = indice_atual[0] + 1
        if indice_proxima < len(lista_de_reproducao):
            musica_selecionada = lista_de_reproducao[indice_proxima]
            pygame.mixer.music.load(musica_selecionada)
            pygame.mixer.music.play()
            lista_musicas.select_clear(0, tk.END)
            lista_musicas.selection_set(indice_proxima)
            lista_musicas.activate(indice_proxima)

# Função para voltar para a música anterior.
def musica_anterior():
    indice_atual = lista_musicas.curselection()
    if indice_atual:
        indice_anterior = indice_atual[0] - 1
        if indice_anterior >= 0:
            musica_selecionada = lista_de_reproducao[indice_anterior]
            pygame.mixer.music.load(musica_selecionada)
            pygame.mixer.music.play()
            lista_musicas.select_clear(0, tk.END)
            lista_musicas.selection_set(indice_anterior)
            lista_musicas.activate(indice_anterior)

# Cria uma lista de reprodução (Listbox) para mostrar as músicas.
lista_musicas = Listbox(janela, selectmode=tk.SINGLE, width=50)
lista_musicas.pack(padx=10, pady=10, side=tk.LEFT)

# Adiciona uma barra de rolagem à lista de reprodução.
scrollbar = Scrollbar(janela)
scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
lista_musicas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_musicas.yview)

# Cria botões estilizados para carregar, tocar, parar, avançar e voltar músicas.
botao_carregar = ttk.Button(janela, text="Carregar Música", command=carregar_musica)
botao_tocar = ttk.Button(janela, text="Tocar Música", command=tocar_musica)
botao_parar = ttk.Button(janela, text="Parar Música", command=parar_musica)
botao_avancar = ttk.Button(janela, text="Avançar", command=proxima_musica)
botao_voltar = ttk.Button(janela, text="Voltar", command=musica_anterior)

botao_carregar.pack(padx=10, pady=5)
botao_tocar.pack(padx=10, pady=5)
botao_parar.pack(padx=10, pady=5)
botao_avancar.pack(padx=10, pady=5)
botao_voltar.pack(padx=10, pady=5)

# Estiliza os botões.
estilo = ttk.Style()
estilo.configure("TButton", foreground="blue", background="white", font=("Helvetica", 12))
estilo.map("TButton",
          foreground=[("pressed", "red"), ("active", "blue")],
          background=[("pressed", "!disabled", "black"), ("active", "white")]
          )

# Inicia o loop principal do Pygame.
janela.mainloop()
