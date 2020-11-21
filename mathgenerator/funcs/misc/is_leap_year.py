from .__init__ import *


def IsLeapYear(minNumber=1900, maxNumber=2099):
    year = random.randint(minNumber, maxNumber)
    problem = "Year " + str(year) + " "
    solution = ""
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                solution = "is a leap year"
            else:
                solution = "is not a leap year"
        else:
            solution = "is a leap year"
    else:
        solution = "is not a leap year"

    return problem, solution


is_leap_year = Generator("Leap Year or Not", 101,
                         "Year y ", "is/not a leap year",
                         IsLeapYear)
# for readme ## | 102 | Leap Year or Not | Year 1964 | is a leap year | is_leap_year |
