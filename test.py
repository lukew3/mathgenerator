from mathgenerator import mathgen

for _ in range(100):
    print(mathgen.genById(2, maxMulti=100, style='latex'))
