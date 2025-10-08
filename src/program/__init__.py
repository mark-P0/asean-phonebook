from lib.terminal import clear_screen
from program.menu import ProgramMenu, ProgramMenuSelection
from phonebook import Phonebook


class Program:
    @classmethod
    def run(cls, *, phonebook: Phonebook):
        while True:
            clear_screen()

            menu = ProgramMenu()
            print()

            if menu.selection == ProgramMenuSelection.STORE:
                phonebook.store_new_entry()

            if menu.selection == ProgramMenuSelection.EDIT:
                phonebook.init_edit_entry()

            if menu.selection == ProgramMenuSelection.SEARCH:
                _: int = input("[NOT_IMPLEMENTED] Press Enter to continue...")

            if menu.selection == ProgramMenuSelection.EXIT:
                break
