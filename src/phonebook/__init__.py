from pydantic import BaseModel

from phonebook.entry import PhonebookEntry


class Phonebook(BaseModel):
    entries: list[PhonebookEntry] = []

    def find_entry(self, *, student_number: str | None = None):
        for entry in self.entries:
            if entry.student_number == student_number:
                return entry

        return None
