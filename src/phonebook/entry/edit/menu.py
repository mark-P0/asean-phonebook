from enum import IntEnum

from pydantic import BaseModel

from lib.pydantic import enum_input
from lib.python.iterables import transpose_2d
from lib.python.enum import EnumValues
from phonebook.entry import (
    PhonebookEntry,
    PhonebookEntryCountryCode,
    PhonebookEntryGender,
)


class PhonebookEntryEditMenuSelection(EnumValues, IntEnum):
    STUDENT_NUMBER = 1
    SURNAME = 2
    GENDER = 3
    OCCUPATION = 4
    COUNTRY_CODE = 5
    AREA_CODE = 6
    PHONE_NUMBER = 7
    NONE = 8


class PhonebookEntryEditMenuItem(BaseModel):
    selection: PhonebookEntryEditMenuSelection
    label: str


class PhonebookEntryEditMenuItems:
    rows = 3
    cols = 3

    items = [
        PhonebookEntryEditMenuItem(
            selection=PhonebookEntryEditMenuSelection.STUDENT_NUMBER,
            label="Student number",
        ),
        PhonebookEntryEditMenuItem(
            selection=PhonebookEntryEditMenuSelection.SURNAME,
            label="Surname",
        ),
        PhonebookEntryEditMenuItem(
            selection=PhonebookEntryEditMenuSelection.GENDER,
            label="Gender",
        ),
        PhonebookEntryEditMenuItem(
            selection=PhonebookEntryEditMenuSelection.OCCUPATION,
            label="Occupation",
        ),
        PhonebookEntryEditMenuItem(
            selection=PhonebookEntryEditMenuSelection.COUNTRY_CODE,
            label="Country code",
        ),
        PhonebookEntryEditMenuItem(
            selection=PhonebookEntryEditMenuSelection.AREA_CODE,
            label="Area code",
        ),
        PhonebookEntryEditMenuItem(
            selection=PhonebookEntryEditMenuSelection.PHONE_NUMBER,
            label="Phone number",
        ),
        PhonebookEntryEditMenuItem(
            selection=PhonebookEntryEditMenuSelection.NONE,
            label="None - Back to main menu",
        ),
    ]

    def __str__(self) -> str:
        matrix_lines = self.__get_formatted_matrix_lines()

        lines = [
            "Which of the following information do you wish to change?",
            "",
            *matrix_lines,
        ]

        return "\n".join(lines)

    def __gen_matrix_col_items(self, col_idx: int):
        for row_idx in range(self.rows):
            idx = row_idx + (self.rows * col_idx)

            try:
                yield self.items[idx]
            except IndexError:
                yield None

    def __gen_matrix_cols(self):
        for col_idx in range(self.cols):
            yield [*self.__gen_matrix_col_items(col_idx)]

    def __format_item(self, item: PhonebookEntryEditMenuItem | None):
        if item is None:
            return ""

        return f"[{item.selection.value}] {item.label}"

    def __gen_formatted_matrix_cols(self):
        for col in self.__gen_matrix_cols():
            formatted_items = [self.__format_item(item) for item in col]
            longest_item = max(formatted_items, key=len)
            longest_item_len = len(longest_item)

            formatted_col = [item.ljust(longest_item_len) for item in formatted_items]

            yield formatted_col

    def __gen_matrix(self):
        matrix = transpose_2d(self.__gen_formatted_matrix_cols())

        return matrix

    def __get_formatted_matrix_lines(self, *, sep=" "):
        matrix = self.__gen_matrix()
        lines = [sep.join(row) for row in matrix]

        return lines

    @classmethod
    def get_label_from_selection(cls, selection: PhonebookEntryEditMenuSelection):
        for item in cls.items:
            if item.selection == selection:
                return item.label

        return None


class PhonebookEntryEditMenu:
    def __init__(self, entry: PhonebookEntry):
        print(entry)
        print(PhonebookEntryEditMenuItems())

        self.selection = enum_input(
            message="Enter choice: ",
            enum=PhonebookEntryEditMenuSelection,
        )


if __name__ == "__main__":
    menu = PhonebookEntryEditMenu(
        entry=PhonebookEntry(
            student_number="2004-56",
            surname="Lee",
            first_name="Sukarno",
            occupation="Doctor",
            gender=PhonebookEntryGender.MALE,
            country_code=PhonebookEntryCountryCode.PHILIPPINES,
            area_code=2,
            number=4567890,
        )
    )

    print(f"{menu.selection=}")
