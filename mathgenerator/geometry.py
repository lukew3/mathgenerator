import random
import math
from math import cos, sin, pi


def angle_btw_vectors(maxEltAmt=20):
    """Angle between 2 vectors"""
    s = 0
    v1 = [
        round(random.uniform(0, 1000), 2)
        for i in range(random.randint(2, maxEltAmt))
    ]
    v2 = [round(random.uniform(0, 1000), 2) for i in v1]
    for i in range(len(v1)):
        s += v1[i] * v2[i]

    mags = math.sqrt(sum([i**2
                          for i in v1])) * math.sqrt(sum([i**2 for i in v2]))
    solution = ''
    ans = 0
    try:
        ans = round(math.acos(s / mags), 2)
        solution = f"${ans}$ radians"
    except ValueError:
        print('angleBtwVectorsFunc has some issues with math module, line 16')
        solution = 'NaN'
        ans = 'NaN'
    # would return the answer in radians
    problem = f"angle between the vectors ${v1}$ and ${v2}$ is:"
    return problem, solution


def angle_regular_polygon(minVal=3, maxVal=20, format='string'):
    """Angle of a Regular Polygon"""
    sideNum = random.randint(minVal, maxVal)
    problem = f"Find the angle of a regular polygon with ${sideNum}$ sides"

    exteriorAngle = round((360 / sideNum), 2)
    solution = f'${180 - exteriorAngle}$'

    return problem, solution


def arc_length(maxRadius=49, maxAngle=359):
    """Arc length of Angle"""
    radius = random.randint(1, maxRadius)
    angle = random.randint(1, maxAngle)
    angle_arc_length = float((angle / 360) * 2 * math.pi * radius)
    formatted_float = "{:.5f}".format(angle_arc_length)

    problem = f"Given radius, ${radius}$ and angle, ${angle}$. Find the arc length of the angle."
    solution = f"Arc length of the angle $= {formatted_float}$"
    return problem, solution


def area_of_circle(maxRadius=100):
    """Area of Circle"""
    r = random.randint(0, maxRadius)
    area = round(pi * r * r, 2)

    problem = f'Area of circle with radius ${r}=$'
    return problem, f'${area}$'


def area_of_circle_given_center_and_point(maxCoordinate=10, maxRadius=10):
    """Area of Circle given center and a point on circle"""
    r = random.randint(0, maxRadius)
    center_x = random.randint(-maxCoordinate, maxCoordinate)
    center_y = random.randint(-maxCoordinate, maxCoordinate)

    angle = random.choice([0, pi // 6, pi // 2, pi, pi + pi // 6, 3 * pi // 2])

    point_x = center_x + round(r * cos(angle), 2)
    point_y = center_y + round(r * sin(angle), 2)

    area = round(pi * r * r, 2)

    problem = f"Area of circle with center $({center_x},{center_y})$ and passing through $({point_x}, {point_y})$ is"
    return problem, f'${area}$'


def area_of_triangle(maxA=20, maxB=20):
    """Area of Triangle"""
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)
    c = random.randint(abs(b - a) + 1, abs(a + b) - 1)

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5

    problem = f"Area of triangle with side lengths: ${a}, {b} {c} = $"
    solution = f'${round(area, 2)}$'
    return problem, solution


# Handles degrees in quadrant one
def basic_trigonometry(angles=[0, 30, 45, 60, 90],
                       functions=["sin", "cos", "tan"]):
    """Trigonometric Values"""
    angle = random.choice(angles)
    function = random.choice(functions)

    problem = f"$\\{function}({angle}) = $"

    expression = 'math.' + function + '(math.radians(angle))'
    result_fraction_map = {
        0.0: "0",
        0.5: "\\frac{1}{2}",
        0.71: "\\frac{1}{\\sqrt{2}}",
        0.87: "\\frac{\\sqrt{3}}{2}",
        1.0: "1",
        0.58: "\\frac{1}{\\sqrt{3}}",
        1.73: "\\sqrt{3}",
    }

    solution = result_fraction_map[round(eval(expression), 2)] if round(
        eval(expression), 2) <= 99999 else "\\infty"  # for handling the ∞ condition

    return problem, f'${solution}$'


def circumference(maxRadius=100):
    """Circumference of Circle"""
    r = random.randint(0, maxRadius)
    circumference = round(2 * math.pi * r, 2)

    problem = f"Circumference of circle with radius ${r} = $"
    return problem, f'${circumference}$'


def complementary_and_supplementary_angle(maxSupp=180, maxComp=90):
    """Complementary and Supplementary Angle"""
    angleType = random.choice(["supplementary", "complementary"])

    if angleType == "supplementary":
        angle = random.randint(1, maxSupp)
        angleAns = 180 - angle
    else:
        angle = random.randint(1, maxComp)
        angleAns = 90 - angle

    problem = f"The {angleType} angle of ${angle} =$"
    solution = f'${angleAns}$'
    return problem, solution


def curved_surface_area_cylinder(maxRadius=49, maxHeight=99):
    """Curved surface area of a cylinder"""
    r = random.randint(1, maxRadius)
    h = random.randint(1, maxHeight)
    csa = float(2 * math.pi * r * h)
    formatted_float = round(csa, 2)  # "{:.5f}".format(csa)

    problem = f"What is the curved surface area of a cylinder of radius, ${r}$ and height, ${h}$?"
    solution = f"${formatted_float}$"
    return problem, solution


def degree_to_rad(max_deg=360):
    """Degrees to Radians"""
    a = random.randint(0, max_deg)
    b = (math.pi * a) / 180
    b = round(b, 2)

    problem = f"Angle ${a}$ degrees in radians is: "
    solution = f'${b}$'
    return problem, solution


def equation_of_line_from_two_points(maxCoordinate=20, minCoordinate=-20):
    """Equation of line from two points"""
    x1 = random.randint(minCoordinate, maxCoordinate)
    x2 = random.randint(minCoordinate, maxCoordinate)

    y1 = random.randint(minCoordinate, maxCoordinate)
    y2 = random.randint(minCoordinate, maxCoordinate)

    coeff_y = (x2 - x1)
    coeff_x = (y2 - y1)
    constant = y2 * coeff_y - x2 * coeff_x

    gcd = math.gcd(abs(coeff_x), abs(coeff_y))

    if gcd != 1:
        if coeff_y > 0:
            coeff_y //= gcd
        if coeff_x > 0:
            coeff_x //= gcd
        if constant > 0:
            constant //= gcd
        if coeff_y < 0:
            coeff_y = -(-coeff_y // gcd)
        if coeff_x < 0:
            coeff_x = -(-coeff_x // gcd)
        if constant < 0:
            constant = -(-constant // gcd)
    if coeff_y < 0:
        coeff_y = -(coeff_y)
        coeff_x = -(coeff_x)
        constant = -(constant)
    if coeff_x in [1, -1]:
        if coeff_x == 1:
            coeff_x = ''
        else:
            coeff_x = '-'
    if coeff_y in [1, -1]:
        if coeff_y == 1:
            coeff_y = ''
        else:
            coeff_y = '-'

    problem = f"What is the equation of the line between points $({x1},{y1})$ and $({x2},{y2})$ in slope-intercept form?"
    if coeff_x == 0:
        solution = str(coeff_y) + "y = " + str(constant)
    elif coeff_y == 0:
        solution = str(coeff_x) + "x = " + str(-constant)
    else:
        if constant > 0:
            solution = str(coeff_y) + "y = " + str(coeff_x) + "x + " + str(constant)
        else:
            solution = str(coeff_y) + "y = " + str(coeff_x) + "x " + str(constant)
    return problem, f'${solution}$'


def fourth_angle_of_quadrilateral(maxAngle=180):
    """Fourth Angle of Quadrilateral"""
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, 240 - angle1)
    angle3 = random.randint(1, 340 - (angle1 + angle2))

    sum_ = angle1 + angle2 + angle3
    angle4 = 360 - sum_

    problem = f"Fourth angle of quadrilateral with angles ${angle1} , {angle2}, {angle3} =$"
    solution = f'${angle4}$'
    return problem, solution


def perimeter_of_polygons(maxSides=12, maxLength=120):
    """Perimeter of Polygons"""
    size_of_sides = random.randint(3, maxSides)
    sides = [random.randint(1, maxLength) for _ in range(size_of_sides)]

    problem = f"The perimeter of a ${size_of_sides}$ sided polygon with lengths of ${', '.join(map(str, sides))}$cm is: "
    solution = sum(sides)

    return problem, f'${solution}$'


def pythagorean_theorem(maxLength=20):
    """Pythagorean Theorem"""
    a = random.randint(1, maxLength)
    b = random.randint(1, maxLength)
    c = round((a ** 2 + b ** 2) ** 0.5, 2)

    problem = f"What is the hypotenuse of a right triangle given the other two sides have lengths ${a}$ and ${b}$?"
    solution = f"${c}$"
    return problem, solution


def radian_to_deg(max_rad=6.28):
    """Radians to Degrees"""
    a = random.randint(0, int(max_rad * 100)) / 100
    b = round((180 * a) / math.pi, 2)

    problem = f"Angle ${a}$ radians in degrees is: "
    solution = f'${b}$'
    return problem, solution


def sector_area(maxRadius=49, maxAngle=359):
    """Area of a Sector"""
    r = random.randint(1, maxRadius)
    a = random.randint(1, maxAngle)
    secArea = float((a / 360) * math.pi * r * r)
    formatted_float = round(secArea, 2)

    problem = f"What is the area of a sector with radius ${r}$ and angle ${a}$ degrees?"
    solution = f"${formatted_float}$"
    return problem, solution


def sum_of_polygon_angles(maxSides=12):
    """Sum of Angles of Polygon"""
    side_count = random.randint(3, maxSides)
    sum = (side_count - 2) * 180

    problem = f"What is the sum of interior angles of a polygon with ${side_count}$ sides?"
    return problem, f'${sum}$'


def surface_area_cone(maxRadius=20, maxHeight=50, unit='m'):
    """Surface area of a cone"""
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)

    slopingHeight = math.sqrt(a**2 + b**2)
    ans = int(math.pi * b * slopingHeight + math.pi * b * b)

    problem = f"Surface area of cone with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def surface_area_cube(maxSide=20, unit='m'):
    """Surface area of a cube"""
    a = random.randint(1, maxSide)
    ans = 6 * (a ** 2)

    problem = f"Surface area of cube with side $= {a}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def surface_area_cuboid(maxSide=20, unit='m'):
    """Surface area of a cuboid"""
    a = random.randint(1, maxSide)
    b = random.randint(1, maxSide)
    c = random.randint(1, maxSide)
    ans = 2 * (a * b + b * c + c * a)

    problem = f"Surface area of cuboid with sides of lengths: ${a}{unit}, {b}{unit}, {c}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def surface_area_cylinder(maxRadius=20, maxHeight=50, unit='m'):
    """Surface area of a cylinder"""
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    ans = int(2 * math.pi * a * b + 2 * math.pi * b * b)

    problem = f"Surface area of cylinder with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


# List of Pythagorean triplets
_PYTHAGOREAN = [(3, 4, 5),
                (6, 8, 10),
                (9, 12, 15),
                (12, 16, 20),
                (15, 20, 25),

                (5, 12, 13),
                (10, 24, 26),

                (7, 24, 25)]


def surface_area_pyramid(unit='m'):
    """Surface area of a pyramid"""
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


def surface_area_sphere(maxSide=20, unit='m'):
    """Surface area of a sphere"""
    r = random.randint(1, maxSide)
    ans = 4 * math.pi * r * r

    problem = f"Surface area of Sphere with radius $= {r}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def third_angle_of_triangle(maxAngle=89):
    """Third Angle of Triangle"""
    angle1 = random.randint(1, maxAngle)
    angle2 = random.randint(1, maxAngle)
    angle3 = 180 - (angle1 + angle2)

    problem = f"Third angle of triangle with angles ${angle1}$ and ${angle2} = $"
    return problem, f'${angle3}$'


def valid_triangle(maxSideLength=50):
    """Valid Triangle"""
    sideA = random.randint(1, maxSideLength)
    sideB = random.randint(1, maxSideLength)
    sideC = random.randint(1, maxSideLength)

    sideSums = [sideA + sideB, sideB + sideC, sideC + sideA]
    sides = [sideC, sideA, sideB]

    exists = True & (sides[0] < sideSums[0]) & (sides[1] < sideSums[1]) & (
        sides[2] < sideSums[2])

    problem = f"Does triangle with sides ${sideA}, {sideB}$ and ${sideC}$ exist?"
    solution = "Yes" if exists else "No"
    return problem, f'${solution}$'


def volume_cone(maxRadius=20, maxHeight=50, unit='m'):
    """Volume of a cone"""
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    ans = int(math.pi * b * b * a * (1 / 3))

    problem = f"Volume of cone with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_cube(maxSide=20, unit='m'):
    """Volume of a cube"""
    a = random.randint(1, maxSide)
    ans = a**3

    problem = f"Volume of cube with a side length of ${a}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_cuboid(maxSide=20, unit='m'):
    """Volume of a cuboid"""
    a = random.randint(1, maxSide)
    b = random.randint(1, maxSide)
    c = random.randint(1, maxSide)
    ans = a * b * c

    problem = f"Volume of cuboid with sides = ${a}{unit}, {b}{unit}, {c}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_cylinder(maxRadius=20, maxHeight=50, unit='m'):
    """Volume of a cylinder"""
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    ans = int(math.pi * b * b * a)

    problem = f"Volume of cylinder with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_frustum(maxR1=20, maxR2=20, maxHeight=50, unit='m'):
    """Volume of a frustum"""
    h = random.randint(1, maxHeight)
    r1 = random.randint(1, maxR1)
    r2 = random.randint(1, maxR2)
    ans = ((math.pi * h) * (r1 ** 2 + r2 ** 2 + r1 * r2)) // 3

    problem = f"Volume of frustum with height $= {h}{unit}$ and $r1 = {r1}{unit}$ is and $r2 = {r1}{unit}$ is "
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_hemisphere(maxRadius=100):
    """Volume of a hemisphere"""
    r = random.randint(1, maxRadius)
    ans = round((2 * math.pi / 3) * r**3, 3)

    problem = f"Volume of hemisphere with radius ${r} m =$ "
    solution = f"${ans} m^3$"
    return problem, solution


def volume_pyramid(maxLength=20, maxWidth=20, maxHeight=50, unit='m'):
    """Volume of a pyramid"""
    length = random.randint(1, maxLength)
    width = random.randint(1, maxWidth)
    height = random.randint(1, maxHeight)

    ans = (length * width * height) / 3

    problem = f"Volume of pyramid with base length $= {length} {unit}$, base width $= {width} {unit}$ and height $= {height} {unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_sphere(maxRadius=100):
    """Volume of a sphere"""
    r = random.randint(1, maxRadius)
    ans = (4 * math.pi / 3) * r**3

    problem = f"Volume of sphere with radius ${r} m = $"
    solution = f"${ans} m^3$"
    return problem, solution
