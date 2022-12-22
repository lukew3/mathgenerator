from ...generator import Generator
import random


def gen_func(range_x=10,
             range_y=10,
             coeff_mult_range=10,
             format='string'):
    # Generate solution point first
    x = random.randint(-range_x, range_x)
    y = random.randint(-range_y, range_y)
    # Start from reduced echelon form (coeffs 1)
    c1 = [1, 0, x]
    c2 = [0, 1, y]

    def randNonZero():
        return random.choice(
            [i for i in range(-coeff_mult_range, coeff_mult_range) if i != 0])

    # Add random (non-zero) multiple of equations (rows) to each other
    c1_mult = randNonZero()
    c2_mult = randNonZero()
    new_c1 = [c1[i] + c1_mult * c2[i] for i in range(len(c1))]
    new_c2 = [c2[i] + c2_mult * c1[i] for i in range(len(c2))]
    # For extra randomness, now add random (non-zero) multiples of original rows
    # to themselves
    c1_mult = randNonZero()
    c2_mult = randNonZero()
    new_c1 = [new_c1[i] + c1_mult * c1[i] for i in range(len(c1))]
    new_c2 = [new_c2[i] + c2_mult * c2[i] for i in range(len(c2))]

    def coeffToFuncString(coeffs):
        # lots of edge cases for perfect formatting!
        x_sign = '-' if coeffs[0] < 0 else ''
        # No redundant 1s
        x_coeff = str(abs(coeffs[0])) if abs(coeffs[0]) != 1 else ''
        # If x coeff is 0, dont include x
        x_str = f'{x_sign}{x_coeff}x' if coeffs[0] != 0 else ''
        # if x isn't included and y is positive, dont include operator
        op = ' - ' if coeffs[1] < 0 else (' + ' if x_str != '' else '')
        # No redundant 1s
        y_coeff = abs(coeffs[1]) if abs(coeffs[1]) != 1 else ''
        # Don't include if 0, unless x is also 0 (probably never happens)
        y_str = f'{y_coeff}y' if coeffs[1] != 0 else (
            '' if x_str != '' else '0')
        return f'{x_str}{op}{y_str} = {coeffs[2]}'

    problem = f"Given ${coeffToFuncString(new_c1)}$ and ${coeffToFuncString(new_c2)}$, solve for $x$ and $y$."
    solution = f"$x = {x}$, $y = {y}$"
    return problem, solution
    # Add random (non-zero) multiple of equations to each other


system_of_equations = Generator(
    "Solve a System of Equations in R^2", 23, gen_func,
    ["range_x=10", "range_y=10", "coeff_mult_range=10"])
