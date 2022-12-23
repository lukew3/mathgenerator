import random


def minutes_to_hours(maxMinutes=999):
    """Convert minutes to hours and minutes"""
    minutes = random.randint(1, maxMinutes)
    ansHours = minutes // 60
    ansMinutes = minutes % 60

    problem = f"Convert ${minutes}$ minutes to hours & minutes"
    solution = f"${ansHours}$ hours and ${ansMinutes}$ minutes"
    return problem, solution
