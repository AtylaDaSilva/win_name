import sys
from os import system, listdir, rename
from os.path import isdir
from re import compile
from pathlib import Path


def run():
    main_menu()
    return


def clear():
    system("cls")


def kill():
    wait_for_input("Exiting... Press anything to continue.")
    sys.exit()


def wait_for_input(message):
    return input(message)


def main_title(title: str):
    main_title_mult = 30
    print("*" * main_title_mult)
    print("|" + title.center(main_title_mult - 2, " ") + "|")
    print("*" * main_title_mult)


def main_menu():
    clear()
    main_title("Win_name")

    main_menu_options = {
        1: "[1] Match & Replace",
    }

    for k, v in main_menu_options.items():
        print(v)

    choice = int(wait_for_input("Choose an option: "))

    match choice:
        case 1:
            match_and_replace()
        case _:
            wait_for_input("Invalid choice. Press anything to exit.")

    return


def match_and_replace():
    clear()
    main_title("Match & Replace")
    directory = wait_for_input("Insert a directory: ")

    if not isdir(directory):
        print("Invalid or non-existing directory.")
        kill()

    p = Path(directory)

    wait_for_input("")
    return

