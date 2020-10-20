genList = []


class Generator:
    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func
        genList.append([id, title, self])

    def __str__(self):
        return str(
            self.id
        ) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self, **kwargs):
        return self.func(**kwargs)


def getGenList():
    correctedList = genList[-1:] + genList[:-1]
    return correctedList
