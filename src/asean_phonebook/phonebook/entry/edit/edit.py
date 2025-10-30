from asean_phonebook.lib.pydantic import enum_input, typed_input
from asean_phonebook.lib.terminal import clear_screen
from asean_phonebook.phonebook.entry.edit.menu import (
    PhonebookEntryEditMenu,
    PhonebookEntryEditMenuSelection,
)
from asean_phonebook.phonebook.entry.entry import (
    PhonebookEntry,
    PhonebookEntryCountryCode,
    PhonebookEntryGender,
)
from asean_phonebook.phonebook.entry.mocks import MockPhonebookEntry


class PhonebookEntryEdit:
    def __init__(self, *, entry: PhonebookEntry):
        self.run(entry)

    def run(self, entry: PhonebookEntry):
        while True:
            clear_screen()

            menu = PhonebookEntryEditMenu(entry)

            if menu.selection == PhonebookEntryEditMenuSelection.STUDENT_NUMBER:
                entry.student_number = input("Enter new student number: ")

            if menu.selection == PhonebookEntryEditMenuSelection.SURNAME:
                entry.surname = input("Enter new surname: ")

            if menu.selection == PhonebookEntryEditMenuSelection.GENDER:
                entry.gender = enum_input(
                    message="Enter new gender (M for male, F for female): ",
                    enum=PhonebookEntryGender,
                )

            if menu.selection == PhonebookEntryEditMenuSelection.OCCUPATION:
                entry.occupation = input("Enter new occupation: ")

            if menu.selection == PhonebookEntryEditMenuSelection.COUNTRY_CODE:
                entry.country_code = enum_input(
                    message="Enter new country code: ",
                    enum=PhonebookEntryCountryCode,
                )

            if menu.selection == PhonebookEntryEditMenuSelection.AREA_CODE:
                entry.area_code = typed_input(
                    message="Enter new area code: ", _type=int
                )

            if menu.selection == PhonebookEntryEditMenuSelection.PHONE_NUMBER:
                entry.number = typed_input(message="Enter new number: ", _type=int)

            if menu.selection == PhonebookEntryEditMenuSelection.NONE:
                break


if __name__ == "__main__":
    PhonebookEntryEdit(entry=MockPhonebookEntry.SUKARNO_LEE)
