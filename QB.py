UNITS = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
         'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
DOZENS = ['Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

HUNDRED = 'Hundred'
THOUSAND = 'Thousand'

def get_dozens_units(number):
    dozens = 0
    units = 0
    if number > 0:
        if number < 20:
            units = number
        else:
            dozens = int(number / 10)
            units = number % 10

    return dozens, units

def convert_less_than_hunded_to_str(number):

    dozens, units = get_dozens_units(number)
    result_str = ''

    if (dozens > 0):
        result_str = DOZENS[dozens - 2]

    if (units > 0):
        if result_str != '':
            result_str = result_str + ' ' + UNITS[units]
        else:
            result_str = UNITS[units]

    result_str = result_str.strip()

    return result_str

def convert_number_to_string(number):
    result_str = ''
    thousands = int(number / 1000)
    number = number % 1000
    hundreds = int(number / 100)
    number = number % 100



    thousands_str = convert_less_than_hunded_to_str(thousands)
    if thousands_str != '':
        thousands_str = thousands_str + ' Thousand '

    hundreds_str = convert_less_than_hunded_to_str(hundreds)
    if hundreds_str != '':
        hundreds_str = hundreds_str + ' Hundred '

    left_str = convert_less_than_hunded_to_str(number)

    result_str = thousands_str + hundreds_str + left_str

    return result_str


values = input().split()
a = int(values[0])
b = int(values[1])


if (a == b):
    print(a)
else:
    while True:
        if (a > b):
            a, b = b, a

        str_a = convert_number_to_string(a)
        str_b = convert_number_to_string(b)

        column_a = [a, b]
        column_b = [str_a, str_b]


        if (str_a < str_b):
            column_c = [str_a, str_b]
            column_d = [a, b]
        else:
            column_c = [str_b, str_a]
            column_d = [b, a]



        a = column_a[0] + column_d[0]
        b = column_a[1] + column_d[1]

        if a > 99999 or b > 99999:
            print('Out of bounds', end="")
            break

        if a == b:
            print(a, end="")
            break