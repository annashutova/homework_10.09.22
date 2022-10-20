"""Writes lines of the list into the file with date marks."""
from datetime import date, timedelta


def make_journal(notes: list, year: int, month: int, day: int) -> None:
    """
    Writes lines of the list into the file with date marks.

    Args:
        notes : list - list of the capitan's notes.
        year : int - initial year .
        month : int - initial month.
        day : int - initial day.
    """
    with open('captains_journal.txt', 'a') as journal:
        current_date = date(year, month, day)
        line = '{0}: {1}\n'.format(str(current_date), notes[0])
        journal.write(line)
        for index in enumerate(notes, start=1):
            next_date = current_date + timedelta(days=1)
            line = '{0}: {1}\n'.format(str(next_date), notes[index])
            current_date = next_date
            journal.write(line)
