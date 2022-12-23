from ...generator import Generator
from ...latexBuilder import bmatrix
import random
import math
import sympy


def gen_func(SquareMatrixDimension=3,
             MaxMatrixElement=99,
             OnlyIntegerElementsInInvertedMatrix=True):
    if OnlyIntegerElementsInInvertedMatrix is True:
        isItOk = False
        Mat = list()
        while (isItOk is False):
            Mat = list()
            for i in range(0, SquareMatrixDimension):
                z = list()
                for j in range(0, SquareMatrixDimension):
                    z.append(0)
                z[i] = 1
                Mat.append(z)
            MaxAllowedMatrixElement = math.ceil(
                pow(MaxMatrixElement, 1 / (SquareMatrixDimension)))
            randomlist = random.sample(range(0, MaxAllowedMatrixElement + 1),
                                       SquareMatrixDimension)

            for i in range(0, SquareMatrixDimension):
                if i == SquareMatrixDimension - 1:
                    Mat[0] = [
                        j + (k * randomlist[i])
                        for j, k in zip(Mat[0], Mat[i])
                    ]
                else:
                    Mat[i + 1] = [
                        j + (k * randomlist[i])
                        for j, k in zip(Mat[i + 1], Mat[i])
                    ]

            for i in range(1, SquareMatrixDimension - 1):
                Mat[i] = [
                    sum(i) for i in zip(Mat[SquareMatrixDimension - 1], Mat[i])
                ]

            isItOk = True
            for i in Mat:
                for j in i:
                    if j > MaxMatrixElement:
                        isItOk = False
                        break
                if isItOk is False:
                    break

        random.shuffle(Mat)
        Mat = sympy.Matrix(Mat)
        Mat = sympy.Matrix.transpose(Mat)
        Mat = Mat.tolist()
        random.shuffle(Mat)
        Mat = sympy.Matrix(Mat)
        Mat = sympy.Matrix.transpose(Mat)

    else:
        randomlist = list(sympy.primerange(0, MaxMatrixElement + 1))
        plist = random.sample(randomlist, SquareMatrixDimension)
        randomlist = random.sample(
            range(0, MaxMatrixElement + 1),
            SquareMatrixDimension * SquareMatrixDimension)
        randomlist = list(set(randomlist) - set(plist))
        n_list = random.sample(
            randomlist, SquareMatrixDimension * (SquareMatrixDimension - 1))
        Mat = list()
        for i in range(0, SquareMatrixDimension):
            z = list()
            z.append(plist[i])
            for j in range(0, SquareMatrixDimension - 1):
                z.append(n_list[(i * SquareMatrixDimension) + j - i])
            random.shuffle(z)
            Mat.append(z)
        Mat = sympy.Matrix(Mat)

    problem = 'Inverse of Matrix $' + bmatrix(Mat.tolist()) + '$ is:'
    solution = bmatrix(sympy.Matrix.inv(Mat).tolist())
    return problem, solution


invert_matrix = Generator("Inverse of a Matrix", 74, gen_func, [
    "SquareMatrixDimension=3", "MaxMatrixElement=99",
    "OnlyIntegerElementsInInvertedMatrix=True"
])
