from enum import Enum

from asean_phonebook.lib.pydantic import enum_input
from asean_phonebook.lib.python.enum import EnumValues
from asean_phonebook.phonebook.entry.entry import PhonebookEntry
from asean_phonebook.phonebook.phonebook import Phonebook


class PhonebookStoreRepeat(EnumValues, Enum):
    YES = "Y"
    NO = "N"


class PhonebookStore:
    def __init__(self, phonebook: Phonebook):
        self.run(phonebook)

    def run(self, phonebook: Phonebook):
        while True:
            entry = PhonebookEntry.from_prompt()
            phonebook.entries.append(entry)

            answer = enum_input(
                message="Do you want to enter another entry [Y/N]? ",
                enum=PhonebookStoreRepeat,
            )
            print()

            if answer == PhonebookStoreRepeat.NO:
                break


if __name__ == "__main__":
    PhonebookStore(phonebook=Phonebook())
