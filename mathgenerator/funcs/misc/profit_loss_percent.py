from ...generator import Generator
import random


def gen_func(maxCP=1000, maxSP=1000):
    cP = random.randint(1, maxCP)
    sP = random.randint(1, maxSP)
    diff = abs(sP - cP)
    if (sP - cP >= 0):
        profitOrLoss = "Profit"
    else:
        profitOrLoss = "Loss"
    percent = round(diff / cP * 100, 2)

    problem = f"{profitOrLoss} percent when $CP = {cP}$ and $SP = {sP}$ is: "
    return problem, f'${percent}$'


profit_loss_percent = Generator("Profit or Loss Percent", 63,
                                gen_func,
                                ["maxCP=1000", "maxSP=1000"])
