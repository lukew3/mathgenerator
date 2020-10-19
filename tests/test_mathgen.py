from math import sqrt
from mathgenerator.mathgen import *

from hypothesis import strategies as st, given, assume


@given(maxSum=st.integers(min_value=1), maxAddend=st.integers(min_value=1))
def test_addition(maxSum, maxAddend):
    assume(maxSum > maxAddend)
    problem, solution = addition.func(maxSum, maxAddend)
    assert eval(problem[:-1]) == int(solution)


@given(maxMinuend=st.integers(min_value=1), maxDiff=st.integers(min_value=1))
def test_subtraction(maxMinuend, maxDiff):
    assume(maxMinuend > maxDiff)
    problem, solution = subtraction.func(maxMinuend, maxDiff)
    assert eval(problem[:-1]) == int(solution)


@given(maxRes=st.integers(min_value=1), maxMulti=st.integers(min_value=1))
def test_multiplication(maxRes, maxMulti):
    assume(maxRes > maxMulti)
    problem, solution = multiplication.func(maxRes, maxMulti)
    assert eval(problem[:-1]) == int(solution)


@given(maxRes=st.integers(min_value=1), maxDivid=st.integers(min_value=1))
def test_division(maxRes, maxDivid):
    assume(maxRes > maxDivid)
    problem, solution = division.func(maxRes, maxDivid)
    assert eval(problem[:-1]) == float(solution)


@given(maxRes=st.integers(min_value=1), maxModulo=st.integers(min_value=1))
def test_moduloDivision(maxRes, maxModulo):
    assume(maxRes > maxModulo)
    problem, solution = moduloDivision.func(maxRes, maxModulo)
    assert eval(problem[:-1]) == int(solution)


@given(minNo=st.integers(min_value=1), maxNo=st.integers(min_value=1, max_value=2 ** 50))
def test_squareRoot(minNo, maxNo):
    assume(maxNo > minNo)
    problem, solution = squareRoot.func(minNo, maxNo)
    assert eval(problem[:-1]) == float(solution)
