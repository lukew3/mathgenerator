from ...generator import Generator
import random

# List of Pythagorean triplets
_PYTHAGOREAN = [(3, 4, 5),
                (6, 8, 10),
                (9, 12, 15),
                (12, 16, 20),
                (15, 20, 25),

                (5, 12, 13),
                (10, 24, 26),

                (7, 24, 25)]


def gen_func(unit='m'):
    # Generate first triplet
    height, half_width, triangle_height_1 = random.sample(random.choice(_PYTHAGOREAN), 3)

    # Calculate first triangle's area
    triangle_1 = half_width * triangle_height_1

    # Generate second triplet
    second_triplet = random.choice([i for i in _PYTHAGOREAN if height in i])
    half_length, triangle_height_2 = random.sample(tuple(i for i in second_triplet if i != height), 2)

    # Calculate second triangle's area
    triangle_2 = half_length * triangle_height_2

    # Calculate base area
    base = 4 * half_width * half_length

    ans = base + 2 * triangle_1 + 2 * triangle_2

    problem = f"Surface area of pyramid with base length $= {2*half_length}{unit}$, base width $= {2*half_width}{unit}$, and height $= {height}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


surface_area_pyramid = Generator("Surface area of pyramid", 123, gen_func,
                                 ["unit='m'"])
