##FUTURAS IMPLEMENTAÇÕES

# SALVAR UM PNG COM O RELATÓRIO
# DIRECIONAR PARA PASTA DO LOG, NÃO PRECISANDO MAIS COPIAR, USAR O tkinter PARA ISSO, SALVANDO NA PASTA LOGS E FAZER OUTRO MENU E OUTRA FUNÇÃO PARA OLHAR E SELECIONAR A PASTA DO DIA

import os

from utils.filter_chat import filter_chat, show_files, select_files
from utils.filter_dmg import filter_dmg
from utils.report_dmg import report_dmg
#from utils.view_dmg import view_dmg
from utils.menu import Menu



while True:

    #Menu.menu_header()

    Menu.abrir_menu_principal()

    select_menu = int(input())

    os.system('cls')

    if select_menu == 1:

        while True:
            Menu.menu_header()

            log_files = show_files()

            idx_file = int(input('Digite o indice do arquivo que deseja ver o relatório OU zero para voltar ao Menu Principal: '))


            if idx_file == 0:
                os.system('cls')
                break

            else:

                file = select_files(log_files, idx_file)
                input_file = file #talvez coloque dentro dos módulos
                output_directory_file = 'Processed Messages'
                os.makedirs(output_directory_file, exist_ok=True)
                output_file = f'{output_directory_file}/filtered_messages_{input_file[:-4]}.txt'
                output_directory_arquivo_resumo = 'Damage Reports'
                os.makedirs(output_directory_arquivo_resumo, exist_ok=True)
                arquivo_resumo = f'{output_directory_arquivo_resumo}/resumo_danos_{input_file[:-4]}.txt'
                filtered_messages = filter_chat(input_file, output_file)
        
            input('Press ENTER to continue.')

            os.system('cls')

            if filtered_messages:

                filter_dmg(input_file)

                damage_dealt, damage_taken = filter_dmg(input_file)

                report_dmg(damage_dealt, damage_taken, arquivo_resumo)

                #view_dmg(damage_dealt, damage_taken)

                #input('Press ENTER to exit.')

    elif select_menu == 0:
        break


print()



os.system('cls')