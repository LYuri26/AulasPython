import pygame
import tkinter as tk
from tkinter import filedialog

# Inicializa o Pygame
pygame.init()

# Cria a janela principal do Tkinter
window = tk.Tk()
window.title("Player de Música")

# Função para carregar música
def load_music():
    file_path = filedialog.askopenfilename(title="Selecione uma música", filetypes=[("Arquivos de áudio", "*.mp3")])
    if file_path:
        pygame.mixer.music.load(file_path)
        print(f"Música carregada: {file_path}")

# Função para reproduzir música
def play_music():
    if pygame.mixer.music.get_busy():
        print("A música já está tocando.")
    else:
        pygame.mixer.music.play()
        print("Reproduzindo música...")

# Função para pausar/despausar música
def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        print("Música pausada.")
    else:
        pygame.mixer.music.unpause()
        print("Música despausada.")

# Função para parar música
def stop_music():
    pygame.mixer.music.stop()
    print("Música parada.")

# Função para repetir música
def repeat_music():
    pygame.mixer.music.play(-1)  # -1 faz a música repetir indefinidamente
    print("Música configurada para repetir.")

# Botão "Carregar"
load_button = tk.Button(window, text="Carregar", command=load_music)
load_button.pack(side="left", padx=10, pady=10)

# Botão "Tocar"
play_button = tk.Button(window, text="Tocar", command=play_music)
play_button.pack(side="left", padx=10, pady=10)

# Botão "Pausar"
pause_button = tk.Button(window, text="Pausar", command=pause_music)
pause_button.pack(side="left", padx=10, pady=10)

# Botão "Parar"
stop_button = tk.Button(window, text="Parar", command=stop_music)
stop_button.pack(side="left", padx=10, pady=10)

# Botão "Repetir"
repeat_button = tk.Button(window, text="Repetir", command=repeat_music)
repeat_button.pack(side="left", padx=10, pady=10)

# Inicia o loop principal do Tkinter
window.mainloop()