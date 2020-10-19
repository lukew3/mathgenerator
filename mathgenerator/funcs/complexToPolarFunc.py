from  .__init__ import *

def polar(minRealImaginaryNum = -20, maxRealImaginaryNum = 20):
    num = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum), random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    a= num.real
    b= num.imag
    r = round(math.hypot(a,b), 2)
    theta = round(math.atan2(b,a), 2)
    plr = str(r) + "exp(i" + str(theta) + ")"
    problem = f"rexp(itheta) = "
    solution = plr
    return problem, solution
    