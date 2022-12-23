import random


def is_leap_year(minNumber=1900, maxNumber=2099):
    """Is Leap Year or Not"""
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
