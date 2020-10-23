from mathgenerator import mathgen

# test your generators here

print(mathgen.addition())

# prints each generator in genList
list = mathgen.getGenList()
for item in list:
    print(item[2])

# print(mathgen.getGenList())
print(mathgen.decimal_to_roman_numerals())
print(mathgen.genById(105))
