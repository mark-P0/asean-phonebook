from lib.terminal import clear_screen
from phonebook.entry.edit.edit import PhonebookEntryEdit
from phonebook.entry.store.store import PhonebookEntryStore
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
                PhonebookEntryStore(phonebook=phonebook)

            if menu.selection == ProgramMenuSelection.EDIT:
                PhonebookEntryEdit(phonebook=phonebook)

            if menu.selection == ProgramMenuSelection.SEARCH:
                _: int = input("[NOT_IMPLEMENTED] Press Enter to continue...")

            if menu.selection == ProgramMenuSelection.EXIT:
                break
