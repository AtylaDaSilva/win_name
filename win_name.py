from os import system, listdir, rename
from os.path import isdir
from re import compile


def run():
    main_menu()
    return


def clear():
    system("cls")


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
        1: "[1] Full Rename",
        2: "[2] Match & Replace",
    }

    for k, v in main_menu_options.items():
        print(v)

    choice = int(wait_for_input("Choose an option: "))

    match choice:
        case 1:
            full_rename_menu()
        case 2:
            match_and_replace_menu()
        case _:
            wait_for_input("Invalid choice. Press anything to exit program.")

    return


def full_rename_menu():
    clear()
    main_title("Full Rename")

    directory = wait_for_input("Insert a directory: ")
    new_name = wait_for_input("Insert the new name: ")

    if isdir(directory):
        #
        entries = listdir(directory)
        msg = f"\nThe following entries will be affected:\n\n{'\n'.join(entries)}\n\nProceed? [Y/N] "
        if bool(wait_for_input(msg)):
            print("\nRenaming directories...")
            regexp = compile(r"\.\w{3,4}$")
            for entry in entries:
                m = regexp.findall(entry)
                ext = m.pop() if len(m) > 0 else ""
                src = f"{directory}\\{entry}"
                dst = f"{new_name}{ext}"
                print(src)
                print(dst)
                wait_for_input("")
                # rename(src, dst)
                print(f"\nRenaming: '{src}' -> '{directory}\\{dst}'.")
            wait_for_input("Process finished. Press anything to exit.")

    else:
        print("Invalid or non-existing directory.")
        wait_for_input("Exiting. Press anything to continue...")
    return


def match_and_replace_menu():
    clear()
    print("TODO")
    return

