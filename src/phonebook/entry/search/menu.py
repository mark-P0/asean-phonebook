from enum import IntEnum
from pydantic import BaseModel
from lib.pydantic import enum_input
from lib.python.enum import EnumValues


class PhonebookEntrySearchMenuSelection(EnumValues, IntEnum):
    PHILIPPINES = 1
    THAILAND = 2
    SINGAPORE = 3
    INDONESIA = 4
    MALAYSIA = 5
    ALL = 6
    NO_MORE = 0


class PhonebookEntrySearchMenuItem(BaseModel):
    selection: PhonebookEntrySearchMenuSelection
    label: str


class PhonebookEntrySearchMenuItems:
    items = [
        PhonebookEntrySearchMenuItem(
            selection=PhonebookEntrySearchMenuSelection.PHILIPPINES,
            label="Philippines",
        ),
        PhonebookEntrySearchMenuItem(
            selection=PhonebookEntrySearchMenuSelection.THAILAND,
            label="Thailand",
        ),
        PhonebookEntrySearchMenuItem(
            selection=PhonebookEntrySearchMenuSelection.SINGAPORE,
            label="Singapore",
        ),
        PhonebookEntrySearchMenuItem(
            selection=PhonebookEntrySearchMenuSelection.INDONESIA,
            label="Indonesia",
        ),
        PhonebookEntrySearchMenuItem(
            selection=PhonebookEntrySearchMenuSelection.MALAYSIA,
            label="Malaysia",
        ),
        PhonebookEntrySearchMenuItem(
            selection=PhonebookEntrySearchMenuSelection.ALL,
            label="ALL",
        ),
        PhonebookEntrySearchMenuItem(
            selection=PhonebookEntrySearchMenuSelection.NO_MORE,
            label="No More",
        ),
    ]

    def __str__(self):
        return " ".join(f"[{item.selection}] {item.label}" for item in self.items)

    @classmethod
    def gen_labels_from_selections(
        cls,
        selections: list[PhonebookEntrySearchMenuSelection],
    ):
        for item in cls.items:
            if item.selection in selections:
                yield item.label


class PhonebookEntrySearchMenu:
    def __init__(self):
        self.selections: list[PhonebookEntrySearchMenuSelection] = []

        self.run()

    def __str__(self):
        lines = ["From which country:", str(PhonebookEntrySearchMenuItems())]

        return "\n".join(lines)

    def run(self):
        print(self)

        while True:
            selection_ct = len(self.selections) + 1
            selection = enum_input(
                message=f"Enter choice {selection_ct}: ",
                enum=PhonebookEntrySearchMenuSelection,
            )

            self.selections.append(selection)

            if selection == PhonebookEntrySearchMenuSelection.ALL:
                self.selections = [*PhonebookEntrySearchMenuSelection]  # Select all
                break

            if selection == PhonebookEntrySearchMenuSelection.NO_MORE:
                break

        # Normalize selections
        self.selections = [
            selection
            for selection in set(self.selections)  # Remove duplicates
            # Keep only countries
            if selection != PhonebookEntrySearchMenuSelection.NO_MORE
            and selection != PhonebookEntrySearchMenuSelection.ALL
        ]


if __name__ == "__main__":
    menu = PhonebookEntrySearchMenu()
    print(f"{menu.selections=}")

    labels = [
        *PhonebookEntrySearchMenuItems.gen_labels_from_selections(menu.selections)
    ]
    print(f"{labels=}")
