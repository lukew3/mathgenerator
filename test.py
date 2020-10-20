from mathgenerator import mathgen

# test your generators here

print(mathgen.addition())
print(mathgen.genById(79))
print(mathgen.getGenList())
list = mathgen.getGenList()

# prints the order of generators in the list
for item in list:
    print(item[2])
