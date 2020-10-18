from .__init__ import *


def fibonacciSeriesFunc(minNo=1):
    n = random.randint(minNo,20)

    def createFibList(n):
        l=[]
        for i in range(n):
            if i<2:
                l.append(i)
            else:
                val = l[i-1]+l[i-2]
                l.append(val)
        return l

    fibList=createFibList(n)
    
    problem = "The Fibonacci Series of the first "+str(n)+" numbers is ?"
    solution = fibList
    return problem,solution
