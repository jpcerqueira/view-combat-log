import os
import sys
import json

def load_translations():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else: 
        base_path = os.path.abspath(".")

    json_path = os.path.join(base_path, "utils/translations.json")

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_translation(lang, key, **kwargs):
    translations = load_translations()
    """
    Obtém uma mensagem traduzida com base na chave e no idioma.
    Suporta chaves aninhadas (ex.: "menu.option_1").
    """
    keys = key.split(".")  # Divide chaves aninhadas
    message = translations.get(lang, {})
    for k in keys:
        message = message.get(k, f"[{key}] não encontrado")
        if not isinstance(message, dict):  # Interrompe se a chave final for uma string
            break
    if isinstance(message, str):
        # Avalia variáveis dinâmicas, como dicionários
        try:
            return message.format(**kwargs)
        except KeyError as e:
            return f"Erro: variável '{e.args[0]}' ausente na mensagem."
    return f"[{key}] não encontrado"

