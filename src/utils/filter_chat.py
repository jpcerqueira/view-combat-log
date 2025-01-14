import os

def filter_chat(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as input:
            lines = input.readlines()

        filtered_messages = [
            line for line in lines 
            if "] You have hit" in line or "hit you" in line or 'Você atingiu <'  in line or 'atingiu você' in line
        ]

        if filtered_messages:
            with open(output_file, 'w', encoding='utf-8') as output:
                output.writelines(filtered_messages)
            print(f"** Filtro concluído! Mensagens filtradas salvas em: {output_file} **\n")
        else:
            print("** Nenhum log de batalha presente nesse arquivo. **\n")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return filtered_messages

def show_files(directory_path):
    log_files = [None] + [f for f in os.listdir(directory_path) if f.endswith('.log')]
    for idx, file in enumerate(log_files[1:], start=1): print(f"{idx}: {file}")
    print()
    print("0: Voltar ao Menu Principal\n")
    return log_files

def select_files(log_files, idx_file):
    #idx_file = int(input('Digite o indice do arquivo que deseja ver o relatório: '))
    file = log_files[idx_file]
    print()
    return file