import random

from pydantic import BaseModel

from asean_phonebook.lib.inflect import oxford_join
from asean_phonebook.lib.terminal import clear_screen
from asean_phonebook.phonebook.entry.entry import (
    PhonebookEntryCountryCode,
)
from asean_phonebook.phonebook.entry.mocks import MockPhonebookEntry
from asean_phonebook.phonebook.phonebook import Phonebook
from asean_phonebook.program.menu.search import (
    SearchProgramMenu,
    SearchProgramMenuItems,
    SearchProgramMenuSelection,
)


class SearchProgramResult(BaseModel):
    phonebook: Phonebook
    selections: list[SearchProgramMenuSelection]

    def __str__(self):
        lines = [
            self._result_header,
            *self._matching_entries_as_str,
        ]

        return "\n".join(lines)

    @property
    def _result_header(self):
        selection_labels = [
            *SearchProgramMenuItems.gen_labels_from_selections(self.selections)
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


def run_search_program(*, phonebook: Phonebook):
    clear_screen()

    menu = SearchProgramMenu()
    print()

    result = SearchProgramResult(
        phonebook=phonebook,
        selections=menu.selections,
    )
    print(result)
    print()

    input("Press Enter to continue...")


if __name__ == "__main__":
    # test = SearchProgramMenuSelection.ALL
    # print(f"{test=}")
    # print(f"{test.name=}")
    # print(f"{(test.name in PhonebookEntryCountryCode)=}")
    # print(f"{PhonebookEntryCountryCode[test.name]=}")

    # selections = [*SearchProgramMenuSelection]
    # print(f"{selections=}")
    # country_codes = [*gen_country_codes_from_selections(selections)]
    # print(f"{country_codes=}")

    entries = [
        MockPhonebookEntry.JULIANA_DELA_CRUZ,
        MockPhonebookEntry.SAWADI_KRAP,
        MockPhonebookEntry.JOHN_SAINT,
    ]
    random.shuffle(entries)

    phonebook = Phonebook(entries=entries)

    result = SearchProgramResult(
        phonebook=phonebook,
        selections=[*SearchProgramMenuSelection],
    )
    print(result)

    run_search_program(phonebook=phonebook)
