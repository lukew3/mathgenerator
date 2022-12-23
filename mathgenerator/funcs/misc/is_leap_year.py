from ...generator import Generator
import random


def gen_func(minNumber=1900, maxNumber=2099):
    year = random.randint(minNumber, maxNumber)
    problem = f"Is {year} a leap year?"
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                ans = True
            else:
                ans = False
        else:
            ans = True
    else:
        ans = False

    solution = f"{year} is{' not' if not ans else ''} a leap year"
    return problem, solution


is_leap_year = Generator("Leap Year or Not", 101, gen_func,
                         ["minNumber=1900", "maxNumber=2099"])
