import random
import math
from math import cos, sin, pi


def angle_btw_vectors(max_elt_amt=20):
    r"""Angle between 2 vectors

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | angle between the vectors $[363.84, 195.54, 997.08, 39.26, 60.14, 722.7, 888.57, 713.15, 436.22, 712.23, 349.23, 595.91, 191.8, 824.58, 861.56, 122.73, 815.14, 700.68, 506.5]$ and $[760.85, 934.67, 513.37, 796.93, 809.97, 423.54, 162.69, 758.96, 133.42, 478.14, 771.84, 824.88, 483.07, 134.41, 954.41, 893.42, 191.01, 453.97, 648.59]$ is: | $0.81$ radians |
    """
    s = 0
    v1 = [
        round(random.uniform(0, 1000), 2)
        for i in range(random.randint(2, max_elt_amt))
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


def angle_regular_polygon(min_val=3, max_val=20):
    r"""Angle of a Regular Polygon

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Find the angle of a regular polygon with $8$ sides | $135.0$ |
    """
    sideNum = random.randint(min_val, max_val)
    problem = f"Find the angle of a regular polygon with ${sideNum}$ sides"

    exteriorAngle = round((360 / sideNum), 2)
    solution = f'${180 - exteriorAngle}$'

    return problem, solution


def arc_length(max_radius=49, max_angle=359):
    r"""Arc length of Angle

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Given radius, $44$ and angle, $184$. Find the arc length of the angle. | Arc length of the angle $= 141.30186$ |
    """
    radius = random.randint(1, max_radius)
    angle = random.randint(1, max_angle)
    angle_arc_length = float((angle / 360) * 2 * math.pi * radius)
    formatted_float = "{:.5f}".format(angle_arc_length)

    problem = f"Given radius, ${radius}$ and angle, ${angle}$. Find the arc length of the angle."
    solution = f"Arc length of the angle $= {formatted_float}$"
    return problem, solution


def area_of_circle(max_radius=100):
    r"""Area of Circle

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Area of circle with radius $29=$ | $2642.08$ |
    """
    r = random.randint(0, max_radius)
    area = round(pi * r * r, 2)

    problem = f'Area of circle with radius ${r}=$'
    return problem, f'${area}$'


def area_of_circle_given_center_and_point(max_coordinate=10, max_radius=10):
    r"""Area of Circle given center and a point on circle

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Area of circle with center $(7,-6)$ and passing through $(1.0, -6.0)$ is | $113.1$ |
    """
    r = random.randint(0, max_radius)
    center_x = random.randint(-max_coordinate, max_coordinate)
    center_y = random.randint(-max_coordinate, max_coordinate)

    angle = random.choice([0, pi // 6, pi // 2, pi, pi + pi // 6, 3 * pi // 2])

    point_x = center_x + round(r * cos(angle), 2)
    point_y = center_y + round(r * sin(angle), 2)

    area = round(pi * r * r, 2)

    problem = f"Area of circle with center $({center_x},{center_y})$ and passing through $({point_x}, {point_y})$ is"
    return problem, f'${area}$'


def area_of_trapezoid(max_len=20):
    r"""Area of Trapezoid

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Area of trapezoid with height $12$ and base lengths: $3, 7, = $ | $60$ |
    """
    a = random.randint(1, max_len)
    b = random.randint(1, max_len)
    h = random.randint(1, max_len)

    area = (a + b) * h / 2

    problem = f"Area of trapezoid with height ${h}$ and base lengths: ${a}, {b}, = $"
    solution = f'${round(area, 2)}$'
    return problem, solution


def area_of_triangle(max_a=20, max_b=20):
    r"""Area of Triangle

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Area of triangle with side lengths: $8, 1, 8 = $ | $3.99$ |
    """
    a = random.randint(1, max_a)
    b = random.randint(1, max_b)
    c = random.randint(abs(b - a) + 1, abs(a + b) - 1)

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5

    problem = f"Area of triangle with side lengths: ${a}, {b}, {c} = $"
    solution = f'${round(area, 2)}$'
    return problem, solution


# Handles degrees in quadrant one
def basic_trigonometry(angles=[0, 30, 45, 60, 90],
                       functions=["sin", "cos", "tan"]):
    r"""Trigonometric Values

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $\sin(30) = $ | $\frac{1}{2}$ |
    """
    angle = random.choice(angles)
    function = random.choice(functions)

    problem = rf"$\{function}({angle}) = $"

    expression = 'math.' + function + '(math.radians(angle))'
    result_fraction_map = {
        0.0: "0",
        0.5: r"\frac{1}{2}",
        0.71: r"\frac{1}{\sqrt{2}}",
        0.87: r"\frac{\sqrt{3}}{2}",
        1.0: "1",
        0.58: r"\frac{1}{\sqrt{3}}",
        1.73: r"\sqrt{3}",
    }

    #solution = result_fraction_map[round(
    #    eval(expression),
    #    2)] if round(eval(expression),
    #                 2) <= 99999 else r"\infty"  # for handling the ∞ condition

    return problem, f'{round(eval(expression))}'


def circumference(max_radius=100):
    r"""Circumference of Circle

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Circumference of circle with radius $56 = $ | $351.86$ |
    """
    r = random.randint(0, max_radius)
    circumference = round(2 * math.pi * r, 2)

    problem = f"Circumference of circle with radius ${r} = $"
    return problem, f'${circumference}$'


def complementary_and_supplementary_angle(max_supp=180, max_comp=90):
    r"""Complementary and Supplementary Angle

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The complementary angle of $15 =$ | $75$ |
    """
    angleType = random.choice(["supplementary", "complementary"])

    if angleType == "supplementary":
        angle = random.randint(1, max_supp)
        angleAns = 180 - angle
    else:
        angle = random.randint(1, max_comp)
        angleAns = 90 - angle

    problem = f"The {angleType} angle of ${angle} =$"
    solution = f'${angleAns}$'
    return problem, solution


def curved_surface_area_cylinder(max_radius=49, max_height=99):
    r"""Curved surface area of a cylinder

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the curved surface area of a cylinder of radius, $44$ and height, $92$? | $25434.33$ |
    """
    r = random.randint(1, max_radius)
    h = random.randint(1, max_height)
    csa = float(2 * math.pi * r * h)
    formatted_float = round(csa, 2)  # "{:.5f}".format(csa)

    problem = f"What is the curved surface area of a cylinder of radius, ${r}$ and height, ${h}$?"
    solution = f"${formatted_float}$"
    return problem, solution


def degree_to_rad(max_deg=360):
    r"""Degrees to Radians

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Angle $113$ degrees in radians is: | $1.97$ |
    """
    a = random.randint(0, max_deg)
    b = (math.pi * a) / 180
    b = round(b, 2)

    problem = f"Angle ${a}$ degrees in radians is: "
    solution = f'${b}$'
    return problem, solution


def equation_of_line_from_two_points(max_coordinate=20, min_coordinate=-20):
    r"""Equation of line from two points

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the equation of the line between points $(13,9)$ and $(6,-19)$ in slope-intercept form? | $y = 4x -43$ |
    """
    x1 = random.randint(min_coordinate, max_coordinate)
    x2 = random.randint(min_coordinate, max_coordinate)

    y1 = random.randint(min_coordinate, max_coordinate)
    y2 = random.randint(min_coordinate, max_coordinate)

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
            solution = str(coeff_y) + "y = " + str(coeff_x) + \
                "x + " + str(constant)
        else:
            solution = str(coeff_y) + "y = " + \
                str(coeff_x) + "x " + str(constant)
    return problem, f'${solution}$'


def fourth_angle_of_quadrilateral(max_angle=180):
    r"""Fourth Angle of Quadrilateral

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Fourth angle of quadrilateral with angles $162 , 43, 78 =$ | $77$ |
    """
    angle1 = random.randint(1, max_angle)
    angle2 = random.randint(1, 240 - angle1)
    angle3 = random.randint(1, 340 - (angle1 + angle2))

    sum_ = angle1 + angle2 + angle3
    angle4 = 360 - sum_

    problem = f"Fourth angle of quadrilateral with angles ${angle1} , {angle2}, {angle3} =$"
    solution = f'${angle4}$'
    return problem, solution


def perimeter_of_polygons(max_sides=12, max_length=120):
    r"""Perimeter of Polygons

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The perimeter of a $4$ sided polygon with lengths of $30, 105, 78, 106$cm is: | $319$ |
    """
    size_of_sides = random.randint(3, max_sides)
    sides = [random.randint(1, max_length) for _ in range(size_of_sides)]

    problem = f"The perimeter of a ${size_of_sides}$ sided polygon with lengths of ${', '.join(map(str, sides))}$cm is: "
    solution = sum(sides)

    return problem, f'${solution}$'


def pythagorean_theorem(max_length=20):
    """Pythagorean Theorem

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the hypotenuse of a right triangle given the other two sides have lengths $9$ and $10$? | $13.45$ |
    """
    a = random.randint(1, max_length)
    b = random.randint(1, max_length)
    c = round((a**2 + b**2)**0.5, 2)

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


def sector_area(max_radius=49, max_angle=359):
    """Area of a Sector

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the area of a sector with radius $42$ and angle $83$ degrees? | $1277.69$ |
    """
    r = random.randint(1, max_radius)
    a = random.randint(1, max_angle)
    secArea = float((a / 360) * math.pi * r * r)
    formatted_float = round(secArea, 2)

    problem = f"What is the area of a sector with radius ${r}$ and angle ${a}$ degrees?"
    solution = f"${formatted_float}$"
    return problem, solution


def sum_of_polygon_angles(max_sides=12):
    """Sum of Angles of Polygon

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the sum of interior angles of a polygon with $8$ sides? | $1080$ |
    """
    side_count = random.randint(3, max_sides)
    sum = (side_count - 2) * 180

    problem = f"What is the sum of interior angles of a polygon with ${side_count}$ sides?"
    return problem, f'${sum}$'


def surface_area_cone(max_radius=20, max_height=50, unit='m'):
    """Surface area of a cone

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Surface area of cone with height $= 26m$ and radius $= 6m$ is | $616 m^2$ |
    """
    a = random.randint(1, max_height)
    b = random.randint(1, max_radius)

    slopingHeight = math.sqrt(a**2 + b**2)
    ans = int(math.pi * b * slopingHeight + math.pi * b * b)

    problem = f"Surface area of cone with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def surface_area_cube(max_side=20, unit='m'):
    """Surface area of a cube

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Surface area of cube with side $= 6m$ is | $216 m^2$ |
    """
    a = random.randint(1, max_side)
    ans = 6 * (a**2)

    problem = f"Surface area of cube with side $= {a}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def surface_area_cuboid(max_side=20, unit='m'):
    """Surface area of a cuboid

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Surface area of cuboid with sides of lengths: $11m, 20m, 8m$ is | $936 m^2$ |
    """
    a = random.randint(1, max_side)
    b = random.randint(1, max_side)
    c = random.randint(1, max_side)
    ans = 2 * (a * b + b * c + c * a)

    problem = f"Surface area of cuboid with sides of lengths: ${a}{unit}, {b}{unit}, {c}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def surface_area_cylinder(max_radius=20, max_height=50, unit='m'):
    """Surface area of a cylinder

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Surface area of cylinder with height $= 26m$ and radius $= 15m$ is | $3864 m^2$ |
    """
    a = random.randint(1, max_height)
    b = random.randint(1, max_radius)
    ans = int(2 * math.pi * a * b + 2 * math.pi * b * b)

    problem = f"Surface area of cylinder with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def surface_area_pyramid(unit='m'):
    """Surface area of a pyramid

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Surface area of pyramid with base length $= 30m$, base width $= 40m$, and height $= 25m$ is | $2400 m^2$ |
    """
    # List of Pythagorean triplets
    _PYTHAGOREAN = [(3, 4, 5), (6, 8, 10), (9, 12, 15), (12, 16, 20),
                    (15, 20, 25), (5, 12, 13), (10, 24, 26), (7, 24, 25)]

    # Generate first triplet
    height, half_width, triangle_height_1 = random.sample(
        random.choice(_PYTHAGOREAN), 3)

    # Calculate first triangle's area
    triangle_1 = half_width * triangle_height_1

    # Generate second triplet
    second_triplet = random.choice([i for i in _PYTHAGOREAN if height in i])
    half_length, triangle_height_2 = random.sample(
        tuple(i for i in second_triplet if i != height), 2)

    # Calculate second triangle's area
    triangle_2 = half_length * triangle_height_2

    # Calculate base area
    base = 4 * half_width * half_length

    ans = base + 2 * triangle_1 + 2 * triangle_2

    problem = f"Surface area of pyramid with base length $= {2*half_length}{unit}$, base width $= {2*half_width}{unit}$, and height $= {height}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def surface_area_sphere(max_side=20, unit='m'):
    """Surface area of a sphere

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Surface area of a sphere with radius $= 8m$ is | $804.25 m^2$ |
    """
    r = random.randint(1, max_side)
    ans = round(4 * math.pi * r * r, 2)

    problem = f"Surface area of a sphere with radius $= {r}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


def third_angle_of_triangle(max_angle=89):
    """Third Angle of Triangle

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Third angle of triangle with angles $10$ and $22 =$ | $148$ |
    """
    angle1 = random.randint(1, max_angle)
    angle2 = random.randint(1, max_angle)
    angle3 = 180 - (angle1 + angle2)

    problem = f"Third angle of triangle with angles ${angle1}$ and ${angle2} = $"
    return problem, f'${angle3}$'


def valid_triangle(max_side_length=50):
    """Valid Triangle

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Does triangel with sides $10, 31$ and $14$ exist? | No |
    """
    sideA = random.randint(1, max_side_length)
    sideB = random.randint(1, max_side_length)
    sideC = random.randint(1, max_side_length)

    sideSums = [sideA + sideB, sideB + sideC, sideC + sideA]
    sides = [sideC, sideA, sideB]

    exists = True & (sides[0] < sideSums[0]) & (sides[1] < sideSums[1]) & (
        sides[2] < sideSums[2])

    problem = f"Does triangle with sides ${sideA}, {sideB}$ and ${sideC}$ exist?"
    solution = "Yes" if exists else "No"
    return problem, f'${solution}$'


def volume_cone(max_radius=20, max_height=50, unit='m'):
    """Volume of a cone

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Volume of cone with height $= 44m$ and radius $= 11m$ is | $5575 m^3$ |
    """
    a = random.randint(1, max_height)
    b = random.randint(1, max_radius)
    ans = int(math.pi * b * b * a * (1 / 3))

    problem = f"Volume of cone with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_cube(max_side=20, unit='m'):
    """Volume of a cube

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Volume of a cube with a side length of $19m$ is | $6859 m^3$ |
    """
    a = random.randint(1, max_side)
    ans = a**3

    problem = f"Volume of cube with a side length of ${a}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_cuboid(max_side=20, unit='m'):
    """Volume of a cuboid

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Volume of cuboid with sides = $17m, 11m, 13m$ is | $2431 m^3$ |
    """
    a = random.randint(1, max_side)
    b = random.randint(1, max_side)
    c = random.randint(1, max_side)
    ans = a * b * c

    problem = f"Volume of cuboid with sides = ${a}{unit}, {b}{unit}, {c}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_cylinder(max_radius=20, max_height=50, unit='m'):
    """Volume of a cylinder

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Volume of cylinder with height $= 3m$ and radius $= 10m$ is | $942 m^3$ |
    """
    a = random.randint(1, max_height)
    b = random.randint(1, max_radius)
    ans = int(math.pi * b * b * a)

    problem = f"Volume of cylinder with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_cone_frustum(max_r1=20, max_r2=20, max_height=50, unit='m'):
    """Volume of the frustum of a cone

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Volume of frustum with height $= 30m$ and $r1 = 20m$ is and $r2 = 8m$ is | $19603.54 m^3$ |
    """
    h = random.randint(1, max_height)
    r1 = random.randint(1, max_r1)
    r2 = random.randint(1, max_r2)
    ans = round(((math.pi * h) * (r1**2 + r2**2 + r1 * r2)) / 3, 2)

    problem = f"Volume of frustum with height $= {h}{unit}$ and $r1 = {r1}{unit}$ is and $r2 = {r2}{unit}$ is "
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_hemisphere(max_radius=100):
    """Volume of a hemisphere

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Volume of hemisphere with radius $32m =$ | $68629.14 m^3$ |
    """
    r = random.randint(1, max_radius)
    ans = round((2 * math.pi / 3) * r**3, 2)

    problem = f"Volume of hemisphere with radius ${r} m =$ "
    solution = f"${ans} m^3$"
    return problem, solution


def volume_pyramid(max_length=20, max_width=20, max_height=50, unit='m'):
    """Volume of a pyramid

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Volume of pyramid with base length $= 7 m$, base width $= 18 m$ and height $= 42 m$ is | $1764.0 m^3$ |
    """
    length = random.randint(1, max_length)
    width = random.randint(1, max_width)
    height = random.randint(1, max_height)

    ans = round((length * width * height) / 3, 2)

    problem = f"Volume of pyramid with base length $= {length} {unit}$, base width $= {width} {unit}$ and height $= {height} {unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


def volume_sphere(max_radius=100):
    """Volume of a sphere

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Volume of sphere with radius $30 m = $ | $113097.36 m^3$ |
    """
    r = random.randint(1, max_radius)
    ans = round((4 * math.pi / 3) * r**3, 2)

    problem = f"Volume of sphere with radius ${r} m = $"
    solution = f"${ans} m^3$"
    return problem, solution
