from .__init__ import *

def curvedSurfaceAreaCylinderFunc(maxRadius = 49, maxHeight=99):
    r = random.randint(1, maxRadius)
    h = random.randint(1, maxHeight)
    problem = f"What is Curved surface area of a cylinder of radius, {r} and height, {h}?"
    csa = float(2*math.pi*r*h)
    formatted_float = "{:.5f}".format(csa)
    solution = f"CSA of cylinder = {formatted_float}%"
    return problem, solution
