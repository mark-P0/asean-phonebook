from lib.pydantic import enum_input
from phonebook.entry.entry import PhonebookEntry, PhonebookEntryRepeat
from phonebook.phonebook import Phonebook


class PhonebookEntryStore:
    def __init__(self, phonebook: Phonebook):
        self.run(phonebook)

    def run(self, phonebook: Phonebook):
        while True:
            entry = PhonebookEntry.from_prompt()
            phonebook.entries.append(entry)

            answer = enum_input(
                message="Do you want to enter another entry [Y/N]? ",
                enum=PhonebookEntryRepeat,
            )
            print()

            if answer == PhonebookEntryRepeat.NO:
                break


if __name__ == "__main__":
    PhonebookEntryStore(phonebook=Phonebook())
