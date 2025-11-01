from enum import IntEnum

from pydantic import BaseModel

from asean_phonebook.lib.pydantic import enum_input


class ProgramMenuSelection(IntEnum):
    STORE = 1
    EDIT = 2
    SEARCH = 3
    EXIT = 4


class ProgramMenuItem(BaseModel):
    selection: ProgramMenuSelection
    label: str


class ProgramMenuItems:
    items = [
        ProgramMenuItem(
            selection=ProgramMenuSelection.STORE,
            label="Store to ASEAN phonebook",
        ),
        ProgramMenuItem(
            selection=ProgramMenuSelection.EDIT,
            label="Edit entry in ASEAN phonebook",
        ),
        ProgramMenuItem(
            selection=ProgramMenuSelection.SEARCH,
            label="Search ASEAN phonebook by country",
        ),
        ProgramMenuItem(
            selection=ProgramMenuSelection.EXIT,
            label="Exit",
        ),
    ]

    def __str__(self) -> str:
        return "\n".join(self.__gen_formatted_items())

    def __gen_formatted_items(self):
        for item in self.items:
            yield f"[{item.selection}] {item.label}"


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
