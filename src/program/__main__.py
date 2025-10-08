from core.phonebook import Phonebook
from core.phonebook.entry import (
    PhonebookEntry,
    PhonebookEntryCountryCode,
    PhonebookEntryGender,
)
from program import Program


entries: None = [
    PhonebookEntry(
        student_number="2004-56",
        surname="Lee",
        first_name="Sukarno",
        occupation="Doctor",
        gender=PhonebookEntryGender.MALE,
        country_code=PhonebookEntryCountryCode.PHILIPPINES,
        area_code=2,
        number=4567890,
    )
]

phonebook = Phonebook(entries=entries)

Program().run(phonebook=phonebook)
