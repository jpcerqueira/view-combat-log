def report_dmg (damage_dealt, damage_taken, total_damage_dealt, total_damage_taken, dead_list, file_resume):
    with open(file_resume, "w", encoding="utf-8") as resume:
            resume.write("Danos causados:\n")
            resume.write("\n")
            for target, damage in damage_dealt.items():
                resume.write(f"{target}\n")
                for type_damage, total in damage.items():
                    resume.write(f"{type_damage} - {total:.2f}\n")
                resume.write("\n")
            resume.write(f"Total de danos causados: {total_damage_dealt:.2f}\n")
            resume.write("\n")
            resume.write("x==================================x\n")
            resume.write("\n")

            resume.write("Lista de kills:\n") #colocar qtd de kills
            for i in dead_list:
                resume.write(f"{i}\n")
                
            resume.write("\n")
            resume.write("x==================================x\n")
            resume.write("\n")

            resume.write("Danos sofridos:\n")
            resume.write("\n")
            for target, damage in damage_taken.items():
                resume.write(f"{target}\n")
                for type_damage, total in damage.items():
                    resume.write(f"{type_damage} - {total:.2f}\n")
                resume.write("\n")
            resume.write(f"Total de danos sofridos: {total_damage_taken:.2f}\n")