from mathgenerator import mathgen

# test your generators here

# print(mathgen.addition())

# prints each generator in genList
# list = mathgen.getGenList()
#for item in list:
#    print(item[2])

# print(mathgen.getGenList())
#print(mathgen.genById(10))

#Make a pdf with 10 problems of generator id 1
# mathgen.makePdf(0, 10)

print(mathgen.genById(0, maxSum=20))
