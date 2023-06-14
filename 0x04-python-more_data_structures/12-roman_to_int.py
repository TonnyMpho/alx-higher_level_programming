#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0;

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0
    value = 0

    for i in reversed(roman_string):
        n = roman_values.get(i, 0)

        if n < value:
            num -= n
        else:
            num += n
            value = n

    return num
        
