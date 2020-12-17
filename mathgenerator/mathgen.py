from .funcs import *
from .__init__ import getGenList
from worksheetgen.wg import Worksheet

genList = getGenList()


# || Non-generator Functions
def genById(id, *args, **kwargs):
    generator = genList[id][2]
    return (generator(*args, **kwargs))


def make_worksheet(title):
    return Worksheet(title=title)


def write_pdf(worksheet):
    worksheet.write_pdf()


def add_section_title(worksheet, task_id):
    title = genList[task_id][1]
    worksheet.add_instruction(title)


def add_task_to_worksheet(worksheet, task_id, count):
    generator = genList[task_id][2]
    for i in range(count):
        worksheet.add_problem(generator()[0])


def add_section_with_task_to_worksheet(worksheet, task_id, count):
    add_section_title(worksheet, task_id)
    add_task_to_worksheet(worksheet, task_id, count)


def make_pdf(task_id, count):
    title = genList[task_id][1]
    worksheet = make_worksheet(title)
    add_task_to_worksheet(worksheet, task_id, count)
    write_pdf(worksheet)
