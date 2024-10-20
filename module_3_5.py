def get_multiplied_digits(number):
    str_number = str(number)
    #str_number = get_multiplied_digits(str(number))
    first = int(str_number[0])

    if len(str_number) <= 1:
        return str_number[0:]
        # return int(str_number[0:])
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
        #return first

print(get_multiplied_digits(40203))