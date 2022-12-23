from ...generator import Generator
import random


def gen_func(maxAngle=180):
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, 240 - angle1)
    angle3 = random.randint(1, 340 - (angle1 + angle2))

    sum_ = angle1 + angle2 + angle3
    angle4 = 360 - sum_

    problem = f"Fourth angle of quadrilateral with angles ${angle1} , {angle2}, {angle3} =$"
    solution = f'${angle4}$'
    return problem, solution


fourth_angle_of_quadrilateral = Generator("Fourth Angle of Quadrilateral", 49,
                                          gen_func,
                                          ["maxAngle=180"])
