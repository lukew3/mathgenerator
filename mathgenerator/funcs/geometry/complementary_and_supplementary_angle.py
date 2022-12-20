from ...generator import Generator
import random


def gen_func(maxSupp=180, maxComp=90, format='string'):
    angleType = random.choice(["supplementary", "complementary"])

    if angleType == "supplementary":
        angle = random.randint(1, maxSupp)
        angleAns = 180 - angle
    else:
        angle = random.randint(1, maxComp)
        angleAns = 90 - angle

    if format == 'string':
        problem = f"The {angleType} angle of {angle} ="
        solution = angleAns
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return angleType, angle, angleAns


complementary_and_supplementary_angle = Generator("Complementary and Supplementary Angle", 125,
                                                  gen_func, ["maxSupp=180", "maxComp=90"])
