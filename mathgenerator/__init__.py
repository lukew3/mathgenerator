"""
.. include:: ../README.md
"""

from .algebra import *
from .basic_math import *
from .calculus import *
from .computer_science import *
from .geometry import *
from .misc import *
from .statistics import *

from ._gen_list import gen_list


# [funcname, subjectname]
def get_gen_list():
    return gen_list


def gen_by_id(id, *args, **kwargs):
    return globals()[gen_list[id][0]](*args, **kwargs)


# Legacy Functions
def getGenList():
    return gen_list


def genById(id, *args, **kwargs):
    return globals()[gen_list[id][0]](*args, **kwargs)
