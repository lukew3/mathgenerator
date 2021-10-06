from .__init__ import *


def minutesToHoursFunc(maxMinutes=999, format='string'):
    minutes = random.randint(1, maxMinutes)
    ansHours = int(minutes / 60)
    ansMinutes = minutes % 60

    if format == 'string':
        problem = f"Convert {minutes} minutes to Hours & Minutes"
        solution = f"{ansHours} hours and {ansMinutes} minutes"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return minutes, ansHours, ansMinutes


minutes_to_hours = Generator("Minute to Hour conversion", 102,
                             minutesToHoursFunc, ["maxMinutes=999"])
