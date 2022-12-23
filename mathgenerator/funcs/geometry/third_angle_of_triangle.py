from ...generator import Generator
import random


def gen_func(maxAngle=89):
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, maxAngle)
    angle3 = 180 - (angle1 + angle2)

    problem = f"Third angle of triangle with angles ${angle1}$ and ${angle2} = $"
    return problem, f'${angle3}$'


third_angle_of_triangle = Generator("Third Angle of Triangle", 22,
                                    gen_func, ["maxAngle=89"])
