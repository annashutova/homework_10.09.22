"""Counts the percentage of the sublines where are more upper case."""


def check_upper(lines: str) -> str:
    """
    Counts the percentage of the sublines where are more upper case.

    Args:
        lines : str - line with space-separated sublines.

    Returns:
        str - formated string with percentage.
    """
    lines = lines.split()
    upper = 0
    for subline in lines:
        num_up = 0
        for symb in subline:
            if symb.isupper():
                num_up += 1
        if num_up > len(lines) - num_up:
            upper += 1
    return 'Заглавных букв больше в {0}% строк'.format(upper / len(lines) * 100)
