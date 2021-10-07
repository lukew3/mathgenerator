from .__init__ import *


def gen_func(maxCP=1000, maxSP=1000, format='string'):
    cP = random.randint(1, maxCP)
    sP = random.randint(1, maxSP)
    diff = abs(sP - cP)
    if (sP - cP >= 0):
        profitOrLoss = "Profit"
    else:
        profitOrLoss = "Loss"
    percent = diff / cP * 100

    if format == 'string':
        problem = f"{profitOrLoss} percent when CP = {cP} and SP = {sP} is: "
        return problem, str(percent)
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return profitOrLoss, cP, sP, percent


profit_loss_percent = Generator("Profit or Loss Percent", 63,
                                gen_func,
                                ["maxCP=1000", "maxSP=1000"])
