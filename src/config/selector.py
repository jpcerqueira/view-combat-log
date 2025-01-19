import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    pasta = filedialog.askdirectory(title="Selecione a pasta dos logs")
    root.destroy()  # Fecha o Tkinter após a seleção
    return pasta