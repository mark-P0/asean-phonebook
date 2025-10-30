from lib.terminal import clear_screen
from phonebook.edit import PhonebookEdit
from phonebook.phonebook import Phonebook
from phonebook.search.search import PhonebookSearch
from phonebook.store import PhonebookStore
from program.menu import ProgramMenu, ProgramMenuSelection


class Program:
    def __init__(self, *, phonebook: Phonebook):
        self.run(phonebook)

    def run(self, phonebook: Phonebook):
        while True:
            clear_screen()

            menu = ProgramMenu()
            print()

            if menu.selection == ProgramMenuSelection.STORE:
                PhonebookStore(phonebook=phonebook)

            if menu.selection == ProgramMenuSelection.EDIT:
                PhonebookEdit(phonebook=phonebook)

            if menu.selection == ProgramMenuSelection.SEARCH:
                PhonebookSearch(phonebook=phonebook)

            if menu.selection == ProgramMenuSelection.EXIT:
                break
