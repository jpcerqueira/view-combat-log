##FUTURAS IMPLEMENTAÇÕES

# SALVAR UM PNG COM O RELATÓRIO
# FAZER UM LOOP PARA UM NO MENU
# GERAR SEMPRE ARQUIVOS NOVOS, SEM SOBRESCREVER - COM A DATA DO LOG
# DIRECIONAR PARA PASTA DO LOG, NÃO PRECISANDO MAIS COPIAR

import os

from utils.filter_chat import filter_chat, view_files, select_files
from utils.filter_dmg import filter_dmg
from utils.report_dmg import report_dmg
from utils.view_dmg import view_dmg

log_files = view_files()

file = select_files(log_files)

os.system('cls')

input_file = file
output_file = 'filtered_messages.txt'
arquivo_resumo = 'resumo_danos.txt'

filtered_messages = filter_chat(input_file, output_file)

if filtered_messages:

    filter_dmg(input_file)

    damage_dealt, damage_taken = filter_dmg(input_file)

    report_dmg(damage_dealt, damage_taken, arquivo_resumo)

    view_dmg(damage_dealt, damage_taken)

print()

input('Press ENTER to exit.')

os.system('cls')