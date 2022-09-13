lines = input().split()
cnt_lines = len(lines)
upper = 0
for line in lines:
    num_up = 0
    num_low = 0
    for symb in line:
        if symb.isupper:
            num_up += 1
        else:
            num_low += 1
    if num_up > num_low:
        upper += 1
print('Заглавных букв больше в {0}% строк'.format(round(cnt_lines/upper*100, 1)))
