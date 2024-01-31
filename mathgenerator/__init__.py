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

def generate_context(seed = None):
    if seed is not None:
        random.seed(seed)
    choice = random.choice(gen_list)
    _ = globals()[choice[0]]()
    problem, solution = _[0], _[1]
    if len(_) == 3:
        forward_words = _[2]
    else:
        forward_words = []
    forward_words.extend(choice[0].split('_')).extend(choice[1].split('_'))
    problem = str(problem)
    solution = str(solution)
    try:
        # See if the solution is a float
        float(solution.replace('$', ''))
        return {
            "problem": problem,
            "solution": solution.replace('$', ''),
            "reward_type": 'float',
            'topic': choice[1],
            'subtopic': choice[0],
            'forward_words': forward_words
        }
    except:
        if solution.lower().replace('$', '') in ['yes', 'no']:
            return {
                "problem": problem,
                "solution": solution.replace('$', ''),
                "reward_type": 'binary',
                'topic': choice[1],
                'subtopic': choice[0],
                'forward_words': forward_words
            }
        return {
            "problem": problem,
            "solution": solution,
            "reward_type": 'string',
            'topic': choice[1],
            'subtopic': choice[0],
            'forward_words': forward_words
        }
