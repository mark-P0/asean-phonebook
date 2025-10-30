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
