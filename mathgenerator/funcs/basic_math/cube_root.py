from .__init__ import *


def cubeRootFunc(minNo=1, maxNo=1000, format='string'):
    b = random.randint(minNo, maxNo)
    a = b**(1 / 3)

    if format == 'string':
        return "What is the cube root of " + str(b) + " up to 2 decimal places?", str(round(a, 2))
    elif format == 'latex':
        return (f"\\(\\sqrt[3]{{{b}}}=\\)", "\\(" + str(round(a, 2)) + "\\)")
    else:
        return b, a


cube_root = Generator("Cube Root", 47, cubeRootFunc, ["minNo=1", "maxNo=1000"])
