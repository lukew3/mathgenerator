import os
from makeReadme import main


def get_filepaths(subject_name):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    directory = "../mathgenerator/funcs/" + subject_name
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)

            front_len = 24 + len(subject_name)
            filename = filepath[front_len:-3]
            file_paths.append(filename)  # Add it to the list.

    return file_paths


subjects = [
    'algebra', 'basic_math', 'calculus', 'computer_science', 'geometry',
    'misc', 'statistics'
]
for subject in subjects:
    full_file_paths = get_filepaths(subject)
    full_file_paths.sort()
    lines = []
    for item in full_file_paths:
        if item[:2] != '__':
            lines.append(f"from .{item} import {item}\n")
    with open(f'../mathgenerator/funcs/{subject}/__init__.py', 'w') as f:
        f.writelines(lines)

main()  # makes readme
