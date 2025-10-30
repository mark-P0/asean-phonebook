from enum import Enum, IntEnum
from pydantic import BaseModel

from lib.inflect import possessive_pronoun, with_indefinite_article
from lib.pydantic import enum_input, typed_input
from lib.python.enum import EnumValues


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
        return self.as_edit_str

    @property
    def as_edit_str(self):
        lines = [
            f"Here is the information about {self.student_number}:",
            f"{self.first_name} {self.surname} {self._str_occupation_segment}. {self._str_number_segment}",
        ]

        return "\n".join(lines)

    @property
    def as_search_str(self):
        return f"{self.surname}, {self.first_name}, with student number {self.student_number}, {self._str_occupation_segment}. {self._str_number_segment}"

    @property
    def _str_occupation_segment(self):
        occupation = with_indefinite_article(self.occupation)

        return f"is {occupation}".lower()

    @property
    def _str_number_segment(self):
        pronoun = (
            possessive_pronoun("feminine")
            if self.gender == PhonebookEntryGender.FEMALE
            else possessive_pronoun("masculine")
        )

        return f"{pronoun.title()} number is {self._str_number}"

    @property
    def _str_number(self):
        return "-".join(
            str(num) for num in (self.country_code.value, self.area_code, self.number)
        )

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
