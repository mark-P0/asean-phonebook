from enum import IntEnum

from lib.pydantic import enum_input
from lib.python.enum import EnumValues


class ProgramMenuSelection(EnumValues, IntEnum):
    STORE = 1
    EDIT = 2
    SEARCH = 3
    EXIT = 4


class ProgramMenuItems:
    items = [
        (ProgramMenuSelection.STORE, "Store to ASEAN phonebook"),
        (ProgramMenuSelection.EDIT, "Edit entry in ASEAN phonebook"),
        (ProgramMenuSelection.SEARCH, "Search ASEAN phonebook by country"),
        (ProgramMenuSelection.EXIT, "Exit"),
    ]

    def __str__(self) -> str:
        return "\n".join(f"[{selection}] {text}" for selection, text in self.items)


class ProgramMenu:
    def __init__(self):
        print(ProgramMenuItems())

        self.selection = enum_input(
            message="Selection: ",
            enum=ProgramMenuSelection,
        )


if __name__ == "__main__":
    menu = ProgramMenu()
    print(f"{menu.selection=}")
