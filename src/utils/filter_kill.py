import re
from collections import defaultdict

def filter_kill(input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as input:
            lines = input.readlines()

        dead_list = {}
        dead_count:int = 0

        for line in lines:
            match = re.search(r"You have killed (\S+)", line)
            if match:
                dead_target = match.group(1)
                dead_count += 1
                dead_list[dead_target] = dead_list.get(dead_target, 0) + 1

    except FileNotFoundError:
        print(f'Erro: O arquivo "{input_file}" não foi encontrado.')

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return dead_list, dead_count