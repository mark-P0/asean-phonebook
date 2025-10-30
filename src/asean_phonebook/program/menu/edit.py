from enum import IntEnum

from pydantic import BaseModel

from asean_phonebook.lib.pydantic import enum_input
from asean_phonebook.lib.python.enum import EnumValues
from asean_phonebook.lib.python.iterables import transpose_2d
from asean_phonebook.phonebook.entry.entry import (
    PhonebookEntry,
)
from asean_phonebook.phonebook.entry.mocks import MockPhonebookEntry


class EditEntryProgramMenuSelection(EnumValues, IntEnum):
    STUDENT_NUMBER = 1
    SURNAME = 2
    GENDER = 3
    OCCUPATION = 4
    COUNTRY_CODE = 5
    AREA_CODE = 6
    PHONE_NUMBER = 7
    NONE = 8


class EditEntryProgramMenuItem(BaseModel):
    selection: EditEntryProgramMenuSelection
    label: str


class EditEntryProgramMenuItems:
    rows = 3
    cols = 3

    items = [
        EditEntryProgramMenuItem(
            selection=EditEntryProgramMenuSelection.STUDENT_NUMBER,
            label="Student number",
        ),
        EditEntryProgramMenuItem(
            selection=EditEntryProgramMenuSelection.SURNAME,
            label="Surname",
        ),
        EditEntryProgramMenuItem(
            selection=EditEntryProgramMenuSelection.GENDER,
            label="Gender",
        ),
        EditEntryProgramMenuItem(
            selection=EditEntryProgramMenuSelection.OCCUPATION,
            label="Occupation",
        ),
        EditEntryProgramMenuItem(
            selection=EditEntryProgramMenuSelection.COUNTRY_CODE,
            label="Country code",
        ),
        EditEntryProgramMenuItem(
            selection=EditEntryProgramMenuSelection.AREA_CODE,
            label="Area code",
        ),
        EditEntryProgramMenuItem(
            selection=EditEntryProgramMenuSelection.PHONE_NUMBER,
            label="Phone number",
        ),
        EditEntryProgramMenuItem(
            selection=EditEntryProgramMenuSelection.NONE,
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

    def __format_item(self, item: EditEntryProgramMenuItem | None):
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
    def get_label_from_selection(cls, selection: EditEntryProgramMenuSelection):
        for item in cls.items:
            if item.selection == selection:
                return item.label

        return None


class EditEntryProgramMenu:
    def __init__(self, entry: PhonebookEntry):
        print(entry)
        print(EditEntryProgramMenuItems())

        self.selection = enum_input(
            message="Enter choice: ",
            enum=EditEntryProgramMenuSelection,
        )


if __name__ == "__main__":
    menu = EditEntryProgramMenu(entry=MockPhonebookEntry.SUKARNO_LEE)

    print(f"{menu.selection=}")
