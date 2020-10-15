import random

# || Generator class

class Generator:
    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func

    def __str__(self):
        return str(self.id) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self):
        return self.func()


# || Functions

def additionFunc(maxSum = 99, maxAddend = 50):
    a = random.randint(0, maxAddend)
    b = random.randint(0, min((maxSum-a), maxAddend)) #The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    c = a+b
    problem = str(a) + "+" + str(b) + "="
    solution = str(c)
    return problem, solution

def subtractionFunc(maxMinuend = 99, maxDiff = 99):
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a-maxDiff)), a)
    c = a-b
    problem = str(a) + "-" + str(b) + "="
    solution = str(c)
    return problem, solution

def multiplicationFunc(maxRes = 99, maxMulti = 99):
    a = random.randint(0, maxMulti)
    b = random.randint(0, min(int(maxMulti/a), maxRes))
    c = a*b
    problem = str(a) + "*" + str(b) + "="
    solution = str(c)
    return problem, solution

def divisionFunc(maxRes = 99, maxDivid = 99):
    a = random.randint(0, maxDivid)
    b = random.randint(0, min(maxRes, maxDivid))
    c = a/b
    problem = str(a) + "/" + str(b) + "="
    solution = str(c)
    return problem, solution

def binaryComplement1sFunc(maxDigits = 10):
    question = ''
    answer = ''    
    for i in range(random.randint(1,maxDigits)): 
        temp = str(random.randint(0, 1)) 
        question += temp
        answer += "0" if temp == "1" else "1" 
   
    problem = question    
    solution = answer
    return problem, solution

def moduloFunc(maxRes = 99, maxModulo= 99):
    a = random.randint(0, maxModulo)
    b = random.randint(0, min(maxRes, maxModulo))
    c = a%b
    problem = str(a) + "%" + str(b) + "="
    solution = str(c)
    return problem, solution

def squareRootFunction(minNo = 1, maxNo = 12):
    b = random.randint(minNo, maxNo)
    a = b*b
    problem = "sqrt(" + str(a) + ")="
    solution = str(b)
    return problem, solution

# || Class Instances

#Format is:
#<title> = Generator("<Title>", <id>, <generalized problem>, <generalized solution>, <function name>)
addition = Generator("Addition", 2, "a+b=", "c", additionFunc)
subtraction = Generator("Subtraction", 3, "a-b=", "c", subtractionFunc)
multiplication = Generator("Multiplication", 4, "a*b=", "c", multiplicationFunc)
division = Generator("Division", 5, "a/b=", "c", divisionFunc)
binaryComplement1s = Generator("binary_complement_1s", 6, "1010=", "0101", binaryComplement1sFunc)
moduloDivision = Generator("Modulo_Division", 7, "a%b=", "c", moduloFunc)
squareRoot = Generator("Square _Root", 8, "sqrt(a)=", "b", squareRootFunction)
