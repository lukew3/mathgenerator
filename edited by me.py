from math import sqrt
from mathgenerator.mathgen import *

from hypothesis import strategies as st, given, assume


@given(maxSum=st.integers(min_value=1), maxAddend=st.integers(min_value=1))
def test_additionFunc(maxSum, maxAddend):
    assume(maxSum > maxAddend)
    problem, solution = additionFunc(maxSum,maxAddend)
    assert eval(problem[:-1])== int(solution)


@given(maxMinuend=st.integers(min_value=1), maxDiff=st.integers(min_value=1))
def test_subtractionFunc(maxMinuend, maxDiff):
    assume(maxMinuend > maxDiff)
    problem, solution = subtractionFunc(maxMinuend,maxDiff)
    assert eval(problem[:-1]) == int(solution)


@given(maxRes=st.integers(min_value=1), maxMulti=st.integers(min_value=1))
def test_multiplicationFunc(maxRes, maxMulti):
    assume(maxRes > maxMulti)
    problem, solution = multiplicationFunc(maxRes,maxMulti)
    assert eval(problem[:-1]) == int(solution)


@given(maxRes=st.integers(min_value=1), maxDivid=st.integers(min_value=1))
def test_divisionFunc(maxRes, maxDivid):
    assume(maxRes > maxDivid)
    problem, solution = divisionFunc(maxRes, maxDivid)
    assert eval(problem[:-1]) == float(solution)


@given(maxRes=st.integers(min_value=1), maxModulo=st.integers(min_value=1))
def test_moduloFunc(maxRes, maxModulo):
    assume(maxRes > maxModulo)
    problem, solution = moduloFunc(maxRes,maxModulo)
    assert eval(problem[:-1]) == int(solution)


@given(minNo=st.integers(min_value=1), maxNo=st.integers(min_value=1, max_value=2 ** 50))
def test_squareRootFunc(minNo, maxNo):
    assume(maxNo > minNo)
    problem, solution = squareRootFunc(minNo,maxNo)
    assert eval(problem[:-1]) == float(solution)
