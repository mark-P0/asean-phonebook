from enum import Enum


from asean_phonebook.lib.pydantic import enum_input, typed_input
from asean_phonebook.lib.python.enum import EnumValues
from asean_phonebook.phonebook.entry.entry import (
    PhonebookEntry,
    PhonebookEntryCountryCode,
    PhonebookEntryGender,
)
from asean_phonebook.phonebook.phonebook import Phonebook


class StoreProgramRepeat(EnumValues, Enum):
    YES = "Y"
    NO = "N"


def prompt_new_entry():
    student_number = input("Enter student number: ")
    surname = input("Enter surname: ")
    first_name = input("Enter first name: ")
    occupation = input("Enter occupation: ")

    gender = enum_input(
        message="Enter gender (M for male, F for female): ",
        enum=PhonebookEntryGender,
    )

    country_code = enum_input(
        message="Enter country code: ",
        enum=PhonebookEntryCountryCode,
    )

    area_code = typed_input(message="Enter area code: ", _type=int)
    number = typed_input(message="Enter number: ", _type=int)

    model_dict = dict(
        student_number=student_number,
        surname=surname,
        first_name=first_name,
        occupation=occupation,
        gender=gender,
        country_code=country_code,
        area_code=area_code,
        number=number,
    )

    return PhonebookEntry.model_validate(model_dict)


def run_store_program(*, phonebook: Phonebook):
    while True:
        entry = prompt_new_entry()
        phonebook.entries.append(entry)

        answer = enum_input(
            message="Do you want to enter another entry [Y/N]? ",
            enum=StoreProgramRepeat,
        )
        print()

        if answer == StoreProgramRepeat.NO:
            break


if __name__ == "__main__":
    run_store_program(phonebook=Phonebook())
