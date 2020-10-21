from  .__init__ import *


def minutesToHoursFunc(maxMinutes=999):
	minutes = random.randint(1, maxMinutes)
	hours1 = int(minutes/60)
	hours2 = minutes%60
	problem = f"Convert {minutes} minutes to Hours & Minutes"
	solution = f"minutes_to_hours(230) = {hours1}h:{hours2}m"
	return problem, solution
  
  minutesToHours = Generator("Minute to Hour conversion", 96 , "Convert minutes to Hours & Minutes", "hours:minutes", minutesToHoursFunc)
