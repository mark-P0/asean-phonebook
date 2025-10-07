from enum import Enum, IntEnum
from pydantic import BaseModel

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


class PhonebookEntry(BaseModel):
    student_number: str
    surname: str
    first_name: str
    occupation: str
    gender: PhonebookEntryGender
    country_code: PhonebookEntryCountryCode
    area_code: int
    number: int

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


class Phonebook(BaseModel):
    entries: list[PhonebookEntry] = []


if __name__ == "__main__":
    entry = PhonebookEntry.from_prompt()
    print(f"{entry=}")

    # gender = enum_input(
    #     message="Enter gender (M for male, F for female): ",
    #     enum=PhonebookEntryGender,
    # )
    # print(f"{gender=}")

    # country_code = enum_input(
    #     message="Enter country code: ",
    #     enum=PhonebookEntryCountryCode,
    # )
    # print(f"{country_code=}")
