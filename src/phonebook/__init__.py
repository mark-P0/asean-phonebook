from pydantic import BaseModel

from phonebook.entry import (
    PhonebookEntry,
    PhonebookEntryRepeat,
)
from lib.pydantic import enum_input


class Phonebook(BaseModel):
    entries: list[PhonebookEntry] = []

    def get_entry_from_student_number(self, student_number: str):
        for entry in self.entries:
            if entry.student_number == student_number:
                return entry

        return None

    def find_entry(self, *, student_number: str | None = None):
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
