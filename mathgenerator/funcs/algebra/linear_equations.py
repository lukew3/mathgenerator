from .__init__ import *


def linearEquationsFunc(n=2, varRange=20, coeffRange=20):
    if n > 10:
        print("[!] n cannot be greater than 10")
        return None, None

    vars = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'][:n]
    soln = [random.randint(-varRange, varRange) for i in range(n)]
    problem = list()
    solution = ", ".join(
        ["{} = {}".format(vars[i], soln[i]) for i in range(n)])

    for _ in range(n):
        coeff = [random.randint(-coeffRange, coeffRange) for i in range(n)]
        res = sum([coeff[i] * soln[i] for i in range(n)])
        prob = [
            "{}{}".format(coeff[i], vars[i]) if coeff[i] != 0 else ""
            for i in range(n)
        ]

        while "" in prob:
            prob.remove("")
        prob = " + ".join(prob) + " = " + str(res)
        problem.append(prob)

    # problem = "\n".join(problem)
    problem = ", ".join(problem)
    return problem, solution


linear_equations = Generator("Linear Equations", 26, "2x+5y=20 & 3x+6y=12",
                             "x=-20 & y=12", linearEquationsFunc)
