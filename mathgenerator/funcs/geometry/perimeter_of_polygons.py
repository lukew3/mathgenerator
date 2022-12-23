import random


def perimeter_of_polygons(maxSides=12, maxLength=120):
    """Perimeter of Polygons"""
    size_of_sides = random.randint(3, maxSides)
    sides = [random.randint(1, maxLength) for _ in range(size_of_sides)]

    problem = f"The perimeter of a ${size_of_sides}$ sided polygon with lengths of ${', '.join(map(str, sides))}$cm is: "
    solution = sum(sides)

    return problem, f'${solution}$'
