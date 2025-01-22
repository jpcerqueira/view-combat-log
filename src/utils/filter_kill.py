import re
#from collections import defaultdict
from utils.translator import get_translation
from config.manager import load_configuration

def get_current_language():
        config = load_configuration()
        current_language = config["current_language"]
        return current_language

def filter_kill(input_file):
    current_language = get_current_language()
    try:
        with open(input_file, "r", encoding="utf-8") as input:
            lines = input.readlines()

        dead_list = {}
        dead_count:int = 0

        for line in lines:
            match = re.search(r"You have killed (\S+)", line)
            if match:
                dead_target = match.group(1)
                dead_count += 1
                dead_list[dead_target] = dead_list.get(dead_target, 0) + 1

    except FileNotFoundError:
        print(get_translation(current_language, "filter_kill.fileNotFoundError", input_file=input_file))

    except Exception as e:
        print(get_translation(current_language, "filter_kill.exception", e=e))

    return dead_list, dead_count