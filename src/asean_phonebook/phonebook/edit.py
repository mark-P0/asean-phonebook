from asean_phonebook.phonebook.entry.edit.edit import PhonebookEntryEdit
from asean_phonebook.phonebook.phonebook import Phonebook


class PhonebookEdit:
    def __init__(self, *, phonebook: Phonebook) -> None:
        self.run(phonebook)

    def run(self, phonebook: Phonebook):
        entry = self.prompt_entry(phonebook)
        if entry is None:
            print("Student does not exist.")
            input("Press Enter to continue...")

            return

        PhonebookEntryEdit(entry=entry)

    def prompt_entry(self, phonebook: Phonebook):
        student_number = input("Enter student number: ")

        entry = phonebook.find_entry(
            student_number=student_number,
        )

        return entry
