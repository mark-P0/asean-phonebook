from lib.terminal import clear_screen
from phonebook.entry.edit.edit import PhonebookEntryEdit
from phonebook.entry.search.search import PhonebookEntrySearch
from phonebook.entry.store.store import PhonebookEntryStore
from phonebook.phonebook import Phonebook
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
                PhonebookEntryStore(phonebook=phonebook)

            if menu.selection == ProgramMenuSelection.EDIT:
                PhonebookEntryEdit(phonebook=phonebook)

            if menu.selection == ProgramMenuSelection.SEARCH:
                PhonebookEntrySearch(phonebook=phonebook)

            if menu.selection == ProgramMenuSelection.EXIT:
                break
