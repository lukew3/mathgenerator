def frac(num, den):
    return f'\\frac{{{num}}}{{{den}}}'

def bmatrix(lst):
    """Turns 2d matrix into a bmatrix"""
    out = '\\begin{bmatrix} '
    for row in lst:
        for item in row:
            out += str(item) + ' & '
        out += '\\\\ '
    out += '\\end{bmatrix}'
    return out

def exp(base, exp):
    return f'{base}^{{{exp}}}'
