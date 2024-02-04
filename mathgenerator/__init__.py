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

def generate_context(seed = None, question_type = None, question_kwargs = None):
    if seed is not None:
        random.seed(seed)
    choice = random.choice(gen_list)
    if question_type is not None:
        generation = globals()[question_type](**question_kwargs)
    else:
        generation = globals()[choice[0]]()
    problem, solution = generation[0], generation[1]
    # If the function returns 3 values, the third value is the forward words
    if len(generation) == 3:
        forward_words = generation[2]
    # Otherwise, we instantiate it as an empty list
    else:
        forward_words = []
    # Add the forward words from the subtopic and topic
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
