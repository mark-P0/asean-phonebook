from enum import Enum, IntEnum
from pydantic import BaseModel

from src.lib.python.iterables import transpose_2d
from src.lib.inflect import possessive_pronoun, with_indefinite_article
from src.lib.pydantic import enum_input, typed_input
from src.lib.python.enum import EnumValues


class PhonebookEntryGender(EnumValues, Enum):
    MALE = "M"
    FEMALE = "F"


class PhonebookEntryCountryCode(EnumValues, IntEnum):
    MALAYSIA = 60
    INDONESIA = 62
    PHILIPPINES = 63
    SINGAPORE = 65
    THAILAND = 66


class PhonebookEntryRepeat(EnumValues, Enum):
    YES = "Y"
    NO = "N"


class PhonebookEntryEditSelection(EnumValues, IntEnum):
    STUDENT_NUMBER = 1
    SURNAME = 2
    GENDER = 3
    OCCUPATION = 4
    COUNTRY_CODE = 5
    AREA_CODE = 6
    PHONE_NUMBER = 7
    NONE = 8


class PhonebookEntryEditItems:
    rows = 3
    cols = 3

    items = [
        (PhonebookEntryEditSelection.STUDENT_NUMBER, "Student number"),
        (PhonebookEntryEditSelection.SURNAME, "Surname"),
        (PhonebookEntryEditSelection.GENDER, "Gender"),
        (PhonebookEntryEditSelection.OCCUPATION, "Occupation"),
        (PhonebookEntryEditSelection.COUNTRY_CODE, "Country code"),
        (PhonebookEntryEditSelection.AREA_CODE, "Area code"),
        (PhonebookEntryEditSelection.PHONE_NUMBER, "Phone number"),
        (PhonebookEntryEditSelection.NONE, "None - Back to main menu"),
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

    def __format_item(self, item: tuple[PhonebookEntryEditSelection, str] | None):
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
    def get_label_from_selection(cls, selection: PhonebookEntryEditSelection):
        for item in cls.items:
            if item[0] == selection:
                return item[1]

        return None


class PhonebookEntry(BaseModel):
    student_number: str
    surname: str
    first_name: str
    occupation: str
    gender: PhonebookEntryGender
    country_code: PhonebookEntryCountryCode
    area_code: int
    number: int

    def __str__(self) -> str:
        occupation = with_indefinite_article(self.occupation)
        pronoun = (
            possessive_pronoun("feminine")
            if self.gender == PhonebookEntryGender.FEMALE
            else possessive_pronoun("masculine")
        )
        number = "-".join(
            str(num) for num in (self.country_code.value, self.area_code, self.number)
        )

        lines = [
            f"Here is the information about {self.student_number}:",
            f"{self.first_name} {self.surname} is {occupation}. {pronoun.title()} number is {number}",
        ]

        return "\n".join(lines)

    @classmethod
    def from_prompt(cls):
        student_number = input("Enter student number: ")
        surname = input("Enter surname: ")
        first_name = input("Enter first name: ")
        occupation = input("Enter occupation: ")

        gender = enum_input(
            message="Enter gender (M for male, F for female): ",
            enum=PhonebookEntryGender,
        )

        country_code = enum_input(
            message="Enter country code: ",
            enum=PhonebookEntryCountryCode,
        )

        area_code = typed_input(message="Enter area code: ", _type=int)
        number = typed_input(message="Enter number: ", _type=int)

        model_dict = dict(
            student_number=student_number,
            surname=surname,
            first_name=first_name,
            occupation=occupation,
            gender=gender,
            country_code=country_code,
            area_code=area_code,
            number=number,
        )

        return cls.model_validate(model_dict)


if __name__ == "__main__":
    print(PhonebookEntryEditItems())

# if __name__ == "__main__":
#     entry = PhonebookEntry.from_prompt()
#     print(f"{entry=}")

# if __name__ == "__main__":
#     gender = enum_input(
#         message="Enter gender (M for male, F for female): ",
#         enum=PhonebookEntryGender,
#     )
#     print(f"{gender=}")
#
#     country_code = enum_input(
#         message="Enter country code: ",
#         enum=PhonebookEntryCountryCode,
#     )
#     print(f"{country_code=}")
