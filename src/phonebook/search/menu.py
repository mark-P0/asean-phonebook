from enum import IntEnum
from pydantic import BaseModel
from lib.pydantic import enum_input
from lib.python.enum import EnumValues


class PhonebookSearchMenuSelection(EnumValues, IntEnum):
    PHILIPPINES = 1
    THAILAND = 2
    SINGAPORE = 3
    INDONESIA = 4
    MALAYSIA = 5
    ALL = 6
    NO_MORE = 0


class PhonebookSearchMenuItem(BaseModel):
    selection: PhonebookSearchMenuSelection
    label: str


class PhonebookSearchMenuItems:
    items = [
        PhonebookSearchMenuItem(
            selection=PhonebookSearchMenuSelection.PHILIPPINES,
            label="Philippines",
        ),
        PhonebookSearchMenuItem(
            selection=PhonebookSearchMenuSelection.THAILAND,
            label="Thailand",
        ),
        PhonebookSearchMenuItem(
            selection=PhonebookSearchMenuSelection.SINGAPORE,
            label="Singapore",
        ),
        PhonebookSearchMenuItem(
            selection=PhonebookSearchMenuSelection.INDONESIA,
            label="Indonesia",
        ),
        PhonebookSearchMenuItem(
            selection=PhonebookSearchMenuSelection.MALAYSIA,
            label="Malaysia",
        ),
        PhonebookSearchMenuItem(
            selection=PhonebookSearchMenuSelection.ALL,
            label="ALL",
        ),
        PhonebookSearchMenuItem(
            selection=PhonebookSearchMenuSelection.NO_MORE,
            label="No More",
        ),
    ]

    def __str__(self):
        return " ".join(f"[{item.selection}] {item.label}" for item in self.items)

    @classmethod
    def gen_labels_from_selections(
        cls,
        selections: list[PhonebookSearchMenuSelection],
    ):
        for item in cls.items:
            if item.selection in selections:
                yield item.label


class PhonebookSearchMenu:
    def __init__(self):
        self.selections: list[PhonebookSearchMenuSelection] = []

        self.run()

    def __str__(self):
        lines = ["From which country:", str(PhonebookSearchMenuItems())]

        return "\n".join(lines)

    def run(self):
        print(self)

        while True:
            selection_ct = len(self.selections) + 1
            selection = enum_input(
                message=f"Enter choice {selection_ct}: ",
                enum=PhonebookSearchMenuSelection,
            )

            self.selections.append(selection)

            if selection == PhonebookSearchMenuSelection.ALL:
                self.selections = [*PhonebookSearchMenuSelection]  # Select all
                break

            if selection == PhonebookSearchMenuSelection.NO_MORE:
                break

        # Normalize selections
        self.selections = [
            selection
            for selection in set(self.selections)  # Remove duplicates
            # Keep only countries
            if selection != PhonebookSearchMenuSelection.NO_MORE
            and selection != PhonebookSearchMenuSelection.ALL
        ]


if __name__ == "__main__":
    menu = PhonebookSearchMenu()
    print(f"{menu.selections=}")

    labels = [*PhonebookSearchMenuItems.gen_labels_from_selections(menu.selections)]
    print(f"{labels=}")
