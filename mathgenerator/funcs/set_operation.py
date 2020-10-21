from .__init__ import *


def set_operation(minval=3, maxval=7, n_a=4, n_b=5):
    number_variables_a = random.randint(minval, maxval)
    number_variables_b = random.randint(minval, maxval)
    a = []
    b = []
    for i in range(number_variables_a):
        a.append(random.randint(1, 10))
    for i in range(number_variables_b):
        b.append(random.randint(1, 10))
    a = set(a)
    b = set(b)
    problem = "Given the two sets a=" + \
        str(a) + " ,b=" + str(b) + ".Find the Union,intersection,a-b,b-a and symmetric difference"
    solution = "Union is " + str(a.union(b)) + ",Intersection is " + str(
        a.intersection(b)) + ", a-b is " + str(
            a.difference(b)) + ",b-a is " + str(
                b.difference(a)) + ", Symmetric difference is " + str(
                    a.symmetric_difference(b))
    return problem, solution


set_operation = Generator("Union,Intersection,Difference of Two Sets", 93,
                          "Union,intersection,difference", "aUb,a^b,a-b,b-a,",
                          set_operation)
