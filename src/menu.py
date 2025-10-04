from enum import IntEnum
import sys
from pydantic import BaseModel, ValidationError


class MenuSelection(IntEnum):
    STORE = 1
    EDIT = 2
    SEARCH = 3
    EXIT = 4


class MenuAction:
    @classmethod
    def from_selection(cls, selection: MenuSelection):
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


class Menu(BaseModel):
    selection: MenuSelection

    @classmethod
    def from_prompt(cls, prompt_text="Selection: "):
        while True:
            try:
                print(MenuItems())
                selection = input(prompt_text)

                return cls.model_validate(dict(selection=selection))
            except ValidationError:
                print("Invalid selection, please try again.")
                print()


if __name__ == "__main__":
    menu = Menu.from_prompt()
    print(f"{menu=}")
