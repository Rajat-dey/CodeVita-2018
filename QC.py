MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

digits_allowed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
text = input()
numbers = ''.join(text.split(','))


def update_values(array):
    for i in range(len(array)):
        if (len(array[i]) == 1):
            array[i] = '0' + array[i]

month = [str(month) for month in range(1, 13)]
day = [str(day) for day in range(1, 32)]
hour = [str(hour) for hour in range(0, 24)]
minute = [str(minute) for minute in range(0, 60)]


update_values(month)
update_values(day)
update_values(hour)
update_values(minute)

digits_allowed = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for digit in numbers:
    digits_allowed[digit] += 1

for month_ind in month:

    can_create = True

    for symb in month_ind:
        digits_allowed[symb] -= 1
        if digits_allowed[symb] < 0:
            can_create = False

    if can_create:
        for day_ind in day:

            for symb in day_ind:
                digits_allowed[symb] -= 1
                if digits_allowed[symb] < 0:
                    can_create = False

            if can_create:
                for hour_ind in hour:

                    for symb in hour_ind:
                        digits_allowed[symb] -= 1
                        if digits_allowed[symb] < 0:
                            can_create = False

                    if can_create:
                        for minute_ind in minute:

                            for symb in minute_ind:
                                digits_allowed[symb] -= 1
                                if digits_allowed[symb] < 0:
                                    can_create = False

                            if can_create:
                                result = month_ind + '/' + day_ind + ' ' + hour_ind + ':' + minute_ind

                            for symb in minute_ind:
                                digits_allowed[symb] += 1

                            can_create = True

                    for symb in hour_ind:
                        digits_allowed[symb] += 1

                    can_create = True

            for symb in day_ind:
                digits_allowed[symb] += 1

            can_create = True

    for symb in month_ind:
        digits_allowed[symb] += 1

    can_create = True

try:
    print (result)
except:
    print (0)

