from src.lib.terminal import clear_screen
from src.menu import Menu, MenuAction
from src.phonebook import Phonebook


class Program:
    @classmethod
    def run(cls, *, phonebook: Phonebook):
        while True:
            clear_screen()

            menu = Menu()
            print()

            MenuAction.from_selection(
                menu.selection,
                phonebook=phonebook,
            )


if __name__ == "__main__":
    Program().run(
        phonebook=Phonebook(),
    )
