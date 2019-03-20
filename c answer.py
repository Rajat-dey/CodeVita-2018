MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

digits_allowed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


text = input()
numbers = text.split(',')



for month in range(1, 13):
    str_month = str(month)
    if month < 10:
        str_month = '0' + str_month

    for day in range(1, MONTH_DAYS[month - 1]):

        str_day = str(day)
        if day < 10:
            str_day = '0' + str_day

        for hour in range(0, 24):

            str_hour = str(hour)
            if hour < 10:
                str_hour = '0' + str_hour

            for minute in range(0, 60):

                digits_allowed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                for digit in numbers:
                    digits_allowed[int(digit)] += 1

                str_minute = str(minute)
                if minute < 10:
                    str_minute = '0' + str_minute


                can_create = True
                result_str = str_month + str_day + str_hour + str_minute
                for symbol in result_str:
                    digits_allowed[int(symbol)] -= 1

                    if digits_allowed[int(symbol)] < 0:
                        can_create = False
                        break

                if can_create:
                    result = str_month + '/' + str_day + ' ' + str_hour + ':' + str_minute

try:
    print (result)
except:
    print (0)











