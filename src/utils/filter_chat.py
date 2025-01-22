import os
from utils.translator import get_translation
from config.manager import load_configuration

def get_current_language():
        config = load_configuration()
        current_language = config["current_language"]
        return current_language

def filter_chat(input_file, output_file):
    current_language = get_current_language()
    try:
        with open(input_file, 'r', encoding='utf-8') as input:
            lines = input.readlines()

        filtered_messages = [
            line for line in lines 
            if "] You have hit" in line or "hit you" in line or 'Você atingiu <'  in line or 'atingiu você' in line or "You have killed" in line
        ]

        if filtered_messages:
            with open(output_file, 'w', encoding='utf-8') as output:
                output.writelines(filtered_messages)
            print(get_translation(current_language, "filter_chat.filter_1", output_file=output_file))
        else:
            print(get_translation(current_language, "filter_chat.filter_2"))

    except FileNotFoundError:
        print(get_translation(current_language, "filter_chat.fileNotFoundError", input_file=input_file))
    except Exception as e:
        print(get_translation(current_language, "filter_chat.exception", e=e))

    return filtered_messages

def show_files(directory_path):
    current_language = get_current_language()
    log_files = [None] + [f for f in os.listdir(directory_path) if f.endswith('.log')]
    for idx, file in enumerate(log_files[1:], start=1): print(f"{idx}: {file}")
    print()
    print(get_translation(current_language, "filter_chat.show_files"))
    return log_files

def select_files(log_files, idx_file):
    file = log_files[idx_file]
    print()
    return file