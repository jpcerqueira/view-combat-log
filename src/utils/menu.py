from utils.translator import get_translation
from config.manager import load_configuration

class Menu():

    def get_current_language():
        config = load_configuration()
        current_language = config["current_language"]
        return current_language

    def menu_header():
        current_language = Menu.get_current_language()

        print("x============================x")
        print(get_translation(current_language, "menu.menu_header"))
        print("x===========================x\n")


    def open_main_menu():
        current_language = Menu.get_current_language()

        print(get_translation(current_language, "menu.main_menu"))
        print(get_translation(current_language, "menu.option_1"))
        print(get_translation(current_language, "menu.option_2"))
        print(get_translation(current_language, "menu.option_3"))
        print(get_translation(current_language, "menu.option_0"))
        print(get_translation(current_language, "menu.prompt"))

    def open_menu_select_folder():
        current_language = Menu.get_current_language()

        print(get_translation(current_language, "menu.select_folder"))

    def open_language_selection_menu():
        current_language = Menu.get_current_language()

        print(get_translation(current_language, "menu.select_language"))
        print(get_translation(current_language, "menu.option_language_1"))
        print(get_translation(current_language, "menu.option_language_2"))
        print(get_translation(current_language, "menu.option_language_3"))
        print(get_translation(current_language, "menu.option_language_0"))
        print(get_translation(current_language, "menu.prompt"))