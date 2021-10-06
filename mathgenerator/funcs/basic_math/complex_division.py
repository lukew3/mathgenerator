from .__init__ import *


def complexDivisionFunc(maxRes=99, maxDivid=99, format='string'):
    a = random.randint(0, maxDivid)
    b = random.randint(1, min(maxRes, maxDivid))
    c = a / b
    c = round(c, 2)

    if format == "string":
        return (str(a) + "/" + str(b) + "=", str(c))
    elif format == 'latex':
        return ("\\(" + str(a) + "\\div" + str(b) + "=\\)",
                "\\(" + str(c) + "\\)")
    else:
        return a, b, c


complex_division = Generator("Complex Division", 13, complexDivisionFunc,
                             ["maxRes=99", "maxDivid=99"])
