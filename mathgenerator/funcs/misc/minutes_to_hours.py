from ...generator import Generator
import random


def gen_func(maxMinutes=999):
    minutes = random.randint(1, maxMinutes)
    ansHours = minutes // 60
    ansMinutes = minutes % 60

    problem = f"Convert ${minutes}$ minutes to hours & minutes"
    solution = f"${ansHours}$ hours and ${ansMinutes}$ minutes"
    return problem, solution


minutes_to_hours = Generator("Minute to Hour conversion", 102,
                             gen_func, ["maxMinutes=999"])
