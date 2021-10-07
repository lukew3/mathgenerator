from .__init__ import *


def gen_func(maxSides=12, maxLength=120, format='string'):
    size_of_sides = random.randint(3, maxSides)
    sides = []
    for x in range(size_of_sides):
        sides.append(random.randint(1, maxLength))
    problem = "The perimeter of a " + str(size_of_sides) + \
        " sided polygon with lengths of " + str(sides) + "cm is: "
    solution = 0
    for y in range(len(sides)):
        solution += sides[y]

    if format == 'string':
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return size_of_sides, sides, solution


perimeter_of_polygons = Generator("Perimeter of Polygons", 96,
                                  gen_func,
                                  ["maxSides=12", "maxLength=120"])
