def report_dmg (damage_dealt, damage_taken, file_resume):
    with open(file_resume, 'w', encoding='utf-8') as resume:
            resume.write("Danos causados:\n")
            resume.write('\n')
            for target, damage in damage_dealt.items():
                resume.write(f"{target}\n")
                for type_damage, total in damage.items():
                    resume.write(f"{type_damage} - {total:.2f}\n")
                resume.write("\n")

            resume.write("Danos sofridos:\n")
            resume.write('\n')
            for target, damage in damage_taken.items():
                resume.write(f"{target}\n")
                for type_damage, total in damage.items():
                    resume.write(f"{type_damage} - {total:.2f}\n")
                resume.write("\n")