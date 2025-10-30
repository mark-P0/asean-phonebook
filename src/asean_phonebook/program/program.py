from asean_phonebook.lib.terminal import clear_screen
from asean_phonebook.phonebook.edit import PhonebookEdit
from asean_phonebook.phonebook.entry.mocks import MockPhonebookEntry
from asean_phonebook.phonebook.phonebook import Phonebook
from asean_phonebook.phonebook.search.search import PhonebookSearch
from asean_phonebook.phonebook.store import PhonebookStore
from asean_phonebook.program.menu import ProgramMenu, ProgramMenuSelection


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


if __name__ == "__main__":
    entries = [
        MockPhonebookEntry.SUKARNO_LEE,
        MockPhonebookEntry.JULIANA_DELA_CRUZ,
        MockPhonebookEntry.SAWADI_KRAP,
        MockPhonebookEntry.JOHN_SAINT,
    ]
    phonebook = Phonebook(entries=entries)

    Program(phonebook=phonebook)
