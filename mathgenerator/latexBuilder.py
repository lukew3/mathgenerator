def frac(num, den):
    return f'\\frac{{{num}}}{{{den}}}'


def bmatrix(lst):
    """Turns 2d matrix into a bmatrix"""
    out = '\\begin{bmatrix} '
    lst = [' & '.join(map(str, row)) for row in lst]
    out += ' \\\\ '.join(lst)
    return out + ' \\end{bmatrix}'


def exp(base, exp):
    return f'{base}^{{{exp}}}'
