import re
from collections import defaultdict

def filter_dmg(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as input:
            lines = input.readlines()

        damage_dealt = defaultdict(lambda: defaultdict(float))
        damage_taken = defaultdict(lambda: defaultdict(float))

        for line in lines:
            if 'You have hit' in line:
                match = re.search(r'You have hit <spush><color:C65F5F>(.*?)<spop> in .*? for <spush><color:C65F5F>(\d+\.\d+)<spop> of <spush><color:C65F5F>(.*?)<spop> damage', line)
                if match:
                    target = match.group(1)
                    damage = float(match.group(2))
                    type_damage = match.group(3)
                    damage_dealt[target][type_damage] += damage

            elif "has hit you" in line:
                match = re.search(r'<spush><color:C65F5F>(.*?)<spop> has hit you in .*? for <spush><color:C65F5F>(\d+\.\d+)<spop> of <spush><color:C65F5F>(.*?)<spop> damage', line)
                if match:
                    target = match.group(1)
                    damage = float(match.group(2))
                    type_damage = match.group(3)
                    damage_taken[target][type_damage] += damage

            elif 'Você atingiu <' in line:
                match = re.search(r'Você atingiu <spush><color:C65F5F>(.*?)<spop> em .*? para <spush><color:C65F5F>(\d+\.\d+)<spop> de <spush><color:C65F5F>(.*?)<spop> de dano', line)
                if match:
                    target = match.group(1)
                    damage = float(match.group(2))
                    type_damage = match.group(3)
                    damage_dealt[target][type_damage] += damage

            elif 'atingiu você' in line:
                match = re.search(r'<spush><color:C65F5F>(.*?)<spop> atingiu você em .*? para <spush><color:C65F5F>(\d+\.\d+)<spop> de <spush><color:C65F5F>(.*?)<spop> de dano', line)
                if match:
                    target = match.group(1)
                    damage = float(match.group(2))
                    type_damage = match.group(3)
                    damage_taken[target][type_damage] += damage

    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return damage_dealt, damage_taken