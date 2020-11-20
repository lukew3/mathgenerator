from .funcs import *
from .__init__ import getGenList
from worksheetgen.wg import Worksheet

genList = getGenList()


# || Non-generator Functions
def genById(id):
    generator = genList[id][2]
    return (generator())


def makePdf(id, count):
    generator = genList[id][2]
    title = genList[id][1]
    ws = Worksheet(title=title)
    for i in range(count):
        ws.add_problem(generator()[0])
    ws.write_pdf()
