from asean_phonebook.lib.terminal import clear_screen
from asean_phonebook.phonebook.entry.mocks import MockPhonebookEntry
from asean_phonebook.phonebook.phonebook import Phonebook
from asean_phonebook.phonebook.search.search import PhonebookSearch
from asean_phonebook.program.edit import run_edit_program
from asean_phonebook.program.menu.program import ProgramMenu, ProgramMenuSelection
from asean_phonebook.program.store import run_store_program


def run_program(*, phonebook: Phonebook):
    while True:
        clear_screen()

        menu = ProgramMenu()
        print()

        if menu.selection == ProgramMenuSelection.STORE:
            run_store_program(phonebook=phonebook)

        if menu.selection == ProgramMenuSelection.EDIT:
            run_edit_program(phonebook=phonebook)

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

    run_program(phonebook=phonebook)
