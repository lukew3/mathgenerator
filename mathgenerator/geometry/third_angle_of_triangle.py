import random


def third_angle_of_triangle(maxAngle=89):
    """Third Angle of Triangle"""
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, maxAngle)
    angle3 = 180 - (angle1 + angle2)

    problem = f"Third angle of triangle with angles ${angle1}$ and ${angle2} = $"
    return problem, f'${angle3}$'
