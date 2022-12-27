def frac(num, den):
    return rf'\frac{{{num}}}{{{den}}}'


def bmatrix(lst):
    """Turns 2d matrix into a bmatrix"""
    out = r'\begin{bmatrix} '
    lst = [' & '.join(map(str, row)) for row in lst]
    out += r' \\\ '.join(lst)
    return out + r' \end{bmatrix}'


def exp(base, exp):
    return f'{base}^{{{exp}}}'
