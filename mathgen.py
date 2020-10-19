import random


genList = []


# || Generator class
class Generator:
    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func
        genList.append([id, title, self])

    def __str__(self):
        return str(self.id) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self, **kwargs):
        return self.func(**kwargs)


def isprime(max_a=100):
    a = random.randint(2, max_a)
    problem = a
    if a == 2:
        solution = True
        return (problem, solution)
    if a % 2 == 0:
        solution = False
        return (problem, solution)
    for i in range(3, a // 2 + 1, 2):
        if a % i == 0:
            solution = False
            return (problem, solution)
    solution = True
    return (problem, solution)


is_prime = Generator('isprime', 74, 'a any positive integer',
                     'True/False', isprime)
