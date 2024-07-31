import sys
from os import system, listdir, rename
from os.path import isdir
from re import compile
from pathlib import Path

class Win_name:
    def __init__(self) -> None:
        self.quit = True

    def run(self):
        while not self.quit:
            self.main_menu()
        self.kill()


    def clear(self):
        system("cls")


    def kill(self):
        self.wait_for_input("Exiting... Press anything to continue.")
        sys.exit()

    def wait_for_input(self, message):
        return input(message)


    def main_title(self, title: str):
        main_title_mult = 30
        print("*" * main_title_mult)
        print("|" + title.center(main_title_mult - 2, " ") + "|")
        print("*" * main_title_mult)


    def main_menu(self):
        self.clear()
        self.main_title("Win_name")

        main_menu_options = (
            "[1] Match & Replace"
        )

        for opt in main_menu_options:
            print(opt)

        choice = int(self.wait_for_input("Choose an option: "))

        match choice:
            case 1:
                self.match_and_replace()
            case _:
                self.wait_for_input("Invalid choice. Press anything to continue.")

        return


    def match_and_replace(self):
        self.clear()
        self.main_title("Match & Replace")
        directory = wait_for_input("Insert a directory: ")

        if not isdir(directory):
            print("Invalid or non-existing directory.")
            kill()

        p = Path(directory)

        self.wait_for_input("")
        return

