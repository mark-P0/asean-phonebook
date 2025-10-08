from enum import IntEnum

from lib.pydantic import enum_input
from lib.python.enum import EnumValues


class MenuSelection(EnumValues, IntEnum):
    STORE = 1
    EDIT = 2
    SEARCH = 3
    EXIT = 4


class MenuItems:
    items = [
        (MenuSelection.STORE, "Store to ASEAN phonebook"),
        (MenuSelection.EDIT, "Edit entry in ASEAN phonebook"),
        (MenuSelection.SEARCH, "Search ASEAN phonebook by country"),
        (MenuSelection.EXIT, "Exit"),
    ]

    def __str__(self) -> str:
        return "\n".join(f"[{selection}] {text}" for selection, text in self.items)


class Menu:
    def __init__(self):
        print(MenuItems())

        self.selection = enum_input(
            message="Selection: ",
            enum=MenuSelection,
        )


if __name__ == "__main__":
    menu = Menu()
    print(f"{menu.selection=}")
