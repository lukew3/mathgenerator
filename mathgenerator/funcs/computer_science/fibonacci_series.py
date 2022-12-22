from ...generator import Generator
import random


def gen_func(minNo=1):
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

    problem = "The Fibonacci Series of the first ${n}$ numbers is ?"
    solution = ', '.join(map(str, fibList))
    return problem, f'${solution}$'


fibonacci_series = Generator("Fibonacci Series", 56, gen_func,
                             ["minNo=1"])
