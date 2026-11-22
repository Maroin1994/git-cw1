# Notatnik – prosty program konsolowy do nauki Gita.

# Lista przechowująca dodane notatki.
notes = []


def add_note(text):
    """Dodaje notatkę do listy."""
    notes.append(text)


def count_notes():
    """Zwraca liczbę zapisanych notatek."""
    return len(notes)


def main():
    """Punkt wejścia programu."""
    print("Witaj w aplikacji Notatnik")
    add_note("pierwsza notatka")
    print("Liczba notatek:", count_notes())


if __name__ == "__main__":
    main()
