from datetime import date
# count number of Sundays

number_sundays = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        d = date(y, m, 1)
        if d.weekday() == 6:
            number_sundays += 1

print(f'{number_sundays= }')

