from  .__init__ import *


def hypotenuseFunc(maxBase = 1000, maxHeight = 1000):
    base = random.randint(1, maxBase)
    height = random.randint(1, maxHeight)
    hypotenuse = math.sqrt(base**2 + height**2)
    problem = f"Hypotenuse of a right angled triangle when base = {base} and height = {height} is: "
    solution = hypotenuse
