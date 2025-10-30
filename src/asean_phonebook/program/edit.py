from asean_phonebook.lib.pydantic import enum_input, typed_input
from asean_phonebook.lib.terminal import clear_screen
from asean_phonebook.phonebook.entry.entry import (
    PhonebookEntry,
    PhonebookEntryCountryCode,
    PhonebookEntryGender,
)
from asean_phonebook.phonebook.entry.mocks import MockPhonebookEntry
from asean_phonebook.phonebook.phonebook import Phonebook
from asean_phonebook.program.menu.edit import (
    EditEntryProgramMenu,
    EditEntryProgramMenuSelection,
)


def run_edit_entry_program(*, entry: PhonebookEntry):
    while True:
        clear_screen()

        menu = EditEntryProgramMenu(entry)

        if menu.selection == EditEntryProgramMenuSelection.STUDENT_NUMBER:
            entry.student_number = input("Enter new student number: ")

        if menu.selection == EditEntryProgramMenuSelection.SURNAME:
            entry.surname = input("Enter new surname: ")

        if menu.selection == EditEntryProgramMenuSelection.GENDER:
            entry.gender = enum_input(
                message="Enter new gender (M for male, F for female): ",
                enum=PhonebookEntryGender,
            )

        if menu.selection == EditEntryProgramMenuSelection.OCCUPATION:
            entry.occupation = input("Enter new occupation: ")

        if menu.selection == EditEntryProgramMenuSelection.COUNTRY_CODE:
            entry.country_code = enum_input(
                message="Enter new country code: ",
                enum=PhonebookEntryCountryCode,
            )

        if menu.selection == EditEntryProgramMenuSelection.AREA_CODE:
            entry.area_code = typed_input(message="Enter new area code: ", _type=int)

        if menu.selection == EditEntryProgramMenuSelection.PHONE_NUMBER:
            entry.number = typed_input(message="Enter new number: ", _type=int)

        if menu.selection == EditEntryProgramMenuSelection.NONE:
            break


def prompt_entry(*, phonebook: Phonebook):
    student_number = input("Enter student number: ")

    entry = phonebook.find_entry(
        student_number=student_number,
    )

    return entry


def run_edit_program(*, phonebook: Phonebook):
    entry = prompt_entry(phonebook=phonebook)

    if entry is None:
        print("Student does not exist.")
        input("Press Enter to continue...")

        return

    run_edit_entry_program(entry=entry)


if __name__ == "__main__":
    # run_edit_program(phonebook=Phonebook(entries=[MockPhonebookEntry.SUKARNO_LEE]))
    run_edit_entry_program(entry=MockPhonebookEntry.SUKARNO_LEE)
