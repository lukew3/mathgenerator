from .__init__ import *


def gen_func(maxAngle=89, format='string'):
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, maxAngle)
    angle3 = 180 - (angle1 + angle2)

    if format == 'string':
        problem = f"Third angle of triangle with angles {angle1} and {angle2} = "
        return problem, angle3
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return angle1, angle2, angle3


third_angle_of_triangle = Generator("Third Angle of Triangle", 22,
                                    gen_func, ["maxAngle=89"])
