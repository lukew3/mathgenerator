from .__init__ import *

import math


def decimalToRomanNumeralsFunc(maxDecimal=4000, format='string'):
    x = random.randint(0, maxDecimal)
    roman_dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    divisor = 1
    while x >= divisor:
        divisor *= 10
    divisor /= 10
    solution = ""
    while x:
        last_value = int(x / divisor)
        if last_value <= 3:
            solution += (roman_dict[divisor] * last_value)
        elif last_value == 4:
            solution += (roman_dict[divisor] + roman_dict[divisor * 5])
        elif 5 <= last_value <= 8:
            solution += (roman_dict[divisor * 5] + (roman_dict[divisor] * (last_value - 5)))
        elif last_value == 9:
            solution += (roman_dict[divisor] + roman_dict[divisor * 10])
        x = math.floor(x % divisor)
        divisor /= 10

    if format == 'string':
        problem = "The number " + str(x) + " in Roman Numerals is: "
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return x, solution


decimal_to_roman_numerals = Generator("Converts decimal to Roman Numerals", 85,
                                      decimalToRomanNumeralsFunc,
                                      ["maxDecimal=4000"])
