import re
import os
import sys
import json
from collections import defaultdict
from utils.translator import get_translation
from config.manager import load_configuration

def get_current_language():
        config = load_configuration()
        current_language = config["current_language"]
        return current_language

def load_patterns():
    # Localiza o diretório base onde o executável está rodando
    if getattr(sys, 'frozen', False):  # Quando executado como um executável PyInstaller
        base_path = sys._MEIPASS
    else:  # Quando executado como um script Python
        base_path = os.path.abspath(".")

    # Caminho para o arquivo JSON
    json_path = os.path.join(base_path, "utils/regex_patterns.json")

    # Carrega o JSON
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_dmg(input_file):
    current_language = get_current_language()
    try:
        patterns = load_patterns()

        damage_dealt = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
        damage_taken = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
        total_damage_dealt = 0.0
        total_damage_taken = 0.0

        with open(input_file, 'r', encoding='utf-8') as input:
            lines = input.readlines()

        for line in lines:
            for pattern in patterns:

                match = re.search(pattern["regex"], line)
                if match:
                    target = match.group(1)
                    hit_location = match.group(2)
                    damage = float(match.group(3))
                    type_damage = match.group(4)

                    if pattern["action"] == "damage_dealt":
                        damage_dealt[target][hit_location][type_damage] += damage
                        total_damage_dealt += damage
                    elif pattern["action"] == "damage_taken":
                        damage_taken[target][hit_location][type_damage] += damage
                        total_damage_taken += damage

                    break

    except FileNotFoundError:
        print(get_translation(current_language, "filter_dmg.fileNotFoundError", input_file=input_file))
    except Exception as e:
        print(get_translation(current_language, "filter_dmg.exception", e=e))

    return damage_dealt, damage_taken, total_damage_dealt, total_damage_taken