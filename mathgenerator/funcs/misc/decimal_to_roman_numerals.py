from ...generator import Generator
import random
import math


def gen_func(maxDecimal=4000):
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
    div = 1
    while x >= div:
        div *= 10
    div /= 10
    solution = ""
    while x:
        last_value = int(x / div)
        if last_value <= 3:
            solution += (roman_dict[div] * last_value)
        elif last_value == 4:
            solution += (roman_dict[div] + roman_dict[div * 5])
        elif 5 <= last_value <= 8:
            solution += (roman_dict[div * 5] + (roman_dict[div] * (last_value - 5)))
        elif last_value == 9:
            solution += (roman_dict[div] + roman_dict[div * 10])
        x = math.floor(x % div)
        div /= 10

    problem = f"The number ${x}$ in Roman Numerals is: "
    return problem, f'${solution}$'


decimal_to_roman_numerals = Generator("Converts decimal to Roman Numerals", 85,
                                      gen_func,
                                      ["maxDecimal=4000"])
