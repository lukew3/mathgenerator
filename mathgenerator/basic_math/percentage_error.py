import random


def percentage_error(maxValue=100, minValue=-100):
    """Percentage error"""
    observed_value = random.randint(minValue, maxValue)
    exact_value = random.randint(minValue, maxValue)

    if observed_value * exact_value < 0:
        observed_value *= -1

    error = (abs(observed_value - exact_value) / abs(exact_value)) * 100
    error = round(error, 2)

    problem = f"Find the percentage error when observed value equals ${observed_value}$ and exact value equals ${exact_value}$."
    solution = f'${error}\\%$'
    return problem, solution
