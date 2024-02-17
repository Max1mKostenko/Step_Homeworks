def is_leap_year(year):
    """
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_difference(year1, month1, day1, year2, month2, day2):

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year1):
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28

    days1 = day1
    for m in range(month1 - 1):
        days1 += days_in_month[m]
    if is_leap_year(year2):
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28

    days2 = day2
    for m in range(month2 - 1):
        days2 += days_in_month[m]

    days_diff = abs(days2 - days1)
    leap_years = sum(1 for y in range(min(year1, year2), max(year1, year2) + 1) if is_leap_year(y))

    if year1 < year2:
        days_diff += leap_years
    elif year1 > year2:
        days_diff -= leap_years

    return days_diff


date1 = (2023, 2, 17)
date2 = (2024, 2, 17)
difference = days_difference(*date1, *date2)
print(f"Разность в днях между {date1} и {date2} составляет {difference} дней.")
