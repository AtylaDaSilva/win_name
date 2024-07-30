def run():
    main_menu()
    return


def wait_for_input(message):
    return input(message)


def main_menu():
    main_title_mult = 20
    print("*" * main_title_mult)
    print("|" + "Win_name".center(main_title_mult - 2, " ") + "|")
    print("*" * main_title_mult)

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
    print("TODO")
    return


def match_and_replace_menu():
    print("TODO")
    return

