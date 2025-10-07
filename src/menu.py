from enum import IntEnum
import sys

from src.lib.pydantic import enum_input
from src.lib.python.enum import EnumValues
from src.phonebook import Phonebook


class MenuSelection(EnumValues, IntEnum):
    STORE = 1
    EDIT = 2
    SEARCH = 3
    EXIT = 4


class MenuAction:
    @classmethod
    def from_selection(cls, selection: MenuSelection, *, phonebook: Phonebook):
        if selection == MenuSelection.STORE:
            phonebook.store_new_entry()

        if selection == MenuSelection.EXIT:
            sys.exit(1)


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
