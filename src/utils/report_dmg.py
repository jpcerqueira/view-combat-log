from utils.translator import get_translation
from config.manager import load_configuration

def get_current_language():
        config = load_configuration()
        current_language = config["current_language"]
        return current_language

def report_dmg (damage_dealt, damage_taken, total_damage_dealt, total_damage_taken, dead_list, dead_count, file_resume):
    current_language = get_current_language()
    with open(file_resume, "w", encoding="utf-8") as resume:
            resume.write(get_translation(current_language, "report_dmg.dmg_dealt"))
            resume.write("\n")
            for target, hit_location in damage_dealt.items():
                resume.write(f"{target}\n")
                total_target = 0
                for i, type_damage in hit_location.items():
                    resume.write(f"<< {i} >>\n")
                    for type_damage, damage in type_damage.items():
                        resume.write(f"{type_damage} - {damage:.2f}\n")
                        total_target += damage
                #formatted_total_target = f"{total_target:.2f}"
                resume.write(get_translation(current_language, "report_dmg.total_dmg_dealt_target", target=target, total_target=total_target))
                resume.write("\n")
            resume.write("\n")
            resume.write(get_translation(current_language, "report_dmg.total_dmg_dealt", total_damage_dealt=total_damage_dealt))
            resume.write("\n")
            resume.write("x==================================x\n")
            resume.write("\n")

            resume.write(get_translation(current_language, "report_dmg.kill_list"))
            resume.write("\n")
            for dead_target, dead_target_count in dead_list.items():
                resume.write(f"{dead_target} - {dead_target_count}\n")
            resume.write("\n")
            resume.write(get_translation(current_language, "report_dmg.total_kill", dead_count=dead_count))
                
            resume.write("\n")
            resume.write("x==================================x\n")
            resume.write("\n")

            resume.write(get_translation(current_language, "report_dmg.dmg_taken"))
            resume.write("\n")
            for target, hit_location in damage_taken.items():
                resume.write(f"{target}\n")
                total_target = 0
                for i, type_damage in hit_location.items():
                    resume.write(f"<< {i} >>\n")
                    for type_damage, damage in type_damage.items():
                        resume.write(f"{type_damage} - {damage:.2f}\n")
                        total_target += damage
                resume.write(get_translation(current_language, "report_dmg.total_dmg_taken_target", target=target, total_target=total_target))
                resume.write("\n")
            resume.write("\n")
            resume.write(get_translation(current_language, "report_dmg.total_dmg_taken", total_damage_taken=total_damage_taken))