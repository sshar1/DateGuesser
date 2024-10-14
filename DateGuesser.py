# Date Guesser

from datetime import date
import math
import random

max_days = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]

# Use indeces that support datetime
weekdays_datetime = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

# Use indeces that support the formula
weekdays_formula = [
    'Saturday',
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
]

year_codes = {
    1700 : 4,
    1800 : 2,
    1900 : 0,
    2000 : 6
}

month_codes = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

def is_leap_year(year):
    if not year % 4 == 0: return False
    if not year % 100 == 0: return True
    if year % 100 == 0: return True
    return False

def show_steps(d):
    year_remainder = math.floor((d.year % 100) / 4)
    year_code = year_codes[d.year - (d.year % 100)]
    month_code = month_codes[d.month-1]
    subtracted_month_code = False
    if (is_leap_year(d.year) and (d.month == 1 or d.month == 2)): 
        month_code -= 1
        subtracted_month_code = True

    year_sum = d.year % 100 + year_remainder + year_code

    weekday_code = (d.day + year_sum + month_code) % 7

    print('Year remainder: ' + str(d.year % 100) + '/' + '4' + ' = ' + str(d.year % 100 / 4) + ' -> ' + str(year_remainder))
    print('Year code: ' + str(d.year - (d.year % 100)) + ' -> ' + str(year_code))
    print('Year sum: ' + str(d.year % 100) + ' + ' + str(year_remainder) + ' + ' + str(year_code) +  ' = ' + str(year_sum))
    print('Add day: ' + str(d.day) + ' + ' + str(year_sum) + ' = ' + str(d.day + year_sum))
    print('Add month code: ' + str(month_code) + ' + ' + str(d.day + year_sum) + ' = ' + str(d.day + year_sum + month_code))
    if subtracted_month_code: print('(Subtracted 1 because of leap year)')
    print('Mod 7: ' + str(d.day + year_sum + month_code) + ' mod 7 = ' + str((d.day + year_sum + month_code) % 7))
    print(str((d.day + year_sum + month_code) % 7) + ' -> ' + weekdays_formula[weekday_code])



while True:
    year = random.randint(1700, 2099)
    month = random.randint(1, 12)
    if month == 2 and is_leap_year(year):
        max_days[1] = 29
    else:
        max_days[1] = 28
    day = random.randint(1, max_days[month-1])

    d = date(year, month, day)

    print(d.strftime("%B %d, %Y"))

    ans = input()
    if ans.lower() == weekdays_datetime[d.weekday()].lower():
        print("Correct!")
    else: 
        print("The answer was " + weekdays_datetime[d.weekday()])
        print("~~How To Solve~~\n")
        show_steps(d)

    response = input('Press enter to continue or enter stop to stop playing\n')

    if response.lower() == 'stop': break
    print()
