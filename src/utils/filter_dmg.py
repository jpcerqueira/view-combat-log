import re
import os
import sys
import json
from collections import defaultdict

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
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return damage_dealt, damage_taken, total_damage_dealt, total_damage_taken