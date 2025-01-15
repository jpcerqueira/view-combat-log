import re
from collections import defaultdict

def filter_kill(input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as input:
            lines = input.readlines()

        dead_list = [] #criar um dic, onde será adicionado a qtd de vezes que o nick apareceu
        #dead_list = defaultdict(lambda: defaultdict(int))

        for line in lines:
            if "You have killed" in line:
                match = re.search(r"You have killed (\S+)", line) #quebra de linha
                dead_target = match.group(1)
                if dead_target not in dead_list:
                    dead_list.append(dead_target)

    except FileNotFoundError:
        print(f'Erro: O arquivo "{input_file}" não foi encontrado.')

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return dead_list