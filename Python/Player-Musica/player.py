import pygame
import tkinter as tk
from tkinter import filedialog

# Inicializa o Pygame.
pygame.init()

# Cria uma janela.
window = tk.Tk()

# Define o título da janela.
window.title("Player de Música")

# Cria uma função para carregar uma música.
def load_music():

    # Exibe uma caixa de diálogo para o usuário selecionar uma música.
    file_path = filedialog.askopenfilename(title="Selecione uma música", filetypes=[("Arquivos de áudio", "*.mp3")])

    # Carrega a música selecionada na biblioteca Pygame.
    pygame.mixer.music.load(file_path)

# Cria uma função para tocar a música atual.
def play_music():

    # Toca a música atual.
    pygame.mixer.music.play()

# Cria uma função para avançar para a próxima música.
def forward():

    # Avança para a próxima música na lista de reprodução.
    pygame.mixer.music.set_pos(pygame.mixer.music.get_pos() + 10)

# Cria uma função para voltar para a música anterior.
def backward():

    # Volta para a música anterior na lista de reprodução.
    pygame.mixer.music.set_pos(pygame.mixer.music.get_pos() - 10)

# Cria uma função para pausar a música atual.
def pause():

    # Pausa a música atual.
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# Cria uma função para interromper a música atual.
def stop():

    # Interrompe a música atual.
    pygame.mixer.music.stop()

# Cria uma função para repetir a música atual.
def repeat():

    # Faz com que a música atual seja reproduzida repetidamente.
    pygame.mixer.music.set_loop(-1)

# Cria um botão para carregar uma música.
load_button = tk.Button(window, text="Carregar", command=load_music)

# Adiciona o botão "Carregar" à janela.
load_button.pack(side="left")

# Cria um botão para tocar a música atual.
play_button = tk.Button(window, text="Tocar", command=play_music)

# Adiciona o botão "Tocar" à janela.
play_button.pack(side="left")

# Cria um botão para avançar para a próxima música.
forward_button = tk.Button(window, text="Avançar", command=forward)

# Adiciona o botão "Avançar" à janela.
forward_button.pack(side="left")

# Cria um botão para voltar para a música anterior.
backward_button = tk.Button(window, text="Voltar", command=backward)

# Adiciona o botão "Voltar" à janela.
backward_button.pack(side="left")

# Cria um botão para pausar a música atual.
pause_button = tk.Button(window, text="Pausar", command=pause)

# Adiciona o botão "Pausar" à janela.
pause_button.pack(side="left")

# Cria um botão para interromper a música atual.
stop_button = tk.Button(window, text="Parar", command=stop)

# Adiciona o botão "Parar" à janela.
stop_button.pack(side="left")

# Cria um botão para repetir a música atual.
repeat_button = tk.Button(window, text="Repetir", command=repeat)

# Adiciona o botão "Repetir" à janela.
repeat_button.pack(side="left")

# Define o formato dos botões.
for button in (load_button, play_button, forward_button, backward_button, pause_button, stop_button, repeat_button):
    button.config(
        relief="raised",
        background="blue",
        foreground="white",
    )
# Define o formato dos botões.
for button in (load_button, play_button, forward_button, backward_button, pause_button, stop_button, repeat_button):
    button.config(
        relief="raised",
        background="blue",
        foreground="white",
    )

# Inicia o loop principal do Pygame.
window.mainloop()
