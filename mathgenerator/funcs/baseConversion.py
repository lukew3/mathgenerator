from  .__init__ import *

#base from 2 to 36
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def fromBaseTenTo(n,toBase):
    assert toBase<=36, "{} should be at most 36"
    if toBase==2:
        return bin(n)[2:]
    elif toBase==8:
        return oct(n)[2:]
    elif toBase==10:
        return str(n)
    elif toBase==16:
        return hex(n)[2:].upper()
    res = alpha[n%toBase]
    n = n//toBase
    while n>0:
        res = alpha[n%toBase] + res
        n = n//toBase
    return res

# Useful to check answers, but not needed here
# def toBaseTen(n,fromBase):
#     assert fromBase<=36, "{} should be at most 36"
#     return int(n,fromBase)

def baseConversion(maxNum = 60000, maxBase = 16):
    assert type(maxNum)==int and maxNum>=100 and maxNum<=65536, "maxNum({}) should be an int between 100 and 65536".format(maxNum)
    assert type(maxBase)==int and maxBase>=2 and maxBase<=36, "maxBase({}) sholud be an int between 2 and 36 (inclusive)".format(maxBase)
    
    n = random.randint(40,maxNum)
    dist = [10]*10+[2]*5+[16]*5+[i for i in range(2,maxBase+1)]
    # set this way since converting to/from bases 2,10,16 are more common -- can be changed if needed.
    bases = random.choices(dist,k=2)
    while bases[0]==bases[1]:
        bases = random.choices(dist,k=2)
    
    problem = "Convert {} from base {} to base {}.".format(fromBaseTenTo(n,bases[0]),bases[0],bases[1])
    ans = fromBaseTenTo(n,bases[1])
    return problem, ans
    
