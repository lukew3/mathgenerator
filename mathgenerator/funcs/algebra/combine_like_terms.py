from .__init__ import *


def likeTermCombineFunc(maxCoef=10, maxExp=20, maxTerms=10):
    numTerms = random.randint(1, maxTerms)
    problem = ""
    solution = ""

    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, maxCoef)
        exponent = random.randint(1, max(numTerms - 1, 2))

        problem += str(coefficient) + "x^" + str(exponent)

    solution = combineTerms(problem)
    return problem, solution


def combineTerms(string):
    each_terms = string.split("+")
    dict_power_wise_terms = {}
    for i in range(11):
        dict_power_wise_terms[i] = []
    for term in each_terms:
        term = term.split("^")
        appendee = term[0].split("x")[0]
        if len(term) == 1:
            dict_power_wise_terms[1].append(int(appendee))
        else:
            dict_power_wise_terms[int(term[1])].append(int(appendee))

    final_string = ''
    for i in range(11):
        if len(dict_power_wise_terms[i]) != 0:
            total = sum(dict_power_wise_terms[i])
            final_string += str(total) + "x^" + str(i) + " + "
    final_string = '+'.join(final_string.split("+")[:-1])
    return final_string


combine_like_terms = Generator("Combine Like terms", 105, "nx^m+lx^k+bx^m",
                               "(n+b)x^m+lx^k", likeTermCombineFunc)
