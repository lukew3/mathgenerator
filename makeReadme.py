from mathgenerator.mathgen import *

write_list = []

def array2markdown_table(string):
    string = string.replace("[[", "<table><tr><td>")
    string = string.replace("[", "<tr><td>")
    string = string.replace(", ", "</td><td>")
    string = string.replace("]]", "</td></tr></table>")
    string = string.replace("]", "</td></tr>")
    string = string.replace(" ", "")
    string = string.replace("\n", "")
    return string


def write_row(item):
    myGen = item[2]
    # NOTE: renamed 'sol' to 'solu' to make it look nicer
    prob, solu = myGen()
    prob = str(prob).rstrip("\n")
    solu = str(solu).rstrip("\n")
    # edge case for matrixMultiplication
    if item[0] == 46:
        prob, solu = myGen(maxVal=10, max_dim=4)
        prob = str(prob).rstrip("\n")
        solu = str(solu).rstrip("\n")
        prob = array2markdown_table(prob)
        solu = array2markdown_table(solu)

    # NOTE: renamed 'def_name' to 'func_name' because it suits it more
    func_name = item[3]
    row = [myGen.id, myGen.title, prob, solu, func_name]
    tableLine = "| " + str(row[0]) + " | " + str(row[1]) + " | " + str(
        row[2]) + " | " + str(row[3]) + " | " + str(row[4]) + " |\n"
    print('added', item[1], '-', func_name, 'to the README.md')
    return tableLine

def make_table_header(name):
    lines = [
        '## ' + name + '\n',
        '| Id   | Skill | Example problem | Example Solution | Function Name |\n',
        '|------|-------|-----------------|------------------|---------------|\n'
    ]
    for line in lines:
        write_list.append(line)

def write_subject_table(subject_name, full_gen_list):
    subject_list = []
    # Create list of generators in given subject
    for gen in full_gen_list:
        if gen[4] == subject_name:
            subject_list.append(gen)
    subject_list.sort()

    # Create table header
    make_table_header(subject_name)

    # Add each item to write_list
    for item in subject_list:
        write_list.append(write_row(item))


wList = getGenList()
lines = []
with open('mathgenerator/mathgen.py', 'r') as f:
    lines = f.readlines()

subjects = ['algebra', 'basic_math', 'calculus', 'computer_science', 'geometry', 'misc', 'statistics']
for subject in subjects:
    write_subject_table(subject, wList)

with open('README.md', "r") as g:
    lines = g.readlines()

    line = lines.index('## List of Generators\n')
    lines = lines[:line + 1]

    for write_line in write_list:
        lines.append(write_line)

with open('README.md', "w") as g:
    g.writelines(lines)

print("New README.md table generated")
