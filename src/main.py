import os

from utils.filter_chat import filter_chat, show_files, select_files
from utils.filter_dmg import filter_dmg
from utils.filter_kill import filter_kill
from utils.report_dmg import report_dmg
from utils.menu import Menu
from config.manager import load_configuration, save_configuration
from config.selector import select_folder




config = load_configuration()

if "log_path" in config:
    print(f"Pasta dos logs: {config['log_path']}\n")

else:
    folder = select_folder()
    if folder:
        config["log_path"] = folder
        save_configuration(config)
        print(f"Pasta dos logs salva: {folder}")


while True:

    Menu.open_main_menu()

    select_menu = int(input())

    os.system('cls')

    if select_menu == 1:

        while True:
            Menu.menu_header()

            log_files = show_files(config["log_path"])

            idx_file = int(input('Digite o indice do arquivo que deseja ver o relatório OU zero para voltar ao Menu Principal: '))


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

            input('Press ENTER to continue.')

            os.system('cls')

    elif select_menu == 2:
        Menu.open_menu_select_folder()
        folder = config["log_path"]
        print(f" >>> {folder[-10:]}\n")

        folder = select_folder()

        if folder:
            config["log_path"] = folder
            save_configuration(config)
            print(f"Nova pasta dos logs salva: {folder}\n")

        input('Press ENTER to exit.')

        os.system('cls')

    elif select_menu == 0:
        break

print()

os.system('cls')