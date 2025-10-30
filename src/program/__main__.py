from phonebook.entry.mocks import MockPhonebookEntry
from phonebook.phonebook import Phonebook
from program.program import Program

entries: None = [
    MockPhonebookEntry.SUKARNO_LEE,
    MockPhonebookEntry.JULIANA_DELA_CRUZ,
    MockPhonebookEntry.SAWADI_KRAP,
    MockPhonebookEntry.JOHN_SAINT,
]

phonebook = Phonebook(entries=entries)

Program().run(phonebook=phonebook)
