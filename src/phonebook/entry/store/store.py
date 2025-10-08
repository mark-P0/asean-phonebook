from lib.pydantic import enum_input
from phonebook import Phonebook
from phonebook.entry import PhonebookEntry, PhonebookEntryRepeat


class PhonebookEntryStore:
    def __init__(self, phonebook: Phonebook):
        self.loop(phonebook)

    def loop(self, phonebook: Phonebook):
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
