from math import sqrt
from mathgenerator.mathgen import *

from hypothesis import strategies as st, given, assume


@given(maxSum=st.integers(min_value=1), maxAddend=st.integers(min_value=1))
def test_additionFunc(maxSum, maxAddend):
    assume(maxSum > maxAddend)
    problem, solution = additionFunc(maxSum, maxAddend)
    assert eval(problem[:-1]) == int(solution)


@given(maxMinuend=st.integers(min_value=1), maxDiff=st.integers(min_value=1))
def test_subtractionFunc(maxMinuend, maxDiff):
    assume(maxMinuend > maxDiff)
    problem, solution = subtractionFunc(maxMinuend, maxDiff)
    assert eval(problem[:-1]) == int(solution)


@given(maxRes=st.integers(min_value=1), maxMulti=st.integers(min_value=1))
def test_multiplicationFunc(maxRes, maxMulti):
    assume(maxRes > maxMulti)
    problem, solution = multiplicationFunc(maxRes, maxMulti)
    assert eval(problem[:-1]) == int(solution)


@given(maxRes=st.integers(min_value=1), maxDivid=st.integers(min_value=1))
def test_divisionFunc(maxRes, maxDivid):
    assume(maxRes > maxDivid)
    problem, solution = divisionFunc(maxRes, maxDivid)
    assert eval(problem[:-1]) == float(solution)


@given(maxRes=st.integers(min_value=1), maxModulo=st.integers(min_value=1))
def test_moduloFunc(maxRes, maxModulo):
    assume(maxRes > maxModulo)
    problem, solution = moduloFunc(maxRes, maxModulo)
    assert eval(problem[:-1]) == int(solution)


@given(maxDigits=st.integers(min_value=1, max_value=16))
def test_binaryComplement1sFunc(maxDigits):
    assume(maxDigits > 1)
    problem, solution = binaryComplement1sFunc(maxDigits)
    assert "".join('1' if i == '0' else '0' for i in problem[:-1]) == solution


@given(minNo=st.integers(min_value=1), maxNo=st.integers(min_value=1, max_value=2 ** 50))
def test_squareRootFunc(minNo, maxNo):
    assume(maxNo > minNo)
    problem, solution = squareRootFunc(minNo, maxNo)
    assert eval(problem[:-1]) == float(solution)


@given(maxSquareNum=st.integers(min_value=1))
def test_squareFunc(maxSquareNum):
    assume(maxSquareNum > 1)
    problem, solution = squareFunc(maxSquareNum)
    assert pow(int(problem[:-3]), 2) == int(solution)


@given(maxVal=st.integers(min_value=1))
def test_lcmFunc(maxVal):
    assume(maxVal > 1)
    problem, solution = lcmFunc(maxVal)
    split_arr = problem.split(' ')
    mult = int(split_arr[2])*int(split_arr[4])
    assert mult if mult != pow(int(split_arr[2]), 2) else int(
        split_arr[2]) == int(solution)


@given(maxVal=st.integers(min_value=1))
def test_gcdFunc(maxVal):
    assume(maxVal > 1)
    problem, solution = gcdFunc(maxVal)
    split_arr = problem.split(' ')
    mult = int(split_arr[2])*int(split_arr[4])
    assert mult if mult != pow(int(split_arr[2]), 2) else int(
        split_arr[2]) == int(solution)
