def clear_screen():
    """
    AI-suggested alternative to `os.system('cls')`
    """

    print("\033c", end="")
