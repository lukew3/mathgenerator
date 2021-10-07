from .__init__ import *


def gen_func(minNumber=1900, maxNumber=2099, format='string'):
    year = random.randint(minNumber, maxNumber)
    problem = "Year " + str(year) + " "
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

    if format == 'string':
        if ans:
            solution = "is a leap year"
        else:
            solution = "is not a leap year"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return year, ans


is_leap_year = Generator("Leap Year or Not", 101, gen_func,
                         ["minNumber=1900", "maxNumber=2099"])
