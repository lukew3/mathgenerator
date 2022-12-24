import random
import math


def bcd_to_decimal(maxNumber=10000):
    """Binary Coded Decimal to Integer"""
    n = random.randint(1000, maxNumber)
    binstring = ''
    while True:
        q, r = divmod(n, 10)
        nibble = bin(r).replace('0b', "")
        while len(nibble) < 4:
            nibble = '0' + nibble
        binstring = nibble + binstring
        if q == 0:
            break
        else:
            n = q

    problem = f"Integer of Binary Coded Decimal ${n}$ is $=$ "
    solution = f'${int(binstring, 2)}$'
    return problem, solution


def binary_2s_complement(maxDigits=10):
    """Binary 2's Complement"""
    digits = random.randint(1, maxDigits)
    question = ''.join([str(random.randint(0, 1))
                        for i in range(digits)]).lstrip('0')

    answer = []
    for i in question:
        answer.append(str(int(not bool(int(i)))))

    carry = True
    j = len(answer) - 1
    while j >= 0:
        if answer[j] == '0':
            answer[j] = '1'
            carry = False
            break
        answer[j] = '0'
        j -= 1

    if j == 0 and carry is True:
        answer.insert(0, '1')

    problem = f"2's complement of ${question} = $"
    solution = ''.join(answer).lstrip('0')
    return problem, f'${solution}$'


def binary_complement_1s(maxDigits=10):
    """Binary Complement 1s"""
    question = ''.join([str(random.randint(0, 1)) for _ in range(random.randint(1, maxDigits))])
    answer = ''.join(["0" if digit == "1" else "1" for digit in question])

    problem = f'${question} = $'
    return problem, f'${answer}$'


def binary_to_decimal(max_dig=10):
    """Binary to Decimal"""
    problem = ''.join([str(random.randint(0, 1)) for _ in range(random.randint(1, max_dig))])
    solution = f'${int(problem, 2)}$'
    return f'${problem}$', solution


def binary_to_hex(max_dig=10):
    """Binary to Hexidecimal"""
    problem = ''.join([str(random.randint(0, 1)) for _ in range(random.randint(1, max_dig))])
    solution = f'${hex(int(problem, 2))}$'
    return f'${problem}$', solution


def decimal_to_bcd(maxNumber=10000):
    """Decimal to Binary Coded Decimal"""
    n = random.randint(1000, maxNumber)
    x = n
    # binstring = ''
    bcdstring = ''
    while x > 0:
        nibble = x % 16
        bcdstring = str(nibble) + bcdstring
        x >>= 4

    problem = f"BCD of Decimal Number ${n} = $"
    return problem, f'${bcdstring}$'


def decimal_to_binary(max_dec=99):
    """Decimal to Binary"""
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")

    problem = f'Binary of ${a} = $'
    solution = f'${b}$'
    return problem, solution


def decimal_to_hexadeci(max_dec=1000):
    """Decimal to Hexadecimal"""
    a = random.randint(0, max_dec)
    b = hex(a)

    problem = f"Binary of ${a} = $"
    solution = f"${b}$"
    return problem, solution


def decimal_to_octal(maxDecimal=4096):
    """Decimal to Octal"""
    x = random.randint(0, maxDecimal)

    problem = "The decimal number ${x}$ in Octal is: "
    solution = f'${oct(x)}$'

    return problem, solution


def fibonacci_series(minNo=1):
    """Fibonacci Series"""
    n = random.randint(minNo, 20)

    def createFibList(n):
        list = []
        for i in range(n):
            if i < 2:
                list.append(i)
            else:
                val = list[i - 1] + list[i - 2]
                list.append(val)
        return list

    fibList = createFibList(n)

    problem = "The Fibonacci Series of the first ${n}$ numbers is ?"
    solution = ', '.join(map(str, fibList))
    return problem, f'${solution}$'


def modulo_division(maxRes=99, maxModulo=99):
    """Modulo Division"""
    a = random.randint(0, maxModulo)
    b = random.randint(0, min(maxRes, maxModulo))
    c = a % b if b != 0 else 0

    problem = f'${a}$ % ${b} = $'
    solution = f'${c}$'
    return problem, solution


def nth_fibonacci_number(maxN=100):
    """nth Fibonacci number"""
    gratio = (1 + math.sqrt(5)) / 2
    n = random.randint(1, maxN)

    problem = f"What is the {n}th Fibonacci number?"
    solution = int((math.pow(gratio, n) - math.pow(-gratio, -n)) / (math.sqrt(5)))

    return problem, f'${solution}$'
