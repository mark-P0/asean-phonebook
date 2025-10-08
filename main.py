from src.lib.terminal import clear_screen
from src.menu import Menu, MenuSelection
from src.core.phonebook import (
    Phonebook,
    PhonebookEntry,
    PhonebookEntryCountryCode,
    PhonebookEntryGender,
)


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


if __name__ == "__main__":
    entries: None = [
        PhonebookEntry(
            student_number="2004-56",
            surname="Lee",
            first_name="Sukarno",
            occupation="Doctor",
            gender=PhonebookEntryGender.MALE,
            country_code=PhonebookEntryCountryCode.PHILIPPINES,
            area_code=2,
            number=4567890,
        )
    ]

    phonebook = Phonebook(entries=entries)

    Program().run(phonebook=phonebook)
