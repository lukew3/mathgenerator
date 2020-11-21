from .__init__ import *


def fourthAngleOfQuadriFunc(maxAngle=180):
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, 240 - angle1)
    angle3 = random.randint(1, 340 - (angle1 + angle2))

    sum_ = angle1 + angle2 + angle3
    angle4 = 360 - sum_

    problem = f"Fourth angle of quadrilateral with angles {angle1} , {angle2}, {angle3} ="
    solution = angle4
    return problem, solution


fourth_angle_of_quadrilateral = Generator(
    "Fourth Angle of Quadrilateral", 49,
    "Fourth angle of Quadrilateral with angles a,b,c =", "angle4",
    fourthAngleOfQuadriFunc)
