import random
import math
import fractions
from .funcs import *
from .__init__ import getGenList
import scipy

genList = getGenList()


# || Non-generator Functions
def genById(id):
    generator = genList[id][2]
    return (generator())
