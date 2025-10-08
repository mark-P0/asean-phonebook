from pydantic import BaseModel

from phonebook.entry import (
    PhonebookEntry,
    PhonebookEntryCountryCode,
    PhonebookEntryGender,
    PhonebookEntryRepeat,
)
from phonebook.entry.edit.menu import (
    PhonebookEntryEditMenuItems,
    PhonebookEntryEditMenuSelection,
)
from lib.terminal import clear_screen
from lib.pydantic import enum_input, typed_input


class Phonebook(BaseModel):
    entries: list[PhonebookEntry] = []

    def get_entry_from_student_number(self, student_number: str):
        for entry in self.entries:
            if entry.student_number == student_number:
                return entry

        return None

    def store_new_entry(self):
        while True:
            entry = PhonebookEntry.from_prompt()
            self.entries.append(entry)

            answer = enum_input(
                message="Do you want to enter another entry [Y/N]? ",
                enum=PhonebookEntryRepeat,
            )
            print()

            if answer == PhonebookEntryRepeat.NO:
                break

    def init_edit_entry(self):
        student_number = input("Enter student number: ")

        entry = self.get_entry_from_student_number(student_number)

        if entry is None:
            print("Student does not exist.")
            input("Press Enter to continue...")

            return

        return self.edit_entry(entry)

    def edit_entry(self, entry: PhonebookEntry):
        while True:
            clear_screen()

            print(entry)
            print(PhonebookEntryEditMenuItems())
            selection = enum_input(
                message="Enter choice: ",
                enum=PhonebookEntryEditMenuSelection,
            )

            if selection == PhonebookEntryEditMenuSelection.STUDENT_NUMBER:
                entry.student_number = input("Enter new student number: ")

            if selection == PhonebookEntryEditMenuSelection.SURNAME:
                entry.surname = input("Enter new surname: ")

            if selection == PhonebookEntryEditMenuSelection.GENDER:
                entry.gender = enum_input(
                    message="Enter new gender (M for male, F for female): ",
                    enum=PhonebookEntryGender,
                )

            if selection == PhonebookEntryEditMenuSelection.OCCUPATION:
                entry.occupation = input("Enter new occupation: ")

            if selection == PhonebookEntryEditMenuSelection.COUNTRY_CODE:
                entry.country_code = enum_input(
                    message="Enter new country code: ",
                    enum=PhonebookEntryCountryCode,
                )

            if selection == PhonebookEntryEditMenuSelection.AREA_CODE:
                entry.area_code = typed_input(
                    message="Enter new area code: ", _type=int
                )

            if selection == PhonebookEntryEditMenuSelection.PHONE_NUMBER:
                entry.number = typed_input(message="Enter new number: ", _type=int)

            if selection == PhonebookEntryEditMenuSelection.NONE:
                break
