from pprint import pprint
from asean_phonebook.phonebook.entry.entry import (
    PhonebookEntry,
    PhonebookEntryCountryCode,
    PhonebookEntryGender,
)


class MockPhonebookEntry:
    SUKARNO_LEE = PhonebookEntry(
        student_number="2004-56",
        surname="Lee",
        first_name="Sukarno",
        occupation="Doctor",
        gender=PhonebookEntryGender.MALE,
        country_code=PhonebookEntryCountryCode.PHILIPPINES,
        area_code=2,
        number=4567890,
    )

    JULIANA_DELA_CRUZ = PhonebookEntry(
        student_number="1991-000",
        surname="Dela Cruz",
        first_name="Juliana",
        occupation="Princess",
        gender=PhonebookEntryGender.FEMALE,
        country_code=PhonebookEntryCountryCode.PHILIPPINES,
        area_code=6,
        number=678123890,
    )

    SAWADI_KRAP = PhonebookEntry(
        student_number="1999-890",
        surname="Krap",
        first_name="Sawadi",
        occupation="Sorcerer",
        gender=PhonebookEntryGender.MALE,
        country_code=PhonebookEntryCountryCode.THAILAND,
        area_code=8,
        number=1234567,
    )

    JOHN_SAINT = PhonebookEntry(
        student_number="2000-123",
        surname="Saint",
        first_name="John",
        occupation="Doctor",
        gender=PhonebookEntryGender.MALE,
        country_code=PhonebookEntryCountryCode.PHILIPPINES,
        area_code=2,
        number=9998765,
    )


if __name__ == "__main__":
    entries = [
        MockPhonebookEntry.SUKARNO_LEE,
        MockPhonebookEntry.JULIANA_DELA_CRUZ,
        MockPhonebookEntry.SAWADI_KRAP,
        MockPhonebookEntry.JOHN_SAINT,
    ]

    _ = "\n\n\n\n".join(
        "\n\n".join(
            [
                str(entry),
                entry.as_edit_str,
                entry.as_search_str,
            ]
        )
        for entry in entries
    )
    _ = {
        entry.student_number: dict(
            __str__=str(entry),
            edit=entry.as_edit_str,
            search=entry.as_search_str,
        )
        for entry in entries
    }

    pprint(_, width=100)
