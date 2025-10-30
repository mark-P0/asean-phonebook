from enum import IntEnum
from pydantic import BaseModel
from asean_phonebook.lib.pydantic import enum_input
from asean_phonebook.lib.python.enum import EnumValues


class SearchProgramMenuSelection(EnumValues, IntEnum):
    PHILIPPINES = 1
    THAILAND = 2
    SINGAPORE = 3
    INDONESIA = 4
    MALAYSIA = 5
    ALL = 6
    NO_MORE = 0


class SearchProgramMenuItem(BaseModel):
    selection: SearchProgramMenuSelection
    label: str


class SearchProgramMenuItems:
    items = [
        SearchProgramMenuItem(
            selection=SearchProgramMenuSelection.PHILIPPINES,
            label="Philippines",
        ),
        SearchProgramMenuItem(
            selection=SearchProgramMenuSelection.THAILAND,
            label="Thailand",
        ),
        SearchProgramMenuItem(
            selection=SearchProgramMenuSelection.SINGAPORE,
            label="Singapore",
        ),
        SearchProgramMenuItem(
            selection=SearchProgramMenuSelection.INDONESIA,
            label="Indonesia",
        ),
        SearchProgramMenuItem(
            selection=SearchProgramMenuSelection.MALAYSIA,
            label="Malaysia",
        ),
        SearchProgramMenuItem(
            selection=SearchProgramMenuSelection.ALL,
            label="ALL",
        ),
        SearchProgramMenuItem(
            selection=SearchProgramMenuSelection.NO_MORE,
            label="No More",
        ),
    ]

    def __str__(self):
        return " ".join(f"[{item.selection}] {item.label}" for item in self.items)

    @classmethod
    def gen_labels_from_selections(
        cls,
        selections: list[SearchProgramMenuSelection],
    ):
        for item in cls.items:
            if item.selection in selections:
                yield item.label


class SearchProgramMenu:
    def __init__(self):
        self.selections: list[SearchProgramMenuSelection] = []

        self.run()

    def __str__(self):
        lines = ["From which country:", str(SearchProgramMenuItems())]

        return "\n".join(lines)

    def run(self):
        print(self)

        while True:
            selection_ct = len(self.selections) + 1
            selection = enum_input(
                message=f"Enter choice {selection_ct}: ",
                enum=SearchProgramMenuSelection,
            )

            self.selections.append(selection)

            if selection == SearchProgramMenuSelection.ALL:
                self.selections = [*SearchProgramMenuSelection]  # Select all
                break

            if selection == SearchProgramMenuSelection.NO_MORE:
                break

        # Normalize selections
        self.selections = [
            selection
            for selection in set(self.selections)  # Remove duplicates
            # Keep only countries
            if selection != SearchProgramMenuSelection.NO_MORE
            and selection != SearchProgramMenuSelection.ALL
        ]


if __name__ == "__main__":
    menu = SearchProgramMenu()
    print(f"{menu.selections=}")

    labels = [*SearchProgramMenuItems.gen_labels_from_selections(menu.selections)]
    print(f"{labels=}")
