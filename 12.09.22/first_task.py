def check_upper(line: str) -> str:
    """
    Counts the percentage of the sublines where are more upper case.

    Args:
        line : str - line with space-separated sublines.

    Returns:
        str - formated string with percentage.
    """
    lines = line.split()
    cnt_lines = len(lines)
    upper = 0
    for line in lines:
        num_up = 0
        num_low = 0
        for symb in line:
            if symb.isupper():
                num_up += 1
            else:
                num_low += 1
        if num_up > num_low:
            upper += 1
    return 'Заглавных букв больше в {0}% строк'.format(upper / cnt_lines * 100)
