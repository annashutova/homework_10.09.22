from datetime import date, timedelta


def make_journal(notes, year, month, day):
    file = open('captains_journal.txt', 'a')
    current_date = date(year, month, day)
    line = '{0}: {1}\n'.format(str(current_date), notes[0])
    file.write(line)
    for i in range(1, len(notes)):
        next_date = current_date + timedelta(days=1)
        line = '{0}: {1}\n'.format(str(next_date), notes[i])
        current_date = next_date
        file.write(line)
    file.close()


make_journal(['first note', 'second note', 'third note', 'fourth note'], 2022, 9, 29)
