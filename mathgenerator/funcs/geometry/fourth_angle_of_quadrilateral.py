from .__init__ import *


def gen_func(maxAngle=180, format='string'):
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, 240 - angle1)
    angle3 = random.randint(1, 340 - (angle1 + angle2))

    sum_ = angle1 + angle2 + angle3
    angle4 = 360 - sum_

    if format == 'string':
        problem = f"Fourth angle of quadrilateral with angles {angle1} , {angle2}, {angle3} ="
        solution = angle4
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return angle1, angle2, angle3, angle4


fourth_angle_of_quadrilateral = Generator("Fourth Angle of Quadrilateral", 49,
                                          gen_func,
                                          ["maxAngle=180"])
