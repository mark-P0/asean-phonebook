from phonebook import Phonebook
from phonebook.entry.mocks import MockPhonebookEntry
from program import Program

entries: None = [
    MockPhonebookEntry.SUKARNO_LEE,
    MockPhonebookEntry.JULIANA_DELA_CRUZ,
    MockPhonebookEntry.SAWADI_KRAP,
    MockPhonebookEntry.JOHN_SAINT,
]

phonebook = Phonebook(entries=entries)

Program().run(phonebook=phonebook)
