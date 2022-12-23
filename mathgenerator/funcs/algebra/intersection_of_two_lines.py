from ...generator import Generator
import random
import fractions


def gen_func(minM=-10,
             maxM=10,
             minB=-10,
             maxB=10,
             minDenominator=1,
             maxDenominator=6):
    def generateEquationString(m, b):
        """
        Generates an equation given the slope and intercept.
        It handles cases where m is fractional.
        It also ensures that we don't have weird signs such as y = mx + -b.
        """
        if m[0] == 0:
            m = 0
        elif abs(m[0]) == abs(m[1]):
            m = m[0] // m[1]
        elif m[1] == 1:
            m = m[0]
        else:
            m = f"{m[0]}/{m[1]}"
        base = "y ="
        if m != 0:
            if m == 1:
                base = f"{base} x"
            elif m == -1:
                base = f"{base} -x"
            else:
                base = f"{base} {m}x"
        if b > 0:
            if m == 0:
                return f"{base} {b}"
            else:
                return f"{base} + {b}"
        elif b < 0:
            if m == 0:
                return f"{base} -{b * -1}"
            else:
                return f"{base} - {b * -1}"
        else:
            if m == 0:
                return f"{base} 0"
            else:
                return base

    def fractionToString(x):
        """
        Converts the given fractions.Fraction into a string.
        """
        if x.denominator == 1:
            x = x.numerator
        else:
            x = f"{x.numerator}/{x.denominator}"
        return x

    m1 = (random.randint(minM,
                         maxM), random.randint(minDenominator, maxDenominator))
    m2 = (random.randint(minM,
                         maxM), random.randint(minDenominator, maxDenominator))

    b1 = random.randint(minB, maxB)
    b2 = random.randint(minB, maxB)

    eq1 = generateEquationString(m1, b1)
    eq2 = generateEquationString(m2, b2)

    problem = f"Find the point of intersection of the two lines: ${eq1}$ and ${eq2}$"

    m1 = fractions.Fraction(*m1)
    m2 = fractions.Fraction(*m2)
    # if m1 == m2 then the slopes are equal
    # This can happen if both line are the same
    # Or if they are parallel
    # In either case there is no intersection

    if m1 == m2:
        solution = "No Solution"
    else:
        intersection_x = (b1 - b2) / (m2 - m1)
        intersection_y = ((m2 * b1) - (m1 * b2)) / (m2 - m1)
        solution = f"$({fractionToString(intersection_x)}, {fractionToString(intersection_y)})$"

    return problem, solution


intersection_of_two_lines = Generator(
    "Intersection of Two Lines", 41, gen_func, [
        "minM=-10", "maxM=10", "minB=-10", "maxB=10", "minDenominator=1",
        "maxDenominator=6"
    ])
