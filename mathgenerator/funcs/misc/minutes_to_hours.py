from .__init__ import *


def minutesToHoursFunc(maxMinutes=999):
    minutes = random.randint(1, maxMinutes)
    hours1 = int(minutes / 60)
    hours2 = minutes % 60
    problem = f"Convert {minutes} minutes to Hours & Minutes"
    solution = f"{hours1} hours and {hours2} minutes"
    return problem, solution


minutes_to_hours = Generator("Minute to Hour conversion", 102,
                             "Convert minutes to Hours & Minutes", "hours:minutes", minutesToHoursFunc)
