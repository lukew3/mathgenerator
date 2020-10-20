import random
import math
import fractions
from .funcs import *
from .__init__ import getGenList

genList = getGenList()

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
        return str(
            self.id
        ) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


# || Non-generator Functions
def genById(id):
    generator = genList[id][2]
    return (generator())


# Format is:
# <title> = Generator("<Title>", <id>, <generalized problem>, <generalized solution>, <function name>)

