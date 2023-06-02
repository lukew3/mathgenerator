import os

name = 'computer_science'
with open(f'/home/luke/src/mathgenerator/mathgenerator/{name}.py', 'w') as f:
    source_dir_path = f'/home/luke/src/mathgenerator/mathgenerator/{name}'
    files = os.listdir(source_dir_path)
    for file in sorted(files):
        with open(os.path.join(source_dir_path, file), 'r') as f2:
            f.write(f2.read())
            f.write('\n')
