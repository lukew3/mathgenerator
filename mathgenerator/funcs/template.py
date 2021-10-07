from .__init__ import *


def gen_func(format='string'):


    if format == 'string':

        return problem, solution
    elif format == 'latex':

        return 'Latex unavailable'
    else:

        return


generator_name = Generator("<Title>", id, gen_func,
                          ["<kwarg1>"])
