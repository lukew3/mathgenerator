from .funcs import *
from .__init__ import getGenList

genList = getGenList()


# || Non-generator Functions
def genById(id, *args, **kwargs):
    generator = genList[id][2]
    return (generator(*args, **kwargs))
