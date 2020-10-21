from .__init__ import *


def thirdAngleOfTriangleFunc(maxAngle=89):
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, maxAngle)
    angle3 = 180 - (angle1 + angle2)

    problem = f"Third angle of triangle with angles {angle1} and {angle2} = "
    solution = angle3
    return problem, solution


third_angle_of_triangle = Generator("Third Angle of Triangle", 22,
                                    "Third Angle of the triangle = ", "angle3",
                                    thirdAngleOfTriangleFunc)
