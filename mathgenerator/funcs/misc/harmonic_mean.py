from ...generator import Generator
import random


def gen_func(maxValue=100, maxCount=4):
    count = random.randint(2, maxCount)
    nums = [random.randint(1, maxValue) for _ in range(count)]
    sum = 0
    for num in nums:
        sum += (1 / num)
    ans = num / sum

    problem = f"Harmonic mean of ${count}$ numbers ${', '.join(map(str, nums))} = $"
    solution = f"${ans}$"
    return problem, solution


harmonic_mean = Generator("Harmonic Mean of N Numbers", 68, gen_func,
                          ["maxValue=100", "maxNum=4"])
