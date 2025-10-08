from enum import IntEnum

from lib.python.iterables import transpose_2d
from lib.python.enum import EnumValues


class PhonebookEntryEditMenuSelection(EnumValues, IntEnum):
    STUDENT_NUMBER = 1
    SURNAME = 2
    GENDER = 3
    OCCUPATION = 4
    COUNTRY_CODE = 5
    AREA_CODE = 6
    PHONE_NUMBER = 7
    NONE = 8


class PhonebookEntryEditMenuItems:
    rows = 3
    cols = 3

    items = [
        (PhonebookEntryEditMenuSelection.STUDENT_NUMBER, "Student number"),
        (PhonebookEntryEditMenuSelection.SURNAME, "Surname"),
        (PhonebookEntryEditMenuSelection.GENDER, "Gender"),
        (PhonebookEntryEditMenuSelection.OCCUPATION, "Occupation"),
        (PhonebookEntryEditMenuSelection.COUNTRY_CODE, "Country code"),
        (PhonebookEntryEditMenuSelection.AREA_CODE, "Area code"),
        (PhonebookEntryEditMenuSelection.PHONE_NUMBER, "Phone number"),
        (PhonebookEntryEditMenuSelection.NONE, "None - Back to main menu"),
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

    def __format_item(self, item: tuple[PhonebookEntryEditMenuSelection, str] | None):
        if item is None:
            return ""

        selection, label = item

        return f"[{selection.value}] {label}"

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
            if item[0] == selection:
                return item[1]

        return None


if __name__ == "__main__":
    print(PhonebookEntryEditMenuItems())
