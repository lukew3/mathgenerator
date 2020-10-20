from .__init__ import *


def matrixMultiplicationFunc(maxVal=100, max_dim=10):
    m = random.randint(2, max_dim)
    n = random.randint(2, max_dim)
    k = random.randint(2, max_dim)

    # generate matrices a and b
    a = []
    for r in range(m):
        a.append([])
        for c in range(n):
            a[r].append(random.randint(-maxVal, maxVal))
    b = []
    for r in range(n):
        b.append([])
        for c in range(k):
            b[r].append(random.randint(-maxVal, maxVal))

    res = []
    a_string = matrixMultiplicationFuncHelper(a)
    b_string = matrixMultiplicationFuncHelper(b)

    for r in range(m):
        res.append([])

        for c in range(k):
            temp = 0

            for t in range(n):
                temp += a[r][t] * b[t][c]
            res[r].append(temp)

    # consider using a, b instead of a_string, b_string if the problem doesn't look right
    problem = f"Multiply \n{a_string}\n and \n\n{b_string}"
    solution = matrixMultiplicationFuncHelper(res)
    return problem, solution


def matrixMultiplicationFuncHelper(inp):
    m = len(inp)
    n = len(inp[0])

    string = "[["
    for i in range(m):
        for j in range(n):
            string += f"{inp[i][j]: 6d}"
            string += ", " if j < n - 1 else ""
        string += "]\n [" if i < m - 1 else ""
    string += "]]"

    return string


matrix_multiplication = Generator("Multiplication of two matrices", 46,
                                  "Multiply two matrices A and B", "C",
                                  matrixMultiplicationFunc)
