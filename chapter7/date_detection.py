import re

date_regex = re.compile(r'^(0?[1-9]|[1-2][0-9|3[0-1])[/.-](0?[1-9]|1[1-2])[/.-](1[0-9]{3}|2[0-9]{3})$')
def detect_date(date):
    match_object = date_regex.search(date)
    day, month, year = match_object.groups()

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_day_value = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_day_value = 30
    elif int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
        max_day_value = 29
    else:
        max_day_value = 28
    
    if int(day) > max_day_value:
        print("Date is invalid.")
    
    print('Date is valid.')

detect_date('29.02.2020')