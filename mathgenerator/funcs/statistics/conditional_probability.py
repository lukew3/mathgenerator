from ...generator import Generator
import random


def gen_func():
    P_disease = round(2. * random.random(), 2)
    true_positive = round(random.random() + float(random.randint(90, 99)), 2)
    true_negative = round(random.random() + float(random.randint(90, 99)), 2)

    def BayesFormula(P_disease, true_positive, true_negative):
        P_notDisease = 100. - P_disease
        false_positive = 100. - true_negative
        P_plus = (P_disease) * (true_positive) + \
            (P_notDisease) * (false_positive)
        P_disease_plus = ((true_positive) * (100 * P_disease)) / P_plus

        return P_disease_plus

    answer = round(BayesFormula(P_disease, true_positive, true_negative), 2)

    problem = "Someone tested positive for a nasty disease which only ${0:.2f}\\%$ of the population have. " \
        "Test sensitivity (true positive) is equal to $SN={1:.2f}$% whereas test specificity (true negative) $SP={2:.2f}\\%$. " \
        "What is the probability that this guy really has that disease?".format(
            P_disease, true_positive, true_negative)
    solution = f'${answer}$%'
    return problem, solution


conditional_probability = Generator("Conditional Probability", 107,
                                    gen_func, [""])
