#!/usr/bin/python3
def roman_to_int(roman_string):
    value_map = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100,
                 "D": 500, "M": 1000}
    sum = 0
    last_digit_val = 0
    if roman_string is None or not isinstance(roman_string, str):
        return sum
    for roman in roman_string[::-1]:
        cur_val = value_map[roman]

        if cur_val >= last_digit_val:
            sum += cur_val
            last_digit_val = cur_val
        else:
            sum -= cur_val
    return sum
