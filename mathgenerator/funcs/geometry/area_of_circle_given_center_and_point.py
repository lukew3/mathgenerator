from ...generator import Generator
import random
from math import cos, sin, pi


def gen_func(maxCoordinate=10, maxRadius=10):
    r = random.randint(0, maxRadius)
    center_x = random.randint(-maxCoordinate, maxCoordinate)
    center_y = random.randint(-maxCoordinate, maxCoordinate)

    angle = random.choice([0, pi // 6, pi // 2, pi, pi + pi // 6, 3 * pi // 2])

    point_x = center_x + round(r * cos(angle), 2)
    point_y = center_y + round(r * sin(angle), 2)

    area = round(pi * r * r, 2)

    problem = f"Area of circle with center $({center_x},{center_y})$ and passing through $({point_x}, {point_y})$ is"
    return problem, f'${area}$'


area_of_circle_given_center_and_point = Generator("Area of Circle given center and a point on circle", 115, gen_func,
                                                  ["maxCoordinate = 10", "maxRadius=10"])
