import random

from pydantic import BaseModel

from lib.inflect import oxford_join
from lib.terminal import clear_screen
from phonebook import Phonebook
from phonebook.entry import (
    PhonebookEntry,
    PhonebookEntryCountryCode,
    PhonebookEntryGender,
)
from phonebook.entry.search.menu import (
    PhonebookEntrySearchMenu,
    PhonebookEntrySearchMenuItems,
    PhonebookEntrySearchMenuSelection,
)


class PhonebookEntrySearchResult(BaseModel):
    phonebook: Phonebook
    selections: list[PhonebookEntrySearchMenuSelection]

    def __str__(self):
        lines = [
            self._result_header,
            *self._matching_entries_as_str,
        ]

        return "\n".join(lines)

    @property
    def _result_header(self):
        selection_labels = [
            *PhonebookEntrySearchMenuItems.gen_labels_from_selections(self.selections)
        ]

        return f"Here are the students from {oxford_join(selection_labels)}:"

    @property
    def _matching_entries_as_str(self):
        selected_country_codes = [*self._gen_country_codes_from_selections()]

        matching_entries_gen = (
            entry
            for entry in self.phonebook.entries
            if entry.country_code in selected_country_codes
        )
        matching_entries = sorted(matching_entries_gen, key=lambda entry: entry.surname)

        return [entry.as_search_str for entry in matching_entries]

    def _gen_country_codes_from_selections(self):
        for selection in self.selections:
            country_code = PhonebookEntryCountryCode.__members__.get(selection.name)

            if country_code is not None:
                yield country_code


class PhonebookEntrySearch:
    def __init__(self, *, phonebook: Phonebook):
        self.run(phonebook)

    def run(self, phonebook: Phonebook):
        clear_screen()

        menu = PhonebookEntrySearchMenu()
        print()

        result = PhonebookEntrySearchResult(
            phonebook=phonebook,
            selections=menu.selections,
        )
        print(result)
        print()

        input("Press Enter to continue...")


if __name__ == "__main__":
    # test = PhonebookEntrySearchMenuSelection.ALL
    # print(f"{test=}")
    # print(f"{test.name=}")
    # print(f"{(test.name in PhonebookEntryCountryCode)=}")
    # print(f"{PhonebookEntryCountryCode[test.name]=}")

    # selections = [*PhonebookEntrySearchMenuSelection]
    # print(f"{selections=}")
    # country_codes = [*gen_country_codes_from_selections(selections)]
    # print(f"{country_codes=}")

    entries = [
        PhonebookEntry(
            student_number="1991-000",
            surname="Dela Cruz",
            first_name="Juliana",
            occupation="Princess",
            gender=PhonebookEntryGender.FEMALE,
            country_code=PhonebookEntryCountryCode.PHILIPPINES,
            area_code=6,
            number=678123890,
        ),
        PhonebookEntry(
            student_number="1999-890",
            surname="Krap",
            first_name="Sawadi",
            occupation="Sorcerer",
            gender=PhonebookEntryGender.MALE,
            country_code=PhonebookEntryCountryCode.THAILAND,
            area_code=8,
            number=1234567,
        ),
        PhonebookEntry(
            student_number="2000-123",
            surname="Saint",
            first_name="John",
            occupation="Doctor",
            gender=PhonebookEntryGender.MALE,
            country_code=PhonebookEntryCountryCode.PHILIPPINES,
            area_code=2,
            number=9998765,
        ),
    ]
    random.shuffle(entries)

    phonebook = Phonebook(entries=entries)

    result = PhonebookEntrySearchResult(
        phonebook=phonebook,
        selections=[*PhonebookEntrySearchMenuSelection],
    )
    print(result)

    PhonebookEntrySearch(phonebook=phonebook)
