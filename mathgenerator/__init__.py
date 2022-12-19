import os
import traceback


genList = []

SEP = os.sep


class Generator:
    def __init__(self, title, id, func, kwargs):
        self.title = title
        self.id = id
        self.func = func
        self.kwargs = kwargs

        (filename, line_number, function_name,
         text) = traceback.extract_stack()[-2]
        funcname = filename[filename.rfind(SEP):].strip()
        funcname = funcname[1:-3]
        subjectname = filename[:filename.rfind(SEP)].strip()
        subjectname = subjectname[subjectname.rfind(SEP):].strip()
        subjectname = subjectname[1:]
        genList.append([id, title, self, funcname, subjectname, kwargs])

    def __str__(self):
        return str(self.id) + " " + self.title

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def getGenList():
    correctedList = genList[-1:] + genList[:-1]
    # Orders list by id
    correctedList.sort()
    return correctedList
