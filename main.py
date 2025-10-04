from src.lib.terminal import clear_screen
from src.menu import Menu, MenuAction


class Program:
    def run(self):
        while True:
            clear_screen()

            menu = Menu()
            MenuAction.from_selection(menu.selection)


if __name__ == "__main__":
    Program().run()
