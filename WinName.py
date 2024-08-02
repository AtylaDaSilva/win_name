import sys
from os import system, listdir, rename
from os.path import isdir
from re import compile
from pathlib import Path


class WinName:
    def __init__(self) -> None:
        self.quit = False

    def run(self):
        while not self.quit:
            self.main_menu()
        self.kill()

    @staticmethod
    def clear():
        system("cls")

    def kill(self):
        self.wait_for_input("Exiting... Press anything to continue.")
        sys.exit()

    @staticmethod
    def wait_for_input(message: str) -> str:
        return input(message)
    
    @staticmethod
    def yes_or_no(message: str) -> bool:
        return True if input(f"{message} [Y/N] -> ").upper() == "Y" else False

    @staticmethod
    def print_title(title: str):
        main_title_mult = 30
        print("*" * main_title_mult)
        print("|" + title.center(main_title_mult - 2, " ") + "|")
        print("*" * main_title_mult)

    @staticmethod
    def print_summary(items: tuple, fill_length: int = 15):
        summary_text = f"\n{'-' * fill_length} Summary {'-' * fill_length}\n"
        print(summary_text)
        print("\n".join(items))
        print(summary_text)


    def main_menu(self):
        try:
            self.clear()
            self.print_title("Win_name")

            main_menu_options = {
                1: "[1] Match & Replace"
            }

            # Append 'Quit' option to menu
            menu_length = len(main_menu_options)
            del_pos = menu_length + 1;
            main_menu_options[del_pos] = f"[{del_pos}] Quit"

            # Print Options
            for k, v in main_menu_options.items():
                print(v)

            # Obtain and validate user input
            choice = int(self.wait_for_input("Choose an option: "))

            main_menu_options_keys = main_menu_options.keys()

            if choice not in main_menu_options_keys:
                raise ValueError(f"Invalid choice. Only  allowed.")

            match choice:
                case 1:
                    self.match_and_replace()
                case del_pos:
                    self.kill()
        except ValueError:
            self.wait_for_input(f"Invalid input. Press anything to go back to the menu.")

    def match_and_replace(self):
        try:
            restart = False
            while not restart:
                self.clear()
                self.print_title("Match & Replace")

                # Get user input
                path_usr_input = self.wait_for_input("Insert a directory: ")
                regexp_usr_input = self.wait_for_input("Insert a Regular Expression (without '/'): ")
                replacer = self.wait_for_input("Insert a replacer: ")
                rename_folders = self.yes_or_no("Rename matching folders too?")

                summary_items = (
                    f"Directory -> '{path_usr_input}'",
                    f"Regular Expression -> /{regexp_usr_input}/",
                    f"Replacer -> '{replacer}'",
                    f"Replace folders? {"Yes" if rename_folders else "No"}"
                )

                self.print_summary(summary_items)

                restart = self.yes_or_no("\nIs this correct?")

            # Validate path
            path = Path(path_usr_input)

            if not path.is_dir():
                raise FileNotFoundError(f"Path '{path_usr_input}' is invalid or does not exist.")
            
            # Compile Regular Expression
            regexp = compile(regexp_usr_input)

            # Find matching directories
            targets = list()  # List of target paths as strings
            paths = list()  # List of pats as instances of WindowsPath

            for p in path.iterdir():
                anchor, root, name = p.parts
                full_path_str = f"{anchor}{root}\\{name}"
                match = regexp.search(full_path_str)
                if match is not None:
                    if p.is_dir() and not rename_folders:
                        continue
                    else:
                        targets.append(full_path_str)
                        paths.append((p, match))


            proceed = self.yes_or_no(f"\nThe following target(s) will be affected: \n\n{'\n '.join(targets)}\n\nProceed?")

            if not proceed:
                self.kill()

            print("\nRenaming item(s). Just a sec...")

            for p in paths:
                new_path = p[0].parents[0] / p[0].name.replace(p[1].group(0), replacer)
                # new_path = new_path.with_suffix(p.suffix)

                #file_exists = new_path.is_file() TODO

                p[0].rename(new_path)
            
            self.wait_for_input("\nDone! Press anything to go back to the menu.")
        except FileNotFoundError as exc:
            self.wait_for_input(f"Exception caught! {exc}")

