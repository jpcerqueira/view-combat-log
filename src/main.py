import os

from utils.filter_chat import filter_chat, show_files, select_files
from utils.filter_dmg import filter_dmg
from utils.filter_kill import filter_kill
from utils.report_dmg import report_dmg
from config.manager import load_configuration, save_configuration
from config.selector import select_folder
from utils.translator import get_translation
from utils.menu import Menu

def get_current_language():
        config = load_configuration()
        current_language = config["current_language"]
        return current_language

config = load_configuration()


if "current_language" in config:
    current_language = config["current_language"]

else:
    config["current_language"] = "pt"
    save_configuration(config)
    current_language = get_current_language()



if "log_path" in config:
    print(get_translation(current_language, "main.log_path_1", config=config)) #msg do erro

else:
    folder = select_folder()
    if folder:
        config["log_path"] = folder
        save_configuration(config)
        print(get_translation(current_language, "main.log_path_2", folder=folder))

while True:

    Menu.open_main_menu()

    select_menu = int(input())

    os.system('cls')

    if select_menu == 1:

        while True:
            Menu.menu_header()

            log_files = show_files(config["log_path"])

            idx_file = int(input(get_translation(current_language, "main.idex_file")))


            if idx_file == 0:
                os.system('cls')
                break

            else:
                file = select_files(log_files, idx_file) #talvez coloque dentro dos módulos / ta horrivel
                input_file = file 

                input_file_folder = config["log_path"] + "/" + file

                output_directory_file = 'Processed Messages'
                os.makedirs(output_directory_file, exist_ok=True)
                output_file = f'{output_directory_file}/filtered_messages_{input_file[:-4]}.txt'

                output_directory_arquivo_resumo = 'Damage Reports'
                os.makedirs(output_directory_arquivo_resumo, exist_ok=True)
                arquivo_resumo = f'{output_directory_arquivo_resumo}/resumo_danos_{input_file[:-4]}.txt'
                
                filtered_messages = filter_chat(input_file_folder, output_file)
        
            

            if filtered_messages:

                dead_list, dead_count = filter_kill(input_file_folder)

                damage_dealt, damage_taken, total_damage_dealt, total_damage_taken = filter_dmg(input_file_folder)

                report_dmg(damage_dealt, damage_taken, total_damage_dealt, total_damage_taken, dead_list, dead_count, arquivo_resumo)

            input(get_translation(current_language, "main.press_enter"))

            os.system('cls')

    elif select_menu == 2:
        Menu.open_menu_select_folder()
        folder = config["log_path"]
        print(f" >>> {folder[-10:]}\n")

        folder = select_folder()

        if folder:
            config["log_path"] = folder
            save_configuration(config)
            print(get_translation(current_language, "main.folder_save", folder=folder))

        input(get_translation(current_language, "main.press_enter"))
        os.system('cls')

    elif select_menu == 3:
        Menu.open_language_selection_menu()

        language_selection = int(input())
        if language_selection == 1:
            current_language = "pt" 
        elif language_selection == 2:
            current_language = "en"
        elif language_selection == 3:
            current_language = "es"
        config["current_language"] = current_language
        save_configuration(config)
        
        input(get_translation(current_language, "main.press_enter"))
        os.system('cls')

    elif select_menu == 0:
        break

print()

os.system('cls')