def valid_date(date):
    date = date.split('.')
    try:
        day, month, year = int(date[0]), int(date[1]), int(date[2])
    except Exception:
        return 'Input format: DD.MM.YYYY'
    leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    leap_date = leap_year and day == 29 and month == 2
    normal_30 = month in (4, 6, 9, 11) and day in range(1, 31)
    normal_31 = month in (1, 3, 5, 7, 8, 10, 12) and day in range(1, 32)
    february = not (leap_year) and month == 2 and day in range(1, 29)
    return leap_date or normal_30 or normal_31 or february
