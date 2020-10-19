from .__init__ import *


def DegreeToRadian(maxAngle=360):
    angle = random.randint(1, maxAngle)
    radian = round(math.radians(angle), 2)
    problem = f"{angle} Degrees is equal to Radian = "
    solution = radian

    return problem, solution