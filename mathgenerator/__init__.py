import sys
import traceback

import random
import sympy
import numpy
import scipy

genList = []


class Generator:
    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func

        (filename, line_number, function_name,
         text) = traceback.extract_stack()[-2]
        funcname = filename[filename.rfind('/'):].strip()
        funcname = funcname[1:-3]
        subjectname = filename[:filename.rfind('/')].strip()
        subjectname = subjectname[subjectname.rfind('/'):].strip()
        subjectname = subjectname[1:]
        genList.append([id, title, self, funcname, subjectname])

    def __str__(self):
        return str(
            self.id
        ) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except TypeError:
            # If an error is thrown from kwargs, remove the style element
            # This happens if someone trys to get style='latex' for an
            del kwargs['style']
            return self.func(*args, **kwargs)


def getGenList():
    correctedList = genList[-1:] + genList[:-1]
    # Orders list by id
    correctedList.sort()
    return correctedList
