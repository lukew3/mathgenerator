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

def generate_float():
    return random.choice(FLOAT_GENERATORS)()

def generate_context(seed = None):
    if seed is not None:
        random.seed(seed)
    choice = random.choice(gen_list)
    problem, solution = globals()[choice[0]]()
    try:
        # See if the solution is a float
        float(solution.replace('$', ''))
        return {
            "problem": problem,
            "solution": solution.replace('$', ''),
            "reward_type": 'float',
            'topic': choice[1],
            'subtopic': choice[0],
        }
    except:
        return {
            "problem": problem,
            "solution": solution,
            "reward_type": 'string',
            'topic': choice[1],
            'subtopic': choice[0],
        }
