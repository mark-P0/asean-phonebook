from lib.terminal import clear_screen
from menu import Menu, MenuSelection
from core.phonebook import Phonebook


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
                _: int = input("[NOT_IMPLEMENTED] Press Enter to continue...")

            if menu.selection == MenuSelection.EXIT:
                break
