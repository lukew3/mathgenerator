from .__init__ import *


def profitLossPercentFunc(maxCP=1000, maxSP=1000):
    cP = random.randint(1, maxCP)
    sP = random.randint(1, maxSP)
    diff = abs(sP - cP)
    if (sP - cP >= 0):
        profitOrLoss = "Profit"
    else:
        profitOrLoss = "Loss"
    percent = diff / cP * 100
    problem = f"{profitOrLoss} percent when CP = {cP} and SP = {sP} is: "
    solution = percent

    return problem, solution


profit_loss_percent = Generator(
    "Profit or Loss Percent", 63,
    "Profit/ Loss percent when CP = cp and SP = sp is: ", "percent",
    profitLossPercentFunc)
