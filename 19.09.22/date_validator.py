"""Checks if the input date is valid."""
MONTH30 = (4, 6, 9, 11)
MONTH31 = (1, 3, 5, 7, 8, 10, 12)
FEBRUARY = 2
FEB_DAY = 29
MONTH_WITH31 = 32
MONTH_WITH30 = 31
LEAP_CONDITION = 400


def valid_date(date: str) -> bool:
    """
    Checks if the input date is valid.

    Args:
        date : str - day, month and year of the date.

    Return:
        bool - true if date is valid, else false.
    """
    date = date.split('.')
    try:
        day, month, year = int(date[0]), int(date[1]), int(date[2])
    except Exception:
        return 'Input format: DD.MM.YYYY'
    leap_year = (year % 4 == 0 and year % 100 != 0) or year % LEAP_CONDITION == 0
    leap_date = leap_year and day == FEB_DAY and month == FEBRUARY
    normal30 = month in MONTH30 and day in range(1, MONTH_WITH30)
    normal31 = month in MONTH31 and day in range(1, MONTH_WITH31)
    february = not (leap_year) and month == FEBRUARY and day in range(1, FEB_DAY)
    return leap_date or normal30 or normal31 or february
