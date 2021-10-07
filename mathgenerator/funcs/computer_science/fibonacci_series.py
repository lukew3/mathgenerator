from .__init__ import *


def gen_func(minNo=1, format='string'):
    n = random.randint(minNo, 20)

    def createFibList(n):
        list = []
        for i in range(n):
            if i < 2:
                list.append(i)
            else:
                val = list[i - 1] + list[i - 2]
                list.append(val)
        return list

    fibList = createFibList(n)

    if format == 'string':
        problem = "The Fibonacci Series of the first " + str(
            n) + " numbers is ?"
        return problem, fibList
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return n, fibList


fibonacci_series = Generator("Fibonacci Series", 56, gen_func,
                             ["minNo=1"])
