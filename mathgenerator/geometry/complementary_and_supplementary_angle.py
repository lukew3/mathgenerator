import random


def complementary_and_supplementary_angle(maxSupp=180, maxComp=90):
    """Complementary and Supplementary Angle"""
    angleType = random.choice(["supplementary", "complementary"])

    if angleType == "supplementary":
        angle = random.randint(1, maxSupp)
        angleAns = 180 - angle
    else:
        angle = random.randint(1, maxComp)
        angleAns = 90 - angle

    problem = f"The {angleType} angle of ${angle} =$"
    solution = f'${angleAns}$'
    return problem, solution
