import random


def combine_like_terms(maxCoef=10, maxExp=20, maxTerms=10):
    """Combine Like Terms"""
    numTerms = random.randint(1, maxTerms)

    coefs = [random.randint(1, maxCoef) for _ in range(numTerms)]
    exponents = [random.randint(1, max(maxExp - 1, 2)) for _ in range(numTerms)]

    problem = " + ".join([f"{coefs[i]}x^{{{exponents[i]}}}" for i in range(numTerms)])
    d = {}
    for i in range(numTerms):
        if exponents[i] in d:
            d[exponents[i]] += coefs[i]
        else:
            d[exponents[i]] = coefs[i]
    solution = " + ".join([f"{d[k]}x^{{{k}}}" for k in sorted(d)])

    return f'${problem}$', f'${solution}$'
