from .__init__ import *


def arithmeticProgressionFunc(firstNum=1000, increaseRate=100, elements=100):
    a = random.randint(1, firstNum)
    b = random.randint(1, increaseRate)
    c = random.randint(1, elements)
    list_num = [str(a + b * i) for i in range(5)]
    sum_ = (a + (c-1) * b / 2) * c
    ap_list = ' '.join(list_num)
    problem = "Find the sum of first " + str(c) + \
              " elements of this AP series: " + ap_list
    solution = sum_
    return problem, solution
