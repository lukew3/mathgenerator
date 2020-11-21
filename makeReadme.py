from mathgenerator.mathgen import *

write_list = []
subjects = ['algebra', 'basic_math', 'calculus', 'computer_science', 'geometry', 'misc', 'statistics']
wList = getGenList()

def array2markdown_table(string):
    string = string.replace("[[", "<table><tr><td>")
    string = string.replace("[", "<tr><td>")
    string = string.replace(", ", "</td><td>")
    string = string.replace("]]", "</td></tr></table>")
    string = string.replace("]", "</td></tr>")
    string = string.replace(" ", "")
    string = string.replace("\n", "")
    return string

def write_table_of_contents():
    lines = []

    tc_lines = [
        '* [Installation](#installation)\n',
        '* [Basic Usage](#basic-usage)\n',
        '  * [More Complicated Usage](#more-complicated-usage)\n'
        '* [Documentation](#documentation)\n',
        '* [List of Generators](#list-of-generators)\n',
    ]
    for subject in subjects:
        line = '  * [' + subject + '](#' + subject + ')\n'
        tc_lines.append(line)

    with open('README.md', "r") as g:
        lines = g.readlines()

        upper_bound = lines.index('## Table of Contents\n')
        upper_lines = lines[:upper_bound + 1]
        lower_bound = lines.index('## Installation\n')
        lower_lines = lines[lower_bound - 1:]
        lines = []

        for upper_line in upper_lines:
            lines.append(upper_line)
        for tc_line in tc_lines:
            lines.append(tc_line)
        for lower_line in lower_lines:
            lines.append(lower_line)

    with open('README.md', "w") as g:
        g.writelines(lines)

def gen_to_row_string(item):
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
        write_list.append(gen_to_row_string(item))


def main():
    write_table_of_contents()
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

if __name__ == "__main__":
    main()
