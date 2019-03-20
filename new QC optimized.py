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
    digits_allowed[digit] += 1           # checking all th digits one by one

for month_ind in month:     #month_ind is the monthly index which is to be check one by one

    can_create = True			#checking we can create or not  False denote that we can't create the number

    for symb in month_ind:                     #checking the month first so that if no result comes then terminating the problem in that phase
        digits_allowed[symb] -= 1				# checking the possibility of dates from smaller to higher one
        if digits_allowed[symb] < 0:			#it is used to check the dublicate values and making an exception when there is less no. of digits present in the digits_allowed
            can_create = False

			# Here symb is used as symbols for the respective month and so on all the days,hrs, min
			
    if can_create:
        for i in range(0, MONTH_DAYS[int(month_ind) - 1]): 				#-1 is done for not completing the 12 months

            day_ind = day[i]											# similarly for days
            for symb in day_ind:
                digits_allowed[symb] -= 1
                if digits_allowed[symb] < 0:
                    can_create = False

            if can_create:
                for hour_ind in hour:										# for checking the hours

                    for symb in hour_ind:									#checking hte symbol in the hour index by minusing the number if condition get false then the last loop after the result get succeed which add the number in the list and can_create=true get executed
                        digits_allowed[symb] -= 1
                        if digits_allowed[symb] < 0:
                            can_create = False

                    if can_create:
                        for minute_ind in minute:							#for checking the minutes

                            for symb in minute_ind:
                                digits_allowed[symb] -= 1
                                if digits_allowed[symb] < 0:
                                    can_create = False

                            if can_create:
                                result = month_ind + '/' + day_ind + ' ' + hour_ind + ':' + minute_ind        #if everything is alright and true for the best possibiity the bring the output in the desired format

                            for symb in minute_ind:
                                digits_allowed[symb] += 1				#now checking the number while adding in every iteration in hte loop of respective min,hour,day,month

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
    print (result, end="")
except:
    print (0, end="")