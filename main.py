from src.lib.terminal import clear_screen
from src.menu import Menu, MenuSelection
from src.phonebook import Phonebook


class Program:
    @classmethod
    def run(cls, *, phonebook: Phonebook):
        while True:
            clear_screen()

            menu = Menu()
            print()

            if menu.selection == MenuSelection.STORE:
                phonebook.store_new_entry()

            if menu.selection == MenuSelection.EDIT:
                phonebook.init_edit_entry()

            if menu.selection == MenuSelection.SEARCH:
                input("[NOT_IMPLEMENTED] Press Enter to continue...")

            if menu.selection == MenuSelection.EXIT:
                break


if __name__ == "__main__":
    Program().run(
        phonebook=Phonebook(),
    )
