def report_dmg (damage_dealt, damage_taken, total_damage_dealt, total_damage_taken, dead_list, dead_count, file_resume):
    
    with open(file_resume, "w", encoding="utf-8") as resume:
            resume.write("Danos causados:\n")
            resume.write("\n")
            for target, hit_location in damage_dealt.items():
                resume.write(f"{target}\n")
                total_target = 0
                for i, type_damage in hit_location.items():
                    resume.write(f"<< {i} >>\n")
                    for type_damage, damage in type_damage.items():
                        resume.write(f"{type_damage} - {damage:.2f}\n")
                        total_target += damage
                resume.write(f">> Dano total em {target} = {total_target:.2f} <<\n")
                resume.write("\n")
            resume.write("\n")
            resume.write(f"TOTAL DE DANOS CAUSADOS: {total_damage_dealt:.2f}\n")
            resume.write("\n")
            resume.write("x==================================x\n")
            resume.write("\n")

            resume.write("Lista de kills:\n")
            resume.write("\n")
            for dead_target, dead_target_count in dead_list.items():
                resume.write(f"{dead_target} - {dead_target_count}\n")
            resume.write("\n")
            resume.write(f"Total de kill {dead_count}\n")
                
            resume.write("\n")
            resume.write("x==================================x\n")
            resume.write("\n")

            resume.write("Danos sofridos:\n")
            resume.write("\n")
            for target, hit_location in damage_taken.items():
                resume.write(f"{target}\n")
                total_target = 0
                for i, type_damage in hit_location.items():
                    resume.write(f"<< {i} >>\n")
                    for type_damage, damage in type_damage.items():
                        resume.write(f"{type_damage} - {damage:.2f}\n")
                        total_target += damage
                resume.write(f">> Dano total em {target} = {total_target:.2f} <<\n")
                resume.write("\n")
            resume.write("\n")
            resume.write(f"TOTAL DE DANOS SOFRIDOS: {total_damage_taken:.2f}\n")