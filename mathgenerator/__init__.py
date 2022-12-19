from .funcs import *
from .generator import getGenList

genList = getGenList()


def genById(id, *args, **kwargs):
    generator = genList[id][2]
    return (generator(*args, **kwargs))
