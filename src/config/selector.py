import tkinter as tk
from tkinter import filedialog
from utils.translator import get_translation
from config.manager import load_configuration

def get_current_language():
        config = load_configuration()
        current_language = config["current_language"]
        return current_language

def select_folder():
    current_language = get_current_language()
    root = tk.Tk()
    root.withdraw()
    pasta = filedialog.askdirectory(title=get_translation(current_language, "selector.title"))
    root.destroy()
    return pasta