from mathgenerator import mathgen

for item in mathgen.getGenList():
    if item[2](format='latex') == 'Latex unavailable':
        print(item[0], item[1], item[4])
