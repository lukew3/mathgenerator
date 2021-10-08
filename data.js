const data = [
    {
        "function_name": "addition",
        "id": 0,
        "kwargs": [
            "maxSum=99",
            "maxAddend=50"
        ],
        "name": "Addition",
        "samples": [
            {
                "problem": "34+25=",
                "solution": "59"
            },
            {
                "problem": "32+2=",
                "solution": "34"
            },
            {
                "problem": "18+47=",
                "solution": "65"
            },
            {
                "problem": "31+31=",
                "solution": "62"
            },
            {
                "problem": "23+47=",
                "solution": "70"
            },
            {
                "problem": "47+18=",
                "solution": "65"
            },
            {
                "problem": "46+42=",
                "solution": "88"
            },
            {
                "problem": "12+42=",
                "solution": "54"
            },
            {
                "problem": "24+6=",
                "solution": "30"
            },
            {
                "problem": "2+13=",
                "solution": "15"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "subtraction",
        "id": 1,
        "kwargs": [
            "maxMinuend=99",
            "maxDiff=99"
        ],
        "name": "Subtraction",
        "samples": [
            {
                "problem": "57-43=",
                "solution": "14"
            },
            {
                "problem": "69-61=",
                "solution": "8"
            },
            {
                "problem": "19-11=",
                "solution": "8"
            },
            {
                "problem": "11-6=",
                "solution": "5"
            },
            {
                "problem": "72-13=",
                "solution": "59"
            },
            {
                "problem": "74-15=",
                "solution": "59"
            },
            {
                "problem": "94-53=",
                "solution": "41"
            },
            {
                "problem": "89-47=",
                "solution": "42"
            },
            {
                "problem": "93-68=",
                "solution": "25"
            },
            {
                "problem": "50-13=",
                "solution": "37"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "multiplication",
        "id": 2,
        "kwargs": [
            "maxMulti=12"
        ],
        "name": "Multiplication",
        "samples": [
            {
                "problem": "11*10=",
                "solution": "110"
            },
            {
                "problem": "1*7=",
                "solution": "7"
            },
            {
                "problem": "1*5=",
                "solution": "5"
            },
            {
                "problem": "3*11=",
                "solution": "33"
            },
            {
                "problem": "10*2=",
                "solution": "20"
            },
            {
                "problem": "1*6=",
                "solution": "6"
            },
            {
                "problem": "4*12=",
                "solution": "48"
            },
            {
                "problem": "10*6=",
                "solution": "60"
            },
            {
                "problem": "4*2=",
                "solution": "8"
            },
            {
                "problem": "0*2=",
                "solution": "0"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "division",
        "id": 3,
        "kwargs": [
            "maxA=25",
            "maxB=25"
        ],
        "name": "Division",
        "samples": [
            {
                "problem": "14/1=",
                "solution": "14"
            },
            {
                "problem": "90/15=",
                "solution": "6"
            },
            {
                "problem": "153/17=",
                "solution": "9"
            },
            {
                "problem": "13/13=",
                "solution": "1"
            },
            {
                "problem": "152/19=",
                "solution": "8"
            },
            {
                "problem": "13/1=",
                "solution": "13"
            },
            {
                "problem": "28/4=",
                "solution": "7"
            },
            {
                "problem": "50/2=",
                "solution": "25"
            },
            {
                "problem": "69/3=",
                "solution": "23"
            },
            {
                "problem": "126/14=",
                "solution": "9"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "binary_complement_1s",
        "id": 4,
        "kwargs": [
            "maxDigits=10"
        ],
        "name": "Binary Complement 1s",
        "samples": [
            {
                "problem": "01=",
                "solution": "10"
            },
            {
                "problem": "101=",
                "solution": "010"
            },
            {
                "problem": "100=",
                "solution": "011"
            },
            {
                "problem": "0=",
                "solution": "1"
            },
            {
                "problem": "1001110011=",
                "solution": "0110001100"
            },
            {
                "problem": "11101110=",
                "solution": "00010001"
            },
            {
                "problem": "1001010110=",
                "solution": "0110101001"
            },
            {
                "problem": "110010=",
                "solution": "001101"
            },
            {
                "problem": "01=",
                "solution": "10"
            },
            {
                "problem": "10010=",
                "solution": "01101"
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "modulo_division",
        "id": 5,
        "kwargs": [
            "maxRes=99",
            "maxModulo=99"
        ],
        "name": "Modulo Division",
        "samples": [
            {
                "problem": "86%1=",
                "solution": "0"
            },
            {
                "problem": "14%69=",
                "solution": "14"
            },
            {
                "problem": "89%70=",
                "solution": "19"
            },
            {
                "problem": "2%89=",
                "solution": "2"
            },
            {
                "problem": "37%22=",
                "solution": "15"
            },
            {
                "problem": "51%52=",
                "solution": "51"
            },
            {
                "problem": "80%84=",
                "solution": "80"
            },
            {
                "problem": "33%96=",
                "solution": "33"
            },
            {
                "problem": "69%56=",
                "solution": "13"
            },
            {
                "problem": "17%63=",
                "solution": "17"
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "square_root",
        "id": 6,
        "kwargs": [
            "minNo=1",
            "maxNo=12"
        ],
        "name": "Square Root",
        "samples": [
            {
                "problem": "sqrt(25)=",
                "solution": "5"
            },
            {
                "problem": "sqrt(144)=",
                "solution": "12"
            },
            {
                "problem": "sqrt(49)=",
                "solution": "7"
            },
            {
                "problem": "sqrt(25)=",
                "solution": "5"
            },
            {
                "problem": "sqrt(9)=",
                "solution": "3"
            },
            {
                "problem": "sqrt(144)=",
                "solution": "12"
            },
            {
                "problem": "sqrt(121)=",
                "solution": "11"
            },
            {
                "problem": "sqrt(1)=",
                "solution": "1"
            },
            {
                "problem": "sqrt(121)=",
                "solution": "11"
            },
            {
                "problem": "sqrt(1)=",
                "solution": "1"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "power_rule_differentiation",
        "id": 7,
        "kwargs": [
            "maxCoef=10",
            "maxExp=10",
            "maxTerms=5"
        ],
        "name": "Power Rule Differentiation",
        "samples": [
            {
                "problem": "6x^5 + 4x^6 + 3x^10 + 6x^6 + 10x^5",
                "solution": "30x^4 + 24x^5 + 30x^9 + 36x^5 + 50x^4"
            },
            {
                "problem": "10x^10 + 10x^4 + 10x^3 + 2x^1",
                "solution": "100x^9 + 40x^3 + 30x^2 + 2x^0"
            },
            {
                "problem": "7x^1 + 2x^1 + 7x^9",
                "solution": "7x^0 + 2x^0 + 63x^8"
            },
            {
                "problem": "10x^2 + 8x^1 + 2x^4 + 8x^4 + 5x^2",
                "solution": "20x^1 + 8x^0 + 8x^3 + 32x^3 + 10x^1"
            },
            {
                "problem": "2x^4 + 8x^8 + 6x^9 + 6x^8",
                "solution": "8x^3 + 64x^7 + 54x^8 + 48x^7"
            },
            {
                "problem": "1x^7",
                "solution": "7x^6"
            },
            {
                "problem": "6x^10 + 3x^8 + 6x^10 + 4x^7 + 4x^3",
                "solution": "60x^9 + 24x^7 + 60x^9 + 28x^6 + 12x^2"
            },
            {
                "problem": "5x^3 + 1x^1 + 10x^3",
                "solution": "15x^2 + 1x^0 + 30x^2"
            },
            {
                "problem": "10x^3 + 1x^1",
                "solution": "30x^2 + 1x^0"
            },
            {
                "problem": "10x^1",
                "solution": "10x^0"
            }
        ],
        "subject": "calculus"
    },
    {
        "function_name": "square",
        "id": 8,
        "kwargs": [
            "maxSquareNum=20"
        ],
        "name": "Square",
        "samples": [
            {
                "problem": "12^2=",
                "solution": "144"
            },
            {
                "problem": "3^2=",
                "solution": "9"
            },
            {
                "problem": "4^2=",
                "solution": "16"
            },
            {
                "problem": "5^2=",
                "solution": "25"
            },
            {
                "problem": "19^2=",
                "solution": "361"
            },
            {
                "problem": "7^2=",
                "solution": "49"
            },
            {
                "problem": "19^2=",
                "solution": "361"
            },
            {
                "problem": "10^2=",
                "solution": "100"
            },
            {
                "problem": "19^2=",
                "solution": "361"
            },
            {
                "problem": "3^2=",
                "solution": "9"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "lcm",
        "id": 9,
        "kwargs": [
            "maxVal=20"
        ],
        "name": "LCM (Least Common Multiple)",
        "samples": [
            {
                "problem": "LCM of 9 and 4 =",
                "solution": "36"
            },
            {
                "problem": "LCM of 13 and 15 =",
                "solution": "195"
            },
            {
                "problem": "LCM of 13 and 4 =",
                "solution": "52"
            },
            {
                "problem": "LCM of 6 and 16 =",
                "solution": "48"
            },
            {
                "problem": "LCM of 7 and 1 =",
                "solution": "7"
            },
            {
                "problem": "LCM of 5 and 4 =",
                "solution": "20"
            },
            {
                "problem": "LCM of 10 and 11 =",
                "solution": "110"
            },
            {
                "problem": "LCM of 12 and 12 =",
                "solution": "12"
            },
            {
                "problem": "LCM of 20 and 3 =",
                "solution": "60"
            },
            {
                "problem": "LCM of 19 and 15 =",
                "solution": "285"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "gcd",
        "id": 10,
        "kwargs": [
            "maxVal=20"
        ],
        "name": "GCD (Greatest Common Denominator)",
        "samples": [
            {
                "problem": "GCD of 9 and 4 = ",
                "solution": "1"
            },
            {
                "problem": "GCD of 6 and 9 = ",
                "solution": "3"
            },
            {
                "problem": "GCD of 5 and 13 = ",
                "solution": "1"
            },
            {
                "problem": "GCD of 3 and 3 = ",
                "solution": "3"
            },
            {
                "problem": "GCD of 18 and 17 = ",
                "solution": "1"
            },
            {
                "problem": "GCD of 19 and 18 = ",
                "solution": "1"
            },
            {
                "problem": "GCD of 13 and 11 = ",
                "solution": "1"
            },
            {
                "problem": "GCD of 4 and 18 = ",
                "solution": "2"
            },
            {
                "problem": "GCD of 1 and 15 = ",
                "solution": "1"
            },
            {
                "problem": "GCD of 20 and 15 = ",
                "solution": "5"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "basic_algebra",
        "id": 11,
        "kwargs": [
            "maxVariable=10"
        ],
        "name": "Basic Algebra",
        "samples": [
            {
                "problem": "9x + 3 = 10",
                "solution": "7/9"
            },
            {
                "problem": "4x + 3 = 8",
                "solution": "5/4"
            },
            {
                "problem": "1x + 8 = 9",
                "solution": "1"
            },
            {
                "problem": "1x + 6 = 10",
                "solution": "4"
            },
            {
                "problem": "9x + 6 = 7",
                "solution": "1/9"
            },
            {
                "problem": "10x + 9 = 9",
                "solution": "0"
            },
            {
                "problem": "7x + 6 = 8",
                "solution": "2/7"
            },
            {
                "problem": "9x + 10 = 10",
                "solution": "0"
            },
            {
                "problem": "9x + 5 = 5",
                "solution": "0"
            },
            {
                "problem": "1x + 3 = 8",
                "solution": "5"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "log",
        "id": 12,
        "kwargs": [
            "maxBase=3",
            "maxVal=8"
        ],
        "name": "Logarithm",
        "samples": [
            {
                "problem": "log3(9)",
                "solution": "2"
            },
            {
                "problem": "log3(27)",
                "solution": "3"
            },
            {
                "problem": "log3(81)",
                "solution": "4"
            },
            {
                "problem": "log2(128)",
                "solution": "7"
            },
            {
                "problem": "log2(128)",
                "solution": "7"
            },
            {
                "problem": "log2(4)",
                "solution": "2"
            },
            {
                "problem": "log3(3)",
                "solution": "1"
            },
            {
                "problem": "log2(2)",
                "solution": "1"
            },
            {
                "problem": "log2(16)",
                "solution": "4"
            },
            {
                "problem": "log3(9)",
                "solution": "2"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "complex_division",
        "id": 13,
        "kwargs": [
            "maxRes=99",
            "maxDivid=99"
        ],
        "name": "Complex Division",
        "samples": [
            {
                "problem": "6/36=",
                "solution": "0.17"
            },
            {
                "problem": "58/91=",
                "solution": "0.64"
            },
            {
                "problem": "55/4=",
                "solution": "13.75"
            },
            {
                "problem": "60/39=",
                "solution": "1.54"
            },
            {
                "problem": "2/90=",
                "solution": "0.02"
            },
            {
                "problem": "80/28=",
                "solution": "2.86"
            },
            {
                "problem": "90/36=",
                "solution": "2.5"
            },
            {
                "problem": "0/25=",
                "solution": "0.0"
            },
            {
                "problem": "17/95=",
                "solution": "0.18"
            },
            {
                "problem": "50/80=",
                "solution": "0.62"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "decimal_to_binary",
        "id": 14,
        "kwargs": [
            "max_dec=99"
        ],
        "name": "Decimal to Binary",
        "samples": [
            {
                "problem": "Binary of 11=",
                "solution": "1011"
            },
            {
                "problem": "Binary of 86=",
                "solution": "1010110"
            },
            {
                "problem": "Binary of 95=",
                "solution": "1011111"
            },
            {
                "problem": "Binary of 19=",
                "solution": "10011"
            },
            {
                "problem": "Binary of 10=",
                "solution": "1010"
            },
            {
                "problem": "Binary of 82=",
                "solution": "1010010"
            },
            {
                "problem": "Binary of 44=",
                "solution": "101100"
            },
            {
                "problem": "Binary of 82=",
                "solution": "1010010"
            },
            {
                "problem": "Binary of 53=",
                "solution": "110101"
            },
            {
                "problem": "Binary of 95=",
                "solution": "1011111"
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "binary_to_decimal",
        "id": 15,
        "kwargs": [
            "max_dig=10"
        ],
        "name": "Binary to Decimal",
        "samples": [
            {
                "problem": "010",
                "solution": 2
            },
            {
                "problem": "10110001",
                "solution": 177
            },
            {
                "problem": "0",
                "solution": 0
            },
            {
                "problem": "111",
                "solution": 7
            },
            {
                "problem": "1111010010",
                "solution": 978
            },
            {
                "problem": "1010100101",
                "solution": 677
            },
            {
                "problem": "0001001",
                "solution": 9
            },
            {
                "problem": "0001000011",
                "solution": 67
            },
            {
                "problem": "000110",
                "solution": 6
            },
            {
                "problem": "0001",
                "solution": 1
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "divide_fractions",
        "id": 16,
        "kwargs": [
            "maxVal=10"
        ],
        "name": "Fraction Division",
        "samples": [
            {
                "problem": "(7/6)/(7/10)",
                "solution": "5/3"
            },
            {
                "problem": "(10/9)/(1/7)",
                "solution": "70/9"
            },
            {
                "problem": "(4/7)/(8/10)",
                "solution": "5/7"
            },
            {
                "problem": "(4/10)/(1/9)",
                "solution": "18/5"
            },
            {
                "problem": "(10/8)/(5/9)",
                "solution": "9/4"
            },
            {
                "problem": "(5/1)/(2/5)",
                "solution": "25/2"
            },
            {
                "problem": "(9/2)/(7/5)",
                "solution": "45/14"
            },
            {
                "problem": "(10/9)/(10/1)",
                "solution": "1/9"
            },
            {
                "problem": "(2/7)/(10/8)",
                "solution": "8/35"
            },
            {
                "problem": "(9/2)/(1/4)",
                "solution": "18"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "multiply_int_to_22_matrix",
        "id": 17,
        "kwargs": [
            "maxMatrixVal=10",
            "maxRes=100"
        ],
        "name": "Integer Multiplication with 2x2 Matrix",
        "samples": [
            {
                "problem": "1 * [[3, 1], [7, 1]] = ",
                "solution": "[[3,1],[7,1]]"
            },
            {
                "problem": "9 * [[0, 10], [6, 2]] = ",
                "solution": "[[0,90],[54,18]]"
            },
            {
                "problem": "0 * [[1, 10], [4, 5]] = ",
                "solution": "[[0,0],[0,0]]"
            },
            {
                "problem": "3 * [[1, 5], [10, 8]] = ",
                "solution": "[[3,15],[30,24]]"
            },
            {
                "problem": "8 * [[4, 4], [7, 9]] = ",
                "solution": "[[32,32],[56,72]]"
            },
            {
                "problem": "8 * [[1, 9], [2, 6]] = ",
                "solution": "[[8,72],[16,48]]"
            },
            {
                "problem": "0 * [[9, 3], [3, 2]] = ",
                "solution": "[[0,0],[0,0]]"
            },
            {
                "problem": "12 * [[3, 8], [8, 8]] = ",
                "solution": "[[36,96],[96,96]]"
            },
            {
                "problem": "5 * [[7, 9], [6, 1]] = ",
                "solution": "[[35,45],[30,5]]"
            },
            {
                "problem": "0 * [[0, 9], [9, 4]] = ",
                "solution": "[[0,0],[0,0]]"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "area_of_triangle",
        "id": 18,
        "kwargs": [
            "maxA=20",
            "maxB=20",
            "maxC=20"
        ],
        "name": "Area of Triangle",
        "samples": [
            {
                "problem": "Area of triangle with side lengths: 17 19 1 = ",
                "solution": "(9.541493884968725e-16+15.582442042247422j)"
            },
            {
                "problem": "Area of triangle with side lengths: 17 13 14 = ",
                "solution": "88.99438184514796"
            },
            {
                "problem": "Area of triangle with side lengths: 3 17 17 = ",
                "solution": "25.40054133281415"
            },
            {
                "problem": "Area of triangle with side lengths: 14 17 19 = ",
                "solution": "114.89125293076057"
            },
            {
                "problem": "Area of triangle with side lengths: 14 18 14 = ",
                "solution": "96.51424765287247"
            },
            {
                "problem": "Area of triangle with side lengths: 15 1 20 = ",
                "solution": "(2.623718239906474e-15+42.8485705712571j)"
            },
            {
                "problem": "Area of triangle with side lengths: 15 4 4 = ",
                "solution": "(2.9135673507458437e-15+47.5821657766857j)"
            },
            {
                "problem": "Area of triangle with side lengths: 13 16 20 = ",
                "solution": "103.81202964974725"
            },
            {
                "problem": "Area of triangle with side lengths: 3 14 4 = ",
                "solution": "(2.5917722631556257e-15+42.32685317856738j)"
            },
            {
                "problem": "Area of triangle with side lengths: 10 11 19 = ",
                "solution": "42.42640687119285"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "valid_triangle",
        "id": 19,
        "kwargs": [
            "maxSideLength=50"
        ],
        "name": "Triangle exists check",
        "samples": [
            {
                "problem": "Does triangle with sides 28, 17 and 19 exist?",
                "solution": "Yes"
            },
            {
                "problem": "Does triangle with sides 16, 23 and 2 exist?",
                "solution": "No"
            },
            {
                "problem": "Does triangle with sides 35, 30 and 3 exist?",
                "solution": "No"
            },
            {
                "problem": "Does triangle with sides 39, 8 and 41 exist?",
                "solution": "Yes"
            },
            {
                "problem": "Does triangle with sides 5, 7 and 43 exist?",
                "solution": "No"
            },
            {
                "problem": "Does triangle with sides 45, 31 and 10 exist?",
                "solution": "No"
            },
            {
                "problem": "Does triangle with sides 41, 26 and 37 exist?",
                "solution": "Yes"
            },
            {
                "problem": "Does triangle with sides 6, 27 and 20 exist?",
                "solution": "No"
            },
            {
                "problem": "Does triangle with sides 29, 24 and 13 exist?",
                "solution": "Yes"
            },
            {
                "problem": "Does triangle with sides 29, 19 and 25 exist?",
                "solution": "Yes"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "midpoint_of_two_points",
        "id": 20,
        "kwargs": [
            "maxValue=20"
        ],
        "name": "Midpoint of the two point",
        "samples": [
            {
                "problem": "(-17,-1),(7,2)=",
                "solution": "(-5.0,0.5)"
            },
            {
                "problem": "(-17,16),(16,-19)=",
                "solution": "(-0.5,-1.5)"
            },
            {
                "problem": "(-10,15),(-3,-3)=",
                "solution": "(-6.5,6.0)"
            },
            {
                "problem": "(0,0),(10,-9)=",
                "solution": "(5.0,-4.5)"
            },
            {
                "problem": "(0,13),(-1,-13)=",
                "solution": "(-0.5,0.0)"
            },
            {
                "problem": "(3,-8),(-1,-20)=",
                "solution": "(1.0,-14.0)"
            },
            {
                "problem": "(-6,7),(-17,15)=",
                "solution": "(-11.5,11.0)"
            },
            {
                "problem": "(13,14),(-7,6)=",
                "solution": "(3.0,10.0)"
            },
            {
                "problem": "(-7,-15),(10,9)=",
                "solution": "(1.5,-3.0)"
            },
            {
                "problem": "(5,-6),(-17,-4)=",
                "solution": "(-6.0,-5.0)"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "factoring",
        "id": 21,
        "kwargs": [
            "range_x1=10",
            "range_x2=10"
        ],
        "name": "Factoring Quadratic",
        "samples": [
            {
                "problem": "x^2+9x+8",
                "solution": "(x+1)(x+8)"
            },
            {
                "problem": "x^2-8x",
                "solution": "(x-8)(x)"
            },
            {
                "problem": "x^2+2x-63",
                "solution": "(x-7)(x+9)"
            },
            {
                "problem": "x^2-16",
                "solution": "(x+4)(x-4)"
            },
            {
                "problem": "x^2-2x-80",
                "solution": "(x-10)(x+8)"
            },
            {
                "problem": "x^2-11x+24",
                "solution": "(x-3)(x-8)"
            },
            {
                "problem": "x^2-4x+3",
                "solution": "(x-3)(x-1)"
            },
            {
                "problem": "x^2+5x-14",
                "solution": "(x-2)(x+7)"
            },
            {
                "problem": "x^2+12x+27",
                "solution": "(x+3)(x+9)"
            },
            {
                "problem": "x^2-17x+72",
                "solution": "(x-9)(x-8)"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "third_angle_of_triangle",
        "id": 22,
        "kwargs": [
            "maxAngle=89"
        ],
        "name": "Third Angle of Triangle",
        "samples": [
            {
                "problem": "Third angle of triangle with angles 31 and 56 = ",
                "solution": 93
            },
            {
                "problem": "Third angle of triangle with angles 39 and 33 = ",
                "solution": 108
            },
            {
                "problem": "Third angle of triangle with angles 36 and 26 = ",
                "solution": 118
            },
            {
                "problem": "Third angle of triangle with angles 61 and 7 = ",
                "solution": 112
            },
            {
                "problem": "Third angle of triangle with angles 79 and 55 = ",
                "solution": 46
            },
            {
                "problem": "Third angle of triangle with angles 13 and 16 = ",
                "solution": 151
            },
            {
                "problem": "Third angle of triangle with angles 33 and 26 = ",
                "solution": 121
            },
            {
                "problem": "Third angle of triangle with angles 20 and 85 = ",
                "solution": 75
            },
            {
                "problem": "Third angle of triangle with angles 44 and 71 = ",
                "solution": 65
            },
            {
                "problem": "Third angle of triangle with angles 57 and 77 = ",
                "solution": 46
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "system_of_equations",
        "id": 23,
        "kwargs": [
            "range_x=10",
            "range_y=10",
            "coeff_mult_range=10"
        ],
        "name": "Solve a System of Equations in R^2",
        "samples": [
            {
                "problem": "9x - 2y = 23, 9x + 9y = 45",
                "solution": "x = 3, y = 2"
            },
            {
                "problem": "4x - 5y = 40, -8x + 3y = -80",
                "solution": "x = 10, y = 0"
            },
            {
                "problem": "-3x - 8y = 45, 7x - 7y = -28",
                "solution": "x = -7, y = -3"
            },
            {
                "problem": "5x + y = 46, 2x + 3y = 21",
                "solution": "x = 9, y = 1"
            },
            {
                "problem": "-x - 7y = -43, 4x - 9y = -50",
                "solution": "x = 1, y = 6"
            },
            {
                "problem": "2x - 6y = 44, x +  = 4",
                "solution": "x = 4, y = -6"
            },
            {
                "problem": "-8x + 7y = -126, -5x + 9y = -125",
                "solution": "x = 7, y = -10"
            },
            {
                "problem": "8x - 8y = 0, -5x - y = -54",
                "solution": "x = 9, y = 9"
            },
            {
                "problem": "7x - 7y = 91, -7x +  = -21",
                "solution": "x = 3, y = -10"
            },
            {
                "problem": "-x + 6y = -51, 5x +  = 45",
                "solution": "x = 9, y = -7"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "distance_two_points",
        "id": 24,
        "kwargs": [
            "maxValXY=20",
            "minValXY=-20"
        ],
        "name": "Distance between 2 points",
        "samples": [
            {
                "problem": "Find the distance between (-9, -20) and (15, 16)",
                "solution": "sqrt(1872)"
            },
            {
                "problem": "Find the distance between (14, 18) and (11, 1)",
                "solution": "sqrt(298)"
            },
            {
                "problem": "Find the distance between (20, 10) and (19, 19)",
                "solution": "sqrt(82)"
            },
            {
                "problem": "Find the distance between (9, 0) and (18, 0)",
                "solution": "sqrt(81)"
            },
            {
                "problem": "Find the distance between (-12, -8) and (-7, 10)",
                "solution": "sqrt(349)"
            },
            {
                "problem": "Find the distance between (-3, -16) and (16, -2)",
                "solution": "sqrt(557)"
            },
            {
                "problem": "Find the distance between (-14, -19) and (-18, -1)",
                "solution": "sqrt(340)"
            },
            {
                "problem": "Find the distance between (-19, 21) and (-4, -9)",
                "solution": "sqrt(1125)"
            },
            {
                "problem": "Find the distance between (-6, 16) and (-10, 0)",
                "solution": "sqrt(272)"
            },
            {
                "problem": "Find the distance between (3, -7) and (4, 17)",
                "solution": "sqrt(577)"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "pythagorean_theorem",
        "id": 25,
        "kwargs": [
            "maxLength=20"
        ],
        "name": "Pythagorean Theorem",
        "samples": [
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 18 and 15 = ",
                "solution": "23.43"
            },
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 3 and 15 = ",
                "solution": "15.30"
            },
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 15 and 5 = ",
                "solution": "15.81"
            },
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 12 and 8 = ",
                "solution": "14.42"
            },
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 20 and 5 = ",
                "solution": "20.62"
            },
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 14 and 6 = ",
                "solution": "15.23"
            },
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 7 and 9 = ",
                "solution": "11.40"
            },
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 10 and 4 = ",
                "solution": "10.77"
            },
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 14 and 16 = ",
                "solution": "21.26"
            },
            {
                "problem": "The hypotenuse of a right triangle given the other two lengths 15 and 2 = ",
                "solution": "15.13"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "linear_equations",
        "id": 26,
        "kwargs": [
            "n=2",
            "varRange=20",
            "coeffRange=20"
        ],
        "name": "Linear Equations",
        "samples": [
            {
                "problem": "-13x + 9y = 188, 8x + -10y = -196",
                "solution": "x = -2, y = 18"
            },
            {
                "problem": "-3x + 10y = -47, 2x + 15y = -12",
                "solution": "x = 9, y = -2"
            },
            {
                "problem": "9x + -2y = 160, 9x + -4y = 176",
                "solution": "x = 16, y = -8"
            },
            {
                "problem": "19x + 7y = 58, -16x + -17y = -171",
                "solution": "x = -1, y = 11"
            },
            {
                "problem": "11x + -14y = -11, 11x + -2y = 121",
                "solution": "x = 13, y = 11"
            },
            {
                "problem": "-17x + 10y = 328, -3x + 13y = 159",
                "solution": "x = -14, y = 9"
            },
            {
                "problem": "-10x + -2y = 82, 9x + 7y = -79",
                "solution": "x = -8, y = -1"
            },
            {
                "problem": "-18x + -1y = -333, 15x + -11y = 171",
                "solution": "x = 18, y = 9"
            },
            {
                "problem": "4x + 9y = -105, 4x + 5y = -85",
                "solution": "x = -15, y = -5"
            },
            {
                "problem": "-1x + 4y = 81, -9x + 1y = 64",
                "solution": "x = -5, y = 19"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "prime_factors",
        "id": 27,
        "kwargs": [
            "minVal=1",
            "maxVal=200"
        ],
        "name": "Prime Factorisation",
        "samples": [
            {
                "problem": "Find prime factors of 141",
                "solution": "[3, 47]"
            },
            {
                "problem": "Find prime factors of 104",
                "solution": "[2, 2, 2, 13]"
            },
            {
                "problem": "Find prime factors of 15",
                "solution": "[3, 5]"
            },
            {
                "problem": "Find prime factors of 173",
                "solution": "[173]"
            },
            {
                "problem": "Find prime factors of 169",
                "solution": "[13, 13]"
            },
            {
                "problem": "Find prime factors of 125",
                "solution": "[5, 5, 5]"
            },
            {
                "problem": "Find prime factors of 86",
                "solution": "[2, 43]"
            },
            {
                "problem": "Find prime factors of 25",
                "solution": "[5, 5]"
            },
            {
                "problem": "Find prime factors of 44",
                "solution": "[2, 2, 11]"
            },
            {
                "problem": "Find prime factors of 14",
                "solution": "[2, 7]"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "fraction_multiplication",
        "id": 28,
        "kwargs": [
            "maxVal=10"
        ],
        "name": "Fraction Multiplication",
        "samples": [
            {
                "problem": "(3/2)*(5/9)",
                "solution": "5/6"
            },
            {
                "problem": "(2/9)*(3/9)",
                "solution": "2/27"
            },
            {
                "problem": "(4/3)*(3/10)",
                "solution": "2/5"
            },
            {
                "problem": "(9/10)*(4/8)",
                "solution": "9/20"
            },
            {
                "problem": "(1/6)*(3/4)",
                "solution": "1/8"
            },
            {
                "problem": "(3/1)*(1/2)",
                "solution": "3/2"
            },
            {
                "problem": "(1/8)*(5/7)",
                "solution": "5/56"
            },
            {
                "problem": "(9/6)*(4/5)",
                "solution": "6/5"
            },
            {
                "problem": "(6/9)*(5/4)",
                "solution": "5/6"
            },
            {
                "problem": "(1/10)*(6/4)",
                "solution": "3/20"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "angle_regular_polygon",
        "id": 29,
        "kwargs": [
            "minVal=3",
            "maxVal=20"
        ],
        "name": "Angle of a Regular Polygon",
        "samples": [
            {
                "problem": "Find the angle of a regular polygon with 15 sides",
                "solution": 156.0
            },
            {
                "problem": "Find the angle of a regular polygon with 16 sides",
                "solution": 157.5
            },
            {
                "problem": "Find the angle of a regular polygon with 19 sides",
                "solution": 161.05
            },
            {
                "problem": "Find the angle of a regular polygon with 9 sides",
                "solution": 140.0
            },
            {
                "problem": "Find the angle of a regular polygon with 12 sides",
                "solution": 150.0
            },
            {
                "problem": "Find the angle of a regular polygon with 20 sides",
                "solution": 162.0
            },
            {
                "problem": "Find the angle of a regular polygon with 4 sides",
                "solution": 90.0
            },
            {
                "problem": "Find the angle of a regular polygon with 13 sides",
                "solution": 152.31
            },
            {
                "problem": "Find the angle of a regular polygon with 5 sides",
                "solution": 108.0
            },
            {
                "problem": "Find the angle of a regular polygon with 5 sides",
                "solution": 108.0
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "combinations",
        "id": 30,
        "kwargs": [
            "maxlength=20"
        ],
        "name": "Combinations of Objects",
        "samples": [
            {
                "problem": "Number of combinations from 16 objects picked 6 at a time ",
                "solution": 8008
            },
            {
                "problem": "Number of combinations from 13 objects picked 1 at a time ",
                "solution": 13
            },
            {
                "problem": "Number of combinations from 16 objects picked 4 at a time ",
                "solution": 1820
            },
            {
                "problem": "Number of combinations from 20 objects picked 2 at a time ",
                "solution": 190
            },
            {
                "problem": "Number of combinations from 17 objects picked 3 at a time ",
                "solution": 680
            },
            {
                "problem": "Number of combinations from 13 objects picked 3 at a time ",
                "solution": 286
            },
            {
                "problem": "Number of combinations from 19 objects picked 1 at a time ",
                "solution": 19
            },
            {
                "problem": "Number of combinations from 11 objects picked 6 at a time ",
                "solution": 462
            },
            {
                "problem": "Number of combinations from 19 objects picked 8 at a time ",
                "solution": 75582
            },
            {
                "problem": "Number of combinations from 17 objects picked 7 at a time ",
                "solution": 19448
            }
        ],
        "subject": "statistics"
    },
    {
        "function_name": "factorial",
        "id": 31,
        "kwargs": [
            "maxInput=6"
        ],
        "name": "Factorial",
        "samples": [
            {
                "problem": "0! = ",
                "solution": "1"
            },
            {
                "problem": "5! = ",
                "solution": "120"
            },
            {
                "problem": "0! = ",
                "solution": "1"
            },
            {
                "problem": "1! = ",
                "solution": "1"
            },
            {
                "problem": "5! = ",
                "solution": "120"
            },
            {
                "problem": "5! = ",
                "solution": "120"
            },
            {
                "problem": "6! = ",
                "solution": "720"
            },
            {
                "problem": "0! = ",
                "solution": "1"
            },
            {
                "problem": "1! = ",
                "solution": "1"
            },
            {
                "problem": "2! = ",
                "solution": "2"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "surface_area_cube",
        "id": 32,
        "kwargs": [
            "maxSide=20",
            "unit='m'"
        ],
        "name": "Surface Area of Cube",
        "samples": [
            {
                "problem": "Surface area of cube with side = 18m is",
                "solution": "1944 m^2"
            },
            {
                "problem": "Surface area of cube with side = 4m is",
                "solution": "96 m^2"
            },
            {
                "problem": "Surface area of cube with side = 1m is",
                "solution": "6 m^2"
            },
            {
                "problem": "Surface area of cube with side = 14m is",
                "solution": "1176 m^2"
            },
            {
                "problem": "Surface area of cube with side = 2m is",
                "solution": "24 m^2"
            },
            {
                "problem": "Surface area of cube with side = 1m is",
                "solution": "6 m^2"
            },
            {
                "problem": "Surface area of cube with side = 6m is",
                "solution": "216 m^2"
            },
            {
                "problem": "Surface area of cube with side = 4m is",
                "solution": "96 m^2"
            },
            {
                "problem": "Surface area of cube with side = 11m is",
                "solution": "726 m^2"
            },
            {
                "problem": "Surface area of cube with side = 16m is",
                "solution": "1536 m^2"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "surface_area_cuboid",
        "id": 33,
        "kwargs": [
            "maxSide=20",
            "unit='m'"
        ],
        "name": "Surface Area of Cuboid",
        "samples": [
            {
                "problem": "Surface area of cuboid with sides = 13m, 12m, 13m is",
                "solution": "962 m^2"
            },
            {
                "problem": "Surface area of cuboid with sides = 15m, 6m, 19m is",
                "solution": "978 m^2"
            },
            {
                "problem": "Surface area of cuboid with sides = 19m, 5m, 7m is",
                "solution": "526 m^2"
            },
            {
                "problem": "Surface area of cuboid with sides = 2m, 7m, 1m is",
                "solution": "46 m^2"
            },
            {
                "problem": "Surface area of cuboid with sides = 17m, 10m, 9m is",
                "solution": "826 m^2"
            },
            {
                "problem": "Surface area of cuboid with sides = 13m, 11m, 18m is",
                "solution": "1150 m^2"
            },
            {
                "problem": "Surface area of cuboid with sides = 12m, 17m, 2m is",
                "solution": "524 m^2"
            },
            {
                "problem": "Surface area of cuboid with sides = 20m, 9m, 3m is",
                "solution": "534 m^2"
            },
            {
                "problem": "Surface area of cuboid with sides = 4m, 18m, 5m is",
                "solution": "364 m^2"
            },
            {
                "problem": "Surface area of cuboid with sides = 1m, 2m, 3m is",
                "solution": "22 m^2"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "surface_area_cylinder",
        "id": 34,
        "kwargs": [
            "maxRadius=20",
            "maxHeight=50",
            "unit='m'"
        ],
        "name": "Surface Area of Cylinder",
        "samples": [
            {
                "problem": "Surface area of cylinder with height = 16m and radius = 18m is",
                "solution": "3845 m^2"
            },
            {
                "problem": "Surface area of cylinder with height = 12m and radius = 16m is",
                "solution": "2814 m^2"
            },
            {
                "problem": "Surface area of cylinder with height = 9m and radius = 12m is",
                "solution": "1583 m^2"
            },
            {
                "problem": "Surface area of cylinder with height = 6m and radius = 6m is",
                "solution": "452 m^2"
            },
            {
                "problem": "Surface area of cylinder with height = 37m and radius = 10m is",
                "solution": "2953 m^2"
            },
            {
                "problem": "Surface area of cylinder with height = 6m and radius = 4m is",
                "solution": "251 m^2"
            },
            {
                "problem": "Surface area of cylinder with height = 34m and radius = 5m is",
                "solution": "1225 m^2"
            },
            {
                "problem": "Surface area of cylinder with height = 35m and radius = 18m is",
                "solution": "5994 m^2"
            },
            {
                "problem": "Surface area of cylinder with height = 44m and radius = 10m is",
                "solution": "3392 m^2"
            },
            {
                "problem": "Surface area of cylinder with height = 35m and radius = 13m is",
                "solution": "3920 m^2"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "volume_cube",
        "id": 35,
        "kwargs": [
            "maxSide=20",
            "unit='m'"
        ],
        "name": "Volum of Cube",
        "samples": [
            {
                "problem": "Volume of cube with side = 7m is",
                "solution": "343 m^3"
            },
            {
                "problem": "Volume of cube with side = 13m is",
                "solution": "2197 m^3"
            },
            {
                "problem": "Volume of cube with side = 3m is",
                "solution": "27 m^3"
            },
            {
                "problem": "Volume of cube with side = 2m is",
                "solution": "8 m^3"
            },
            {
                "problem": "Volume of cube with side = 19m is",
                "solution": "6859 m^3"
            },
            {
                "problem": "Volume of cube with side = 14m is",
                "solution": "2744 m^3"
            },
            {
                "problem": "Volume of cube with side = 6m is",
                "solution": "216 m^3"
            },
            {
                "problem": "Volume of cube with side = 13m is",
                "solution": "2197 m^3"
            },
            {
                "problem": "Volume of cube with side = 9m is",
                "solution": "729 m^3"
            },
            {
                "problem": "Volume of cube with side = 5m is",
                "solution": "125 m^3"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "volume_cuboid",
        "id": 36,
        "kwargs": [
            "maxSide=20",
            "unit='m'"
        ],
        "name": "Volume of Cuboid",
        "samples": [
            {
                "problem": "Volume of cuboid with sides = 16m, 9m, 14m is",
                "solution": "2016 m^3"
            },
            {
                "problem": "Volume of cuboid with sides = 18m, 14m, 14m is",
                "solution": "3528 m^3"
            },
            {
                "problem": "Volume of cuboid with sides = 16m, 2m, 9m is",
                "solution": "288 m^3"
            },
            {
                "problem": "Volume of cuboid with sides = 7m, 2m, 11m is",
                "solution": "154 m^3"
            },
            {
                "problem": "Volume of cuboid with sides = 1m, 15m, 3m is",
                "solution": "45 m^3"
            },
            {
                "problem": "Volume of cuboid with sides = 18m, 6m, 14m is",
                "solution": "1512 m^3"
            },
            {
                "problem": "Volume of cuboid with sides = 12m, 8m, 2m is",
                "solution": "192 m^3"
            },
            {
                "problem": "Volume of cuboid with sides = 3m, 16m, 19m is",
                "solution": "912 m^3"
            },
            {
                "problem": "Volume of cuboid with sides = 20m, 18m, 10m is",
                "solution": "3600 m^3"
            },
            {
                "problem": "Volume of cuboid with sides = 13m, 15m, 12m is",
                "solution": "2340 m^3"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "volume_cylinder",
        "id": 37,
        "kwargs": [
            "maxRadius=20",
            "maxHeight=50",
            "unit='m'"
        ],
        "name": "Volume of cylinder",
        "samples": [
            {
                "problem": "Volume of cylinder with height = 37m and radius = 15m is",
                "solution": "26153 m^3"
            },
            {
                "problem": "Volume of cylinder with height = 50m and radius = 18m is",
                "solution": "50893 m^3"
            },
            {
                "problem": "Volume of cylinder with height = 9m and radius = 14m is",
                "solution": "5541 m^3"
            },
            {
                "problem": "Volume of cylinder with height = 22m and radius = 7m is",
                "solution": "3386 m^3"
            },
            {
                "problem": "Volume of cylinder with height = 23m and radius = 14m is",
                "solution": "14162 m^3"
            },
            {
                "problem": "Volume of cylinder with height = 18m and radius = 8m is",
                "solution": "3619 m^3"
            },
            {
                "problem": "Volume of cylinder with height = 27m and radius = 7m is",
                "solution": "4156 m^3"
            },
            {
                "problem": "Volume of cylinder with height = 45m and radius = 2m is",
                "solution": "565 m^3"
            },
            {
                "problem": "Volume of cylinder with height = 46m and radius = 14m is",
                "solution": "28324 m^3"
            },
            {
                "problem": "Volume of cylinder with height = 34m and radius = 2m is",
                "solution": "427 m^3"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "surface_area_cone",
        "id": 38,
        "kwargs": [
            "maxRadius=20",
            "maxHeight=50",
            "unit='m'"
        ],
        "name": "Surface Area of cone",
        "samples": [
            {
                "problem": "Surface area of cone with height = 1m and radius = 5m is",
                "solution": "158 m^2"
            },
            {
                "problem": "Surface area of cone with height = 21m and radius = 20m is",
                "solution": "3078 m^2"
            },
            {
                "problem": "Surface area of cone with height = 44m and radius = 16m is",
                "solution": "3157 m^2"
            },
            {
                "problem": "Surface area of cone with height = 14m and radius = 2m is",
                "solution": "101 m^2"
            },
            {
                "problem": "Surface area of cone with height = 9m and radius = 17m is",
                "solution": "1935 m^2"
            },
            {
                "problem": "Surface area of cone with height = 41m and radius = 3m is",
                "solution": "415 m^2"
            },
            {
                "problem": "Surface area of cone with height = 14m and radius = 8m is",
                "solution": "606 m^2"
            },
            {
                "problem": "Surface area of cone with height = 18m and radius = 9m is",
                "solution": "823 m^2"
            },
            {
                "problem": "Surface area of cone with height = 7m and radius = 4m is",
                "solution": "151 m^2"
            },
            {
                "problem": "Surface area of cone with height = 7m and radius = 13m is",
                "solution": "1133 m^2"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "volume_cone",
        "id": 39,
        "kwargs": [
            "maxRadius=20",
            "maxHeight=50",
            "unit='m'"
        ],
        "name": "Volume of cone",
        "samples": [
            {
                "problem": "Volume of cone with height = 4m and radius = 20m is",
                "solution": "1675 m^3"
            },
            {
                "problem": "Volume of cone with height = 4m and radius = 19m is",
                "solution": "1512 m^3"
            },
            {
                "problem": "Volume of cone with height = 40m and radius = 8m is",
                "solution": "2680 m^3"
            },
            {
                "problem": "Volume of cone with height = 39m and radius = 1m is",
                "solution": "40 m^3"
            },
            {
                "problem": "Volume of cone with height = 20m and radius = 14m is",
                "solution": "4105 m^3"
            },
            {
                "problem": "Volume of cone with height = 2m and radius = 2m is",
                "solution": "8 m^3"
            },
            {
                "problem": "Volume of cone with height = 3m and radius = 20m is",
                "solution": "1256 m^3"
            },
            {
                "problem": "Volume of cone with height = 40m and radius = 3m is",
                "solution": "376 m^3"
            },
            {
                "problem": "Volume of cone with height = 47m and radius = 20m is",
                "solution": "19687 m^3"
            },
            {
                "problem": "Volume of cone with height = 41m and radius = 11m is",
                "solution": "5195 m^3"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "common_factors",
        "id": 40,
        "kwargs": [
            "maxVal=100"
        ],
        "name": "Common Factors",
        "samples": [
            {
                "problem": "Common Factors of 56 and 37 = ",
                "solution": [
                    1
                ]
            },
            {
                "problem": "Common Factors of 68 and 86 = ",
                "solution": [
                    1,
                    2
                ]
            },
            {
                "problem": "Common Factors of 94 and 89 = ",
                "solution": [
                    1
                ]
            },
            {
                "problem": "Common Factors of 35 and 51 = ",
                "solution": [
                    1
                ]
            },
            {
                "problem": "Common Factors of 60 and 72 = ",
                "solution": [
                    1,
                    2,
                    3,
                    4,
                    6,
                    12
                ]
            },
            {
                "problem": "Common Factors of 58 and 42 = ",
                "solution": [
                    1,
                    2
                ]
            },
            {
                "problem": "Common Factors of 38 and 39 = ",
                "solution": [
                    1
                ]
            },
            {
                "problem": "Common Factors of 40 and 77 = ",
                "solution": [
                    1
                ]
            },
            {
                "problem": "Common Factors of 27 and 33 = ",
                "solution": [
                    1,
                    3
                ]
            },
            {
                "problem": "Common Factors of 20 and 54 = ",
                "solution": [
                    1,
                    2
                ]
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "intersection_of_two_lines",
        "id": 41,
        "kwargs": [
            "minM=-10",
            "maxM=10",
            "minB=-10",
            "maxB=10",
            "minDenominator=1",
            "maxDenominator=6"
        ],
        "name": "Intersection of Two Lines",
        "samples": [
            {
                "problem": "Find the point of intersection of the two lines: y = -10/6x - 7 and y = 8/3x - 3",
                "solution": "(-12/13, -71/13)"
            },
            {
                "problem": "Find the point of intersection of the two lines: y = 5/6x + 4 and y = 7/5x + 2",
                "solution": "(60/17, 118/17)"
            },
            {
                "problem": "Find the point of intersection of the two lines: y = -8/3x - 10 and y = 5x - 7",
                "solution": "(-9/23, -206/23)"
            },
            {
                "problem": "Find the point of intersection of the two lines: y = -10x + 8 and y = 3/3x + 2",
                "solution": "(6/11, 28/11)"
            },
            {
                "problem": "Find the point of intersection of the two lines: y = 0/4x + 1 and y = 10/2x + 1",
                "solution": "(0, 1)"
            },
            {
                "problem": "Find the point of intersection of the two lines: y = 5/4x + 8 and y = 9x - 3",
                "solution": "(44/31, 303/31)"
            },
            {
                "problem": "Find the point of intersection of the two lines: y = -7/3x - 3 and y = -4/5x + 4",
                "solution": "(-105/23, 176/23)"
            },
            {
                "problem": "Find the point of intersection of the two lines: y = 3/2x - 2 and y = -1/5x - 6",
                "solution": "(-40/17, -94/17)"
            },
            {
                "problem": "Find the point of intersection of the two lines: y = 6x + 10 and y = 8/4x + 4",
                "solution": "(-3/2, 1)"
            },
            {
                "problem": "Find the point of intersection of the two lines: y = -5/5x - 9 and y = -4/3x - 8",
                "solution": "(3, -12)"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "permutation",
        "id": 42,
        "kwargs": [
            "maxlength=20"
        ],
        "name": "Permutations",
        "samples": [
            {
                "problem": "Number of Permutations from 16 objects picked 4 at a time =  ",
                "solution": 43680
            },
            {
                "problem": "Number of Permutations from 19 objects picked 3 at a time =  ",
                "solution": 5814
            },
            {
                "problem": "Number of Permutations from 18 objects picked 5 at a time =  ",
                "solution": 1028160
            },
            {
                "problem": "Number of Permutations from 11 objects picked 5 at a time =  ",
                "solution": 55440
            },
            {
                "problem": "Number of Permutations from 11 objects picked 8 at a time =  ",
                "solution": 6652800
            },
            {
                "problem": "Number of Permutations from 14 objects picked 9 at a time =  ",
                "solution": 726485760
            },
            {
                "problem": "Number of Permutations from 12 objects picked 3 at a time =  ",
                "solution": 1320
            },
            {
                "problem": "Number of Permutations from 16 objects picked 2 at a time =  ",
                "solution": 240
            },
            {
                "problem": "Number of Permutations from 13 objects picked 7 at a time =  ",
                "solution": 8648640
            },
            {
                "problem": "Number of Permutations from 18 objects picked 7 at a time =  ",
                "solution": 160392960
            }
        ],
        "subject": "statistics"
    },
    {
        "function_name": "vector_cross",
        "id": 43,
        "kwargs": [
            "minVal=-20",
            "maxVal=20"
        ],
        "name": "Cross Product of 2 Vectors",
        "samples": [
            {
                "problem": "[17, 0, -2] X [-10, -2, -2] = ",
                "solution": "[-4, 54, -34]"
            },
            {
                "problem": "[-20, 15, -15] X [2, -17, -19] = ",
                "solution": "[-540, -410, 310]"
            },
            {
                "problem": "[4, -10, 16] X [-5, -7, 13] = ",
                "solution": "[-18, -132, -78]"
            },
            {
                "problem": "[-6, 10, -9] X [-4, -1, 13] = ",
                "solution": "[121, 114, 46]"
            },
            {
                "problem": "[3, 13, 5] X [0, 14, -18] = ",
                "solution": "[-304, 54, 42]"
            },
            {
                "problem": "[-7, 1, -9] X [17, 5, 16] = ",
                "solution": "[61, -41, -52]"
            },
            {
                "problem": "[-1, 8, -13] X [6, -7, 2] = ",
                "solution": "[-75, -76, -41]"
            },
            {
                "problem": "[-2, -12, 10] X [3, 15, 10] = ",
                "solution": "[-270, 50, 6]"
            },
            {
                "problem": "[9, 10, 4] X [-19, 19, 2] = ",
                "solution": "[-56, -94, 361]"
            },
            {
                "problem": "[20, 5, 5] X [9, 3, -14] = ",
                "solution": "[-85, 325, 15]"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "compare_fractions",
        "id": 44,
        "kwargs": [
            "maxVal=10"
        ],
        "name": "Compare Fractions",
        "samples": [
            {
                "problem": "Which symbol represents the comparison between 1/2 and 7/4?",
                "solution": "<"
            },
            {
                "problem": "Which symbol represents the comparison between 8/6 and 9/10?",
                "solution": ">"
            },
            {
                "problem": "Which symbol represents the comparison between 8/7 and 3/1?",
                "solution": "<"
            },
            {
                "problem": "Which symbol represents the comparison between 6/4 and 3/9?",
                "solution": ">"
            },
            {
                "problem": "Which symbol represents the comparison between 5/4 and 7/3?",
                "solution": "<"
            },
            {
                "problem": "Which symbol represents the comparison between 3/6 and 8/2?",
                "solution": "<"
            },
            {
                "problem": "Which symbol represents the comparison between 10/2 and 9/7?",
                "solution": ">"
            },
            {
                "problem": "Which symbol represents the comparison between 8/9 and 7/3?",
                "solution": "<"
            },
            {
                "problem": "Which symbol represents the comparison between 2/3 and 3/7?",
                "solution": ">"
            },
            {
                "problem": "Which symbol represents the comparison between 8/2 and 6/9?",
                "solution": ">"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "simple_interest",
        "id": 45,
        "kwargs": [
            "maxPrinciple=10000",
            "maxRate=10",
            "maxTime=10"
        ],
        "name": "Simple Interest",
        "samples": [
            {
                "problem": "Simple interest for a principle amount of 7217 dollars, 9% rate of interest and for a time period of 10 years is = ",
                "solution": 6495.3
            },
            {
                "problem": "Simple interest for a principle amount of 8597 dollars, 6% rate of interest and for a time period of 1 years is = ",
                "solution": 515.82
            },
            {
                "problem": "Simple interest for a principle amount of 4010 dollars, 8% rate of interest and for a time period of 7 years is = ",
                "solution": 2245.6
            },
            {
                "problem": "Simple interest for a principle amount of 2754 dollars, 10% rate of interest and for a time period of 9 years is = ",
                "solution": 2478.6
            },
            {
                "problem": "Simple interest for a principle amount of 4678 dollars, 6% rate of interest and for a time period of 6 years is = ",
                "solution": 1684.08
            },
            {
                "problem": "Simple interest for a principle amount of 8776 dollars, 4% rate of interest and for a time period of 5 years is = ",
                "solution": 1755.2
            },
            {
                "problem": "Simple interest for a principle amount of 4773 dollars, 9% rate of interest and for a time period of 7 years is = ",
                "solution": 3006.99
            },
            {
                "problem": "Simple interest for a principle amount of 6810 dollars, 7% rate of interest and for a time period of 3 years is = ",
                "solution": 1430.1
            },
            {
                "problem": "Simple interest for a principle amount of 3839 dollars, 4% rate of interest and for a time period of 5 years is = ",
                "solution": 767.8
            },
            {
                "problem": "Simple interest for a principle amount of 5532 dollars, 4% rate of interest and for a time period of 3 years is = ",
                "solution": 663.84
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "matrix_multiplication",
        "id": 46,
        "kwargs": [
            "maxVal=100",
            "max_dim=10"
        ],
        "name": "Multiplication of two matrices",
        "samples": [
            {
                "problem": "Multiply \n[[     3,    -16,     94,     78,    -79,     65,    -68,    -64,     71]\n [    57,    -24,     79,     49,    -14,    -12,    -74,    -53,    -22]\n [    39,    -96,    -83,     -7,     92,    -18,     78,    -85,      3]\n [    66,     93,   -100,    -98,     95,    -28,     33,     36,    -24]\n [   -95,     -9,     36,    -53,    -94,     94,     -4,    -59,    -27]\n [    59,    -70,     26,     19,    -97,    -86,    -50,      1,    -46]\n [   -90,    -82,    -18,    -78,     76,     55,   -100,     85,    -48]\n [     7,     -5,     35,     70,    -30,    -57,     84,    -29,    -86]\n [   -64,    -49,     44,    -65,     46,     96,     42,     87,     63]]\n and \n\n[[    23,     46,    -51,    100,    -56,     32]\n [   -19,     26,     -5,     60,    -83,    -36]\n [   -77,     80,    -16,     64,     21,     98]\n [   -28,     49,    -38,    -27,     96,    -66]\n [   -21,   -100,    -37,     66,     86,     13]\n [   -28,    -12,    -44,    -24,     49,    -42]\n [    48,    -29,    -78,    -79,    -27,    -80]\n [   -35,    -97,     41,     31,   -100,     24]\n [   -59,     -3,     13,    -46,    -88,      6]]",
                "solution": "[[-14423,  26151,   -875,  -3402,   9001,   5309]\n [ -5457,  19616,  -1554,  12572,  12605,  12034]\n [ 14422, -10695, -12057,  -9414,  16529,  -9278]\n [ 10724, -20889,  -2200,  14981, -18504,  -4077]\n [  -494,   9871,   3212, -15036,   6641,  -2118]\n [  4877,  16128,   6919,   4610,  -2382,  11801]\n [ -5021, -24995,  13681,   3473,  11635,  11886]\n [  7948,  10741,  -8793,  -3441,  10305,  -6714]\n [-10509, -19481,    459,  -7556,  -4383,   3990]]"
            },
            {
                "problem": "Multiply \n[[    28,    -66,     17,    -96,     -8]\n [   -64,    -48,   -100,     33,    -39]]\n and \n\n[[   -47,    -49]\n [    58,     92]\n [   -76,     11]\n [   -56,    -21]\n [   -68,    -47]]",
                "solution": "[[  -516,  -4865]\n [  8628,  -1240]]"
            },
            {
                "problem": "Multiply \n[[   -32,    -80]\n [   -65,     67]]\n and \n\n[[     2,     53,    -23,     56,     -5,     87,    -50,     84]\n [    25,    -14,    -78,    -49,     37,     97,    -93,     28]]",
                "solution": "[[ -2064,   -576,   6976,   2128,  -2800, -10544,   9040,  -4928]\n [  1545,  -4383,  -3731,  -6923,   2804,    844,  -2981,  -3584]]"
            },
            {
                "problem": "Multiply \n[[    49,    -35,     82,     66,     11]\n [   -55,    -94,    -70,    -24,    -18]\n [    48,     63,    -36,     59,    -81]]\n and \n\n[[    89,     49,      4,    -29,    -50,     51,     38,    -56,    -86,     12]\n [   -54,     65,    -19,     43,     70,     47,     84,    -19,    -38,     14]\n [     2,     10,    -41,    -34,     21,     27,     41,     61,    -14,     22]\n [   -60,     48,    -67,    -43,    -66,     -1,     -6,     22,    -94,     17]\n [   -22,     94,     57,    -72,     94,    -66,    -71,    -54,     29,    -92]]",
                "solution": "[[  2213,   5148,  -6296,  -9344,  -6500,   2276,   1107,   3781,  -9917,   2012]\n [  1877, -12349,   5018,   2261,  -5408,  -7901, -11434,   1040,  11016,  -2268]\n [  -960,   1305,  -8099,   5836, -10254,   9724,  11037,   -409, -13913,   9121]]"
            },
            {
                "problem": "Multiply \n[[   -38,     20,    -21,    -87]\n [    38,    -36,    -10,     56]\n [    96,     -9,    -85,    -43]]\n and \n\n[[    91,    -18,    -19,    -27,    -55,     10,     24,    -12]\n [    11,     55,     79,     -1,     19,     19,    -26,    -23]\n [    -8,     80,      9,     32,    -87,     85,    -29,    -34]\n [   -93,     27,     11,     -9,    -80,     68,     36,    -14]]",
                "solution": "[[  5021,  -2245,   1156,   1117,  11257,  -7701,  -3955,   1928]\n [ -2066,  -1952,  -3040,  -1814,  -6384,   2654,   4154,    -72]\n [ 13316, -10184,  -3773,  -4916,   5384,  -9360,   3455,   2547]]"
            },
            {
                "problem": "Multiply \n[[   -63,    -52,    -33,    -41,     87]\n [   -42,    -96,     14,     15,     44]\n [    51,    -69,     41,     -4,     22]\n [   -63,     87,     75,     62,   -100]\n [   -99,    -59,     94,    -87,    -91]\n [    32,     41,    -28,    -97,    -86]\n [    30,     53,     65,     20,     47]\n [    82,     77,     53,    -32,    -11]]\n and \n\n[[   -41,     91,     28,    -45,    -80,    -90,     33,     42]\n [   -17,     43,     50,    -29,     30,     55,     35,    -47]\n [    70,     83,     81,    -82,    -92,    -62,     81,     16]\n [   -86,     79,     62,    -56,     32,    -18,     -5,     52]\n [     5,     76,    -89,    -76,    -61,     54,     53,     77]]",
                "solution": "[[  5118,  -7335, -17322,   2733,   -103,  10292,  -1756,   3837]\n [  3264,  -2259,  -7828,   -658,  -3012,   -262,  -1355,   7140]\n [  2406,   6433,   -907,  -5104, -11392,  -9667,   3775,   7527]\n [   522,   1531,  21405,  -1710,   8834,   -711,   1431, -10011]\n [ 18669, -17533,   4597,  10246,    269,  -3511,  -2106, -11412]\n [  3943, -11848,   2318,  11635,   3388,  -1787,  -3850, -12697]\n [   934,  15556,   5812, -12909,  -9017,  -1637,  10501,   4468]\n [  1736,  11808,   9434,  -7641,  -9479,  -6449,   9271,  -1838]]"
            },
            {
                "problem": "Multiply \n[[   100,    -56,     97,    -51,    -79,     47,     -5]\n [    -8,    -53,    -36,     20,    -88,   -100,     11]\n [   -20,     13,    -51,     -6,    -96,    -38,    100]\n [   -25,    -51,    -23,    -66,     -5,      9,    -36]\n [   -34,    -89,     -4,    -96,    -24,    -99,    -21]]\n and \n\n[[     4,    -82,     15,    -37,    -92,     96]\n [   -83,    -81,    -65,      5,     24,    -85]\n [    91,     20,    -92,     99,     30,     56]\n [   -21,    -81,     39,    -50,     17,    -97]\n [    63,     97,    -17,    -79,    -30,     -8]\n [    -3,    -51,    -57,    -31,    -69,     18]\n [   -34,    -60,     95,     12,     27,     35]]",
                "solution": "[[  9998,  -7353,  -7584,  12897,  -9509,  26042]\n [ -4947,  -1487,  15658,   5651,   8561,   -930]\n [-15008, -13321,  16611,   6018,   8722,  -1715]\n [  4308,  12283,  -1366,   1377,  -2179,   5991]\n [  8402,  21674,   5955,   9930,   6224,  11064]]"
            },
            {
                "problem": "Multiply \n[[    30,    -11,    -12,     30,     70,    -63]\n [   -43,     58,     75,    -11,    -97,    -66]\n [    66,     65,     71,    -47,      2,      3]\n [    14,     60,    -29,    -34,      8,    -86]\n [   -79,    -15,     62,     -9,    -48,     87]\n [    73,     96,      7,     38,    -54,      0]\n [   -52,    -12,     30,    -38,    -15,    -99]\n [   -57,      5,    -89,     39,      1,     18]\n [    -7,    -57,     11,     26,    -41,    -69]]\n and \n\n[[   -35,    -40,    -80,    -13]\n [   -13,     96,     26,     14]\n [   -89,    -42,    -16,    -56]\n [    84,    -53,    -54,     -7]\n [    -8,    -16,    -39,     96]\n [   -90,     79,     74,    -23]]",
                "solution": "[[  7791,  -9439, -11506,   8087]\n [  -132,   1059,   3241, -10546]\n [-13708,   3314,  -2044,  -3472]\n [  6131,   1298,  -3936,   5266]\n [-10760,   7234,  13734,  -9201]\n [  -802,   4852,  -3402,  -5447]\n [  5144,  -5899,  -1321,    -69]\n [ 11499,   5837,   5301,   5204]\n [  8729, -11827,  -6009,  -3854]]"
            },
            {
                "problem": "Multiply \n[[    90,     20,     39,    -83,    -51]\n [   -46,     31,     85,      2,    -69]\n [   -90,     12,     52,     48,     58]]\n and \n\n[[    28,    -55,    -74,    -80,    -65,      6]\n [   -27,     89,     81,    -57,    -48,    -35]\n [   -70,     35,    -20,     98,    -50,     25]\n [   -85,     88,    100,    -99,     81,     11]\n [    87,     43,    -81,     13,    -10,    -60]]",
                "solution": "[[  1868, -11302,  -9989,   3036, -14973,   2962]\n [-14248,   5473,  10004,   9148,  -1896,   4926]\n [ -5518,  14556,   6694,   7614,   5982,  -2612]]"
            },
            {
                "problem": "Multiply \n[[   -27,     26,    -86,    -74,     -3,      2]\n [    -8,     11,    -31,     42,     90,    -11]]\n and \n\n[[    23,    -38,    -45,     15]\n [    49,    -35,     23,    -75]\n [    57,    -26,     -7,     38]\n [    30,    -28,    -22,     74]\n [   -26,    -69,     88,     16]\n [    61,     17,    -61,     31]]",
                "solution": "[[ -6269,   4665,   3657, -11085]\n [ -3163,  -6848,   8497,   2084]]"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "cube_root",
        "id": 47,
        "kwargs": [
            "minNo=1",
            "maxNo=1000"
        ],
        "name": "Cube Root",
        "samples": [
            {
                "problem": "What is the cube root of 647 up to 2 decimal places?",
                "solution": "8.65"
            },
            {
                "problem": "What is the cube root of 794 up to 2 decimal places?",
                "solution": "9.26"
            },
            {
                "problem": "What is the cube root of 398 up to 2 decimal places?",
                "solution": "7.36"
            },
            {
                "problem": "What is the cube root of 484 up to 2 decimal places?",
                "solution": "7.85"
            },
            {
                "problem": "What is the cube root of 10 up to 2 decimal places?",
                "solution": "2.15"
            },
            {
                "problem": "What is the cube root of 255 up to 2 decimal places?",
                "solution": "6.34"
            },
            {
                "problem": "What is the cube root of 281 up to 2 decimal places?",
                "solution": "6.55"
            },
            {
                "problem": "What is the cube root of 379 up to 2 decimal places?",
                "solution": "7.24"
            },
            {
                "problem": "What is the cube root of 880 up to 2 decimal places?",
                "solution": "9.58"
            },
            {
                "problem": "What is the cube root of 576 up to 2 decimal places?",
                "solution": "8.32"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "power_rule_integration",
        "id": 48,
        "kwargs": [
            "maxCoef=10",
            "maxExp=10",
            "maxTerms=5"
        ],
        "name": "Power Rule Integration",
        "samples": [
            {
                "problem": "1x^9 + 3x^9 + 4x^9",
                "solution": "(1/9)x^10 + (3/9)x^10 + (4/9)x^10 + c"
            },
            {
                "problem": "7x^4 + 8x^5 + 6x^4 + 2x^4",
                "solution": "(7/4)x^5 + (8/5)x^6 + (6/4)x^5 + (2/4)x^5 + c"
            },
            {
                "problem": "3x^4",
                "solution": "(3/4)x^5 + c"
            },
            {
                "problem": "2x^2",
                "solution": "(2/2)x^3 + c"
            },
            {
                "problem": "9x^7 + 1x^4 + 1x^5 + 2x^5",
                "solution": "(9/7)x^8 + (1/4)x^5 + (1/5)x^6 + (2/5)x^6 + c"
            },
            {
                "problem": "5x^1 + 3x^1 + 9x^3",
                "solution": "(5/1)x^2 + (3/1)x^2 + (9/3)x^4 + c"
            },
            {
                "problem": "10x^6 + 2x^5 + 4x^2 + 4x^2 + 1x^7",
                "solution": "(10/6)x^7 + (2/5)x^6 + (4/2)x^3 + (4/2)x^3 + (1/7)x^8 + c"
            },
            {
                "problem": "10x^10 + 2x^9",
                "solution": "(10/10)x^11 + (2/9)x^10 + c"
            },
            {
                "problem": "6x^4 + 1x^4 + 4x^2 + 6x^8 + 2x^6",
                "solution": "(6/4)x^5 + (1/4)x^5 + (4/2)x^3 + (6/8)x^9 + (2/6)x^7 + c"
            },
            {
                "problem": "1x^3 + 10x^1",
                "solution": "(1/3)x^4 + (10/1)x^2 + c"
            }
        ],
        "subject": "calculus"
    },
    {
        "function_name": "fourth_angle_of_quadrilateral",
        "id": 49,
        "kwargs": [
            "maxAngle=180"
        ],
        "name": "Fourth Angle of Quadrilateral",
        "samples": [
            {
                "problem": "Fourth angle of quadrilateral with angles 73 , 13, 195 =",
                "solution": 79
            },
            {
                "problem": "Fourth angle of quadrilateral with angles 149 , 85, 65 =",
                "solution": 61
            },
            {
                "problem": "Fourth angle of quadrilateral with angles 56 , 170, 90 =",
                "solution": 44
            },
            {
                "problem": "Fourth angle of quadrilateral with angles 163 , 28, 137 =",
                "solution": 32
            },
            {
                "problem": "Fourth angle of quadrilateral with angles 5 , 76, 241 =",
                "solution": 38
            },
            {
                "problem": "Fourth angle of quadrilateral with angles 61 , 167, 98 =",
                "solution": 34
            },
            {
                "problem": "Fourth angle of quadrilateral with angles 174 , 62, 48 =",
                "solution": 76
            },
            {
                "problem": "Fourth angle of quadrilateral with angles 17 , 101, 98 =",
                "solution": 144
            },
            {
                "problem": "Fourth angle of quadrilateral with angles 172 , 8, 16 =",
                "solution": 164
            },
            {
                "problem": "Fourth angle of quadrilateral with angles 13 , 184, 67 =",
                "solution": 96
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "quadratic_equation",
        "id": 50,
        "kwargs": [
            "maxVal=100"
        ],
        "name": "Quadratic Equation",
        "samples": [
            {
                "problem": "Zeros of the Quadratic Equation 25x^2+114x+85=0",
                "solution": "[-0.94, -3.62]"
            },
            {
                "problem": "Zeros of the Quadratic Equation 48x^2+75x+17=0",
                "solution": "[-0.28, -1.29]"
            },
            {
                "problem": "Zeros of the Quadratic Equation 4x^2+56x+75=0",
                "solution": "[-1.5, -12.5]"
            },
            {
                "problem": "Zeros of the Quadratic Equation 41x^2+144x+17=0",
                "solution": "[-0.12, -3.39]"
            },
            {
                "problem": "Zeros of the Quadratic Equation 67x^2+168x+16=0",
                "solution": "[-0.1, -2.41]"
            },
            {
                "problem": "Zeros of the Quadratic Equation 95x^2+196x+93=0",
                "solution": "[-0.74, -1.32]"
            },
            {
                "problem": "Zeros of the Quadratic Equation 41x^2+193x+2=0",
                "solution": "[-0.01, -4.7]"
            },
            {
                "problem": "Zeros of the Quadratic Equation 28x^2+179x+76=0",
                "solution": "[-0.46, -5.94]"
            },
            {
                "problem": "Zeros of the Quadratic Equation 22x^2+51x+26=0",
                "solution": "[-0.76, -1.56]"
            },
            {
                "problem": "Zeros of the Quadratic Equation 25x^2+99x+18=0",
                "solution": "[-0.19, -3.77]"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "hcf",
        "id": 51,
        "kwargs": [
            "maxVal=20"
        ],
        "name": "HCF (Highest Common Factor)",
        "samples": [
            {
                "problem": "HCF of 6 and 15 = ",
                "solution": "3"
            },
            {
                "problem": "HCF of 7 and 11 = ",
                "solution": "1"
            },
            {
                "problem": "HCF of 19 and 4 = ",
                "solution": "1"
            },
            {
                "problem": "HCF of 4 and 10 = ",
                "solution": "2"
            },
            {
                "problem": "HCF of 17 and 13 = ",
                "solution": "1"
            },
            {
                "problem": "HCF of 11 and 13 = ",
                "solution": "1"
            },
            {
                "problem": "HCF of 12 and 14 = ",
                "solution": "2"
            },
            {
                "problem": "HCF of 5 and 12 = ",
                "solution": "1"
            },
            {
                "problem": "HCF of 13 and 9 = ",
                "solution": "1"
            },
            {
                "problem": "HCF of 6 and 18 = ",
                "solution": "6"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "dice_sum_probability",
        "id": 52,
        "kwargs": [
            "maxDice=3"
        ],
        "name": "Probability of a certain sum appearing on faces of dice",
        "samples": [
            {
                "problem": "If 2 dice are rolled at the same time, the probability of getting a sum of 7 =",
                "solution": "6/36"
            },
            {
                "problem": "If 1 dice are rolled at the same time, the probability of getting a sum of 5 =",
                "solution": "1/6"
            },
            {
                "problem": "If 2 dice are rolled at the same time, the probability of getting a sum of 5 =",
                "solution": "4/36"
            },
            {
                "problem": "If 1 dice are rolled at the same time, the probability of getting a sum of 5 =",
                "solution": "1/6"
            },
            {
                "problem": "If 1 dice are rolled at the same time, the probability of getting a sum of 1 =",
                "solution": "1/6"
            },
            {
                "problem": "If 3 dice are rolled at the same time, the probability of getting a sum of 3 =",
                "solution": "1/216"
            },
            {
                "problem": "If 3 dice are rolled at the same time, the probability of getting a sum of 18 =",
                "solution": "1/216"
            },
            {
                "problem": "If 1 dice are rolled at the same time, the probability of getting a sum of 6 =",
                "solution": "1/6"
            },
            {
                "problem": "If 2 dice are rolled at the same time, the probability of getting a sum of 3 =",
                "solution": "2/36"
            },
            {
                "problem": "If 1 dice are rolled at the same time, the probability of getting a sum of 4 =",
                "solution": "1/6"
            }
        ],
        "subject": "statistics"
    },
    {
        "function_name": "exponentiation",
        "id": 53,
        "kwargs": [
            "maxBase=20",
            "maxExpo=10"
        ],
        "name": "Exponentiation",
        "samples": [
            {
                "problem": "4^3 =",
                "solution": "64"
            },
            {
                "problem": "5^3 =",
                "solution": "125"
            },
            {
                "problem": "9^5 =",
                "solution": "59049"
            },
            {
                "problem": "16^7 =",
                "solution": "268435456"
            },
            {
                "problem": "19^1 =",
                "solution": "19"
            },
            {
                "problem": "6^4 =",
                "solution": "1296"
            },
            {
                "problem": "18^10 =",
                "solution": "3570467226624"
            },
            {
                "problem": "8^8 =",
                "solution": "16777216"
            },
            {
                "problem": "15^4 =",
                "solution": "50625"
            },
            {
                "problem": "6^3 =",
                "solution": "216"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "confidence_interval",
        "id": 54,
        "kwargs": [
            ""
        ],
        "name": "Confidence interval For sample S",
        "samples": [
            {
                "problem": "The confidence interval for sample [223, 227, 245, 206, 296, 228, 205, 201, 242, 234, 204, 231, 214, 276, 270, 210, 200, 255, 233, 215, 271, 299, 254, 203, 232, 230, 235, 292, 273, 220, 275, 286, 222, 264, 274, 219, 244, 267, 297] with 90% confidence is",
                "solution": "(250.7912515458906, 234.95233819769913)"
            },
            {
                "problem": "The confidence interval for sample [257, 246, 283, 226, 296, 212, 265, 275, 206, 250, 220, 242, 239, 273, 227, 253, 236, 261, 284, 209, 213] with 90% confidence is",
                "solution": "(255.7557187158305, 236.91094795083617)"
            },
            {
                "problem": "The confidence interval for sample [201, 258, 206, 264, 283, 232, 227, 276, 253, 260, 273, 293, 294, 216, 266, 230, 267, 225, 277, 245, 254, 218, 217, 219, 271, 278, 269, 235, 222, 241, 281, 249, 210, 261, 257, 290, 259, 298, 223] with 99% confidence is",
                "solution": "(262.33660497931584, 240.1249334822226)"
            },
            {
                "problem": "The confidence interval for sample [281, 225, 236, 274, 208, 212, 267, 217, 233, 254, 229, 205, 230, 289, 268, 253, 231, 218, 252, 245, 283, 265, 223, 201, 280, 203] with 80% confidence is",
                "solution": "(248.431297670285, 234.79947156048422)"
            },
            {
                "problem": "The confidence interval for sample [275, 238, 234, 261, 278, 259, 253, 266, 232, 267, 210, 219, 286, 222, 205, 288, 213, 221, 255, 289, 218, 262, 294, 242, 215, 279, 240, 231] with 90% confidence is",
                "solution": "(256.67024998182086, 239.9011785896077)"
            },
            {
                "problem": "The confidence interval for sample [276, 281, 204, 217, 283, 269, 273, 242, 268, 297, 248, 285, 254, 257, 239, 241, 212, 272, 209, 299, 282, 247, 267] with 90% confidence is",
                "solution": "(266.7925057155987, 248.1640160235317)"
            },
            {
                "problem": "The confidence interval for sample [245, 259, 286, 299, 256, 236, 251, 283, 298, 277, 260, 285, 209, 201, 253, 223, 226, 247, 225, 235, 267, 224, 239, 204, 280, 244, 233, 265, 278, 212, 214, 292] with 99% confidence is",
                "solution": "(263.08682437063084, 237.2881756293692)"
            },
            {
                "problem": "The confidence interval for sample [284, 239, 275, 253, 278, 282, 260, 279, 207, 215, 294, 240, 217, 238, 288, 228, 219, 248, 296, 203, 213, 241, 222, 209, 208, 225, 250, 276, 245, 218, 258, 280, 266, 277, 223, 249, 299, 290, 216] with 90% confidence is",
                "solution": "(256.7052516594648, 241.14090218668903)"
            },
            {
                "problem": "The confidence interval for sample [234, 252, 267, 292, 219, 224, 257, 201, 203, 261, 254, 208, 242, 229, 228, 276, 209, 217, 216, 238, 271, 232, 245, 250, 296, 231, 240, 274, 255, 285, 264, 270, 215] with 95% confidence is",
                "solution": "(252.92179671381342, 235.26002146800477)"
            },
            {
                "problem": "The confidence interval for sample [261, 228, 277, 249, 204, 221, 201, 203, 276, 236, 210, 273, 250, 283, 232, 252, 279, 205, 226, 243, 234, 248, 293, 233, 296, 269] with 90% confidence is",
                "solution": "(254.6629081245542, 236.2601687985227)"
            }
        ],
        "subject": "statistics"
    },
    {
        "function_name": "surds_comparison",
        "id": 55,
        "kwargs": [
            "maxValue=100",
            "maxRoot=10"
        ],
        "name": "Comparing surds",
        "samples": [
            {
                "problem": "Fill in the blanks 61^(1/1) _ 79^(1/8)",
                "solution": ">"
            },
            {
                "problem": "Fill in the blanks 80^(1/9) _ 13^(1/6)",
                "solution": ">"
            },
            {
                "problem": "Fill in the blanks 43^(1/1) _ 83^(1/5)",
                "solution": ">"
            },
            {
                "problem": "Fill in the blanks 99^(1/8) _ 23^(1/4)",
                "solution": "<"
            },
            {
                "problem": "Fill in the blanks 66^(1/5) _ 60^(1/9)",
                "solution": ">"
            },
            {
                "problem": "Fill in the blanks 40^(1/1) _ 35^(1/8)",
                "solution": ">"
            },
            {
                "problem": "Fill in the blanks 56^(1/1) _ 41^(1/3)",
                "solution": ">"
            },
            {
                "problem": "Fill in the blanks 70^(1/9) _ 16^(1/8)",
                "solution": ">"
            },
            {
                "problem": "Fill in the blanks 29^(1/5) _ 37^(1/2)",
                "solution": "<"
            },
            {
                "problem": "Fill in the blanks 65^(1/1) _ 6^(1/9)",
                "solution": ">"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "fibonacci_series",
        "id": 56,
        "kwargs": [
            "minNo=1"
        ],
        "name": "Fibonacci Series",
        "samples": [
            {
                "problem": "The Fibonacci Series of the first 2 numbers is ?",
                "solution": [
                    0,
                    1
                ]
            },
            {
                "problem": "The Fibonacci Series of the first 14 numbers is ?",
                "solution": [
                    0,
                    1,
                    1,
                    2,
                    3,
                    5,
                    8,
                    13,
                    21,
                    34,
                    55,
                    89,
                    144,
                    233
                ]
            },
            {
                "problem": "The Fibonacci Series of the first 7 numbers is ?",
                "solution": [
                    0,
                    1,
                    1,
                    2,
                    3,
                    5,
                    8
                ]
            },
            {
                "problem": "The Fibonacci Series of the first 15 numbers is ?",
                "solution": [
                    0,
                    1,
                    1,
                    2,
                    3,
                    5,
                    8,
                    13,
                    21,
                    34,
                    55,
                    89,
                    144,
                    233,
                    377
                ]
            },
            {
                "problem": "The Fibonacci Series of the first 1 numbers is ?",
                "solution": [
                    0
                ]
            },
            {
                "problem": "The Fibonacci Series of the first 2 numbers is ?",
                "solution": [
                    0,
                    1
                ]
            },
            {
                "problem": "The Fibonacci Series of the first 11 numbers is ?",
                "solution": [
                    0,
                    1,
                    1,
                    2,
                    3,
                    5,
                    8,
                    13,
                    21,
                    34,
                    55
                ]
            },
            {
                "problem": "The Fibonacci Series of the first 20 numbers is ?",
                "solution": [
                    0,
                    1,
                    1,
                    2,
                    3,
                    5,
                    8,
                    13,
                    21,
                    34,
                    55,
                    89,
                    144,
                    233,
                    377,
                    610,
                    987,
                    1597,
                    2584,
                    4181
                ]
            },
            {
                "problem": "The Fibonacci Series of the first 10 numbers is ?",
                "solution": [
                    0,
                    1,
                    1,
                    2,
                    3,
                    5,
                    8,
                    13,
                    21,
                    34
                ]
            },
            {
                "problem": "The Fibonacci Series of the first 3 numbers is ?",
                "solution": [
                    0,
                    1,
                    1
                ]
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "basic_trigonometry",
        "id": 57,
        "kwargs": [
            "angles=[0, 30, 45, 60, 90]",
            "functions=['sin', 'cos', 'tan']"
        ],
        "name": "Trigonometric Values",
        "samples": [
            {
                "problem": "What is sin(0)?",
                "solution": "0"
            },
            {
                "problem": "What is tan(60)?",
                "solution": "\u221a3"
            },
            {
                "problem": "What is sin(30)?",
                "solution": "1/2"
            },
            {
                "problem": "What is cos(45)?",
                "solution": "1/\u221a2"
            },
            {
                "problem": "What is sin(60)?",
                "solution": "\u221a3/2"
            },
            {
                "problem": "What is tan(60)?",
                "solution": "\u221a3"
            },
            {
                "problem": "What is sin(90)?",
                "solution": "1"
            },
            {
                "problem": "What is tan(60)?",
                "solution": "\u221a3"
            },
            {
                "problem": "What is sin(0)?",
                "solution": "0"
            },
            {
                "problem": "What is sin(45)?",
                "solution": "1/\u221a2"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "sum_of_polygon_angles",
        "id": 58,
        "kwargs": [
            "maxSides=12"
        ],
        "name": "Sum of Angles of Polygon",
        "samples": [
            {
                "problem": "Sum of angles of polygon with 10 sides = ",
                "solution": 1440
            },
            {
                "problem": "Sum of angles of polygon with 10 sides = ",
                "solution": 1440
            },
            {
                "problem": "Sum of angles of polygon with 10 sides = ",
                "solution": 1440
            },
            {
                "problem": "Sum of angles of polygon with 7 sides = ",
                "solution": 900
            },
            {
                "problem": "Sum of angles of polygon with 3 sides = ",
                "solution": 180
            },
            {
                "problem": "Sum of angles of polygon with 11 sides = ",
                "solution": 1620
            },
            {
                "problem": "Sum of angles of polygon with 12 sides = ",
                "solution": 1800
            },
            {
                "problem": "Sum of angles of polygon with 4 sides = ",
                "solution": 360
            },
            {
                "problem": "Sum of angles of polygon with 5 sides = ",
                "solution": 540
            },
            {
                "problem": "Sum of angles of polygon with 12 sides = ",
                "solution": 1800
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "data_summary",
        "id": 59,
        "kwargs": [
            "number_values=15",
            "minval=5",
            "maxval=50"
        ],
        "name": "Mean,Standard Deviation,Variance",
        "samples": [
            {
                "problem": "Find the mean,standard deviation and variance for the data[12, 14, 7, 23, 9, 9, 49, 24, 8, 50, 10, 28, 11, 48, 8]",
                "solution": "The Mean is 20.666666666666668 , Standard Deviation is 239.15555555555554, Variance is 15.464655041595837"
            },
            {
                "problem": "Find the mean,standard deviation and variance for the data[25, 33, 20, 19, 25, 12, 11, 46, 41, 25, 30, 34, 39, 28, 34]",
                "solution": "The Mean is 28.133333333333333 , Standard Deviation is 95.44888888888887, Variance is 9.769794720918597"
            },
            {
                "problem": "Find the mean,standard deviation and variance for the data[36, 18, 13, 17, 10, 32, 5, 48, 13, 33, 32, 47, 38, 24, 23]",
                "solution": "The Mean is 25.933333333333334 , Standard Deviation is 165.5288888888889, Variance is 12.865803079827115"
            },
            {
                "problem": "Find the mean,standard deviation and variance for the data[27, 31, 12, 49, 36, 47, 5, 14, 43, 42, 37, 16, 24, 28, 37]",
                "solution": "The Mean is 29.866666666666667 , Standard Deviation is 169.84888888888887, Variance is 13.03260867550656"
            },
            {
                "problem": "Find the mean,standard deviation and variance for the data[32, 15, 23, 12, 15, 31, 41, 16, 40, 24, 28, 50, 31, 27, 11]",
                "solution": "The Mean is 26.4 , Standard Deviation is 124.10666666666665, Variance is 11.140317170828965"
            },
            {
                "problem": "Find the mean,standard deviation and variance for the data[30, 20, 17, 14, 26, 21, 32, 11, 43, 18, 19, 10, 8, 9, 7]",
                "solution": "The Mean is 19.0 , Standard Deviation is 97.33333333333333, Variance is 9.865765724632494"
            },
            {
                "problem": "Find the mean,standard deviation and variance for the data[28, 18, 16, 40, 47, 10, 21, 29, 40, 7, 36, 37, 44, 28, 23]",
                "solution": "The Mean is 28.266666666666666 , Standard Deviation is 142.19555555555556, Variance is 11.924577793597372"
            },
            {
                "problem": "Find the mean,standard deviation and variance for the data[12, 39, 47, 17, 44, 42, 22, 23, 36, 11, 20, 24, 23, 42, 28]",
                "solution": "The Mean is 28.666666666666668 , Standard Deviation is 134.62222222222223, Variance is 11.602681682362153"
            },
            {
                "problem": "Find the mean,standard deviation and variance for the data[34, 23, 41, 41, 32, 6, 37, 31, 20, 7, 21, 13, 34, 8, 27]",
                "solution": "The Mean is 25.0 , Standard Deviation is 138.0, Variance is 11.74734012447073"
            },
            {
                "problem": "Find the mean,standard deviation and variance for the data[44, 47, 8, 35, 42, 8, 19, 47, 30, 23, 43, 42, 17, 27, 46]",
                "solution": "The Mean is 31.866666666666667 , Standard Deviation is 185.0488888888889, Variance is 13.603267581316222"
            }
        ],
        "subject": "statistics"
    },
    {
        "function_name": "surface_area_sphere",
        "id": 60,
        "kwargs": [
            "maxSide=20",
            "unit='m'"
        ],
        "name": "Surface Area of Sphere",
        "samples": [
            {
                "problem": "Surface area of Sphere with radius = 5m is",
                "solution": "314.1592653589793 m^2"
            },
            {
                "problem": "Surface area of Sphere with radius = 15m is",
                "solution": "2827.4333882308138 m^2"
            },
            {
                "problem": "Surface area of Sphere with radius = 8m is",
                "solution": "804.247719318987 m^2"
            },
            {
                "problem": "Surface area of Sphere with radius = 10m is",
                "solution": "1256.6370614359173 m^2"
            },
            {
                "problem": "Surface area of Sphere with radius = 18m is",
                "solution": "4071.5040790523717 m^2"
            },
            {
                "problem": "Surface area of Sphere with radius = 8m is",
                "solution": "804.247719318987 m^2"
            },
            {
                "problem": "Surface area of Sphere with radius = 18m is",
                "solution": "4071.5040790523717 m^2"
            },
            {
                "problem": "Surface area of Sphere with radius = 19m is",
                "solution": "4536.459791783661 m^2"
            },
            {
                "problem": "Surface area of Sphere with radius = 13m is",
                "solution": "2123.7166338267 m^2"
            },
            {
                "problem": "Surface area of Sphere with radius = 15m is",
                "solution": "2827.4333882308138 m^2"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "volume_sphere",
        "id": 61,
        "kwargs": [
            "maxRadius=100"
        ],
        "name": "Volume of Sphere",
        "samples": [
            {
                "problem": "Volume of sphere with radius 98 m = ",
                "solution": "3942455.8304233127 m^3"
            },
            {
                "problem": "Volume of sphere with radius 62 m = ",
                "solution": "998305.9919263308 m^3"
            },
            {
                "problem": "Volume of sphere with radius 8 m = ",
                "solution": "2144.660584850632 m^3"
            },
            {
                "problem": "Volume of sphere with radius 95 m = ",
                "solution": "3591364.0018287315 m^3"
            },
            {
                "problem": "Volume of sphere with radius 22 m = ",
                "solution": "44602.23810056549 m^3"
            },
            {
                "problem": "Volume of sphere with radius 41 m = ",
                "solution": "288695.6097040828 m^3"
            },
            {
                "problem": "Volume of sphere with radius 85 m = ",
                "solution": "2572440.784514442 m^3"
            },
            {
                "problem": "Volume of sphere with radius 87 m = ",
                "solution": "2758330.916222452 m^3"
            },
            {
                "problem": "Volume of sphere with radius 10 m = ",
                "solution": "4188.790204786391 m^3"
            },
            {
                "problem": "Volume of sphere with radius 14 m = ",
                "solution": "11494.040321933857 m^3"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "nth_fibonacci_number",
        "id": 62,
        "kwargs": [
            "maxN=100"
        ],
        "name": "nth Fibonacci number",
        "samples": [
            {
                "problem": "What is the 59th Fibonacci number?",
                "solution": "956722026041"
            },
            {
                "problem": "What is the 20th Fibonacci number?",
                "solution": "6765"
            },
            {
                "problem": "What is the 12th Fibonacci number?",
                "solution": "144"
            },
            {
                "problem": "What is the 81th Fibonacci number?",
                "solution": "37889062373144008"
            },
            {
                "problem": "What is the 94th Fibonacci number?",
                "solution": "19740274219868282880"
            },
            {
                "problem": "What is the 50th Fibonacci number?",
                "solution": "12586269025"
            },
            {
                "problem": "What is the 59th Fibonacci number?",
                "solution": "956722026041"
            },
            {
                "problem": "What is the 55th Fibonacci number?",
                "solution": "139583862445"
            },
            {
                "problem": "What is the 50th Fibonacci number?",
                "solution": "12586269025"
            },
            {
                "problem": "What is the 84th Fibonacci number?",
                "solution": "160500643816367552"
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "profit_loss_percent",
        "id": 63,
        "kwargs": [
            "maxCP=1000",
            "maxSP=1000"
        ],
        "name": "Profit or Loss Percent",
        "samples": [
            {
                "problem": "Profit percent when CP = 296 and SP = 306 is: ",
                "solution": 3.3783783783783785
            },
            {
                "problem": "Profit percent when CP = 142 and SP = 236 is: ",
                "solution": 66.19718309859155
            },
            {
                "problem": "Profit percent when CP = 135 and SP = 313 is: ",
                "solution": 131.85185185185185
            },
            {
                "problem": "Loss percent when CP = 784 and SP = 547 is: ",
                "solution": 30.22959183673469
            },
            {
                "problem": "Loss percent when CP = 902 and SP = 799 is: ",
                "solution": 11.419068736141908
            },
            {
                "problem": "Profit percent when CP = 20 and SP = 52 is: ",
                "solution": 160.0
            },
            {
                "problem": "Loss percent when CP = 867 and SP = 450 is: ",
                "solution": 48.09688581314879
            },
            {
                "problem": "Profit percent when CP = 554 and SP = 747 is: ",
                "solution": 34.83754512635379
            },
            {
                "problem": "Loss percent when CP = 945 and SP = 757 is: ",
                "solution": 19.894179894179896
            },
            {
                "problem": "Profit percent when CP = 7 and SP = 349 is: ",
                "solution": 4885.714285714285
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "binary_to_hex",
        "id": 64,
        "kwargs": [
            "max_dig=10"
        ],
        "name": "Binary to Hexidecimal",
        "samples": [
            {
                "problem": "0",
                "solution": "0x0"
            },
            {
                "problem": "100000111",
                "solution": "0x107"
            },
            {
                "problem": "11",
                "solution": "0x3"
            },
            {
                "problem": "0111",
                "solution": "0x7"
            },
            {
                "problem": "1001101001",
                "solution": "0x269"
            },
            {
                "problem": "010001101",
                "solution": "0x8d"
            },
            {
                "problem": "011",
                "solution": "0x3"
            },
            {
                "problem": "10110111",
                "solution": "0xb7"
            },
            {
                "problem": "010000101",
                "solution": "0x85"
            },
            {
                "problem": "100000011",
                "solution": "0x103"
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "multiply_complex_numbers",
        "id": 65,
        "kwargs": [
            "minRealImaginaryNum=-20",
            "maxRealImaginaryNum=20"
        ],
        "name": "Multiplication of 2 complex numbers",
        "samples": [
            {
                "problem": "(-10+7j) * (-17-19j) = ",
                "solution": "(303+71j)"
            },
            {
                "problem": "(14+4j) * (1-2j) = ",
                "solution": "(22-24j)"
            },
            {
                "problem": "(14+13j) * (17-14j) = ",
                "solution": "(420+25j)"
            },
            {
                "problem": "(11-12j) * (17+8j) = ",
                "solution": "(283-116j)"
            },
            {
                "problem": "14j * (-8-12j) = ",
                "solution": "(168-112j)"
            },
            {
                "problem": "(-1-6j) * (-4-3j) = ",
                "solution": "(-14+27j)"
            },
            {
                "problem": "(12-9j) * (7-10j) = ",
                "solution": "(-6-183j)"
            },
            {
                "problem": "(-15+15j) * (20+2j) = ",
                "solution": "(-330+270j)"
            },
            {
                "problem": "(15+13j) * (7+6j) = ",
                "solution": "(27+181j)"
            },
            {
                "problem": "(19+5j) * (4+6j) = ",
                "solution": "(46+134j)"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "geometric_progression",
        "id": 66,
        "kwargs": [
            "number_values=6",
            "min_value=2",
            "max_value=12",
            "n_term=7",
            "sum_term=5"
        ],
        "name": "Geometric Progression",
        "samples": [
            {
                "problem": "For the given GP [7, 49, 343, 2401, 16807, 117649] ,Find the value of a,common ratio,11th term value, sum upto 7th term",
                "solution": "The value of a is 7, common ratio is 7 , 11th term is 1977326743 , sum upto 7th term is 960799.0"
            },
            {
                "problem": "For the given GP [5, 50, 500, 5000, 50000, 500000] ,Find the value of a,common ratio,10th term value, sum upto 8th term",
                "solution": "The value of a is 5, common ratio is 10 , 10th term is 5000000000 , sum upto 8th term is 55555555.0"
            },
            {
                "problem": "For the given GP [10, 60, 360, 2160, 12960, 77760] ,Find the value of a,common ratio,9th term value, sum upto 11th term",
                "solution": "The value of a is 10, common ratio is 6 , 9th term is 16796160 , sum upto 11th term is 725594110.0"
            },
            {
                "problem": "For the given GP [3, 18, 108, 648, 3888, 23328] ,Find the value of a,common ratio,11th term value, sum upto 6th term",
                "solution": "The value of a is 3, common ratio is 6 , 11th term is 181398528 , sum upto 6th term is 27993.0"
            },
            {
                "problem": "For the given GP [12, 36, 108, 324, 972, 2916] ,Find the value of a,common ratio,6th term value, sum upto 9th term",
                "solution": "The value of a is 12, common ratio is 3 , 6th term is 2916 , sum upto 9th term is 118092.0"
            },
            {
                "problem": "For the given GP [4, 40, 400, 4000, 40000, 400000] ,Find the value of a,common ratio,10th term value, sum upto 8th term",
                "solution": "The value of a is 4, common ratio is 10 , 10th term is 4000000000 , sum upto 8th term is 44444444.0"
            },
            {
                "problem": "For the given GP [10, 60, 360, 2160, 12960, 77760] ,Find the value of a,common ratio,6th term value, sum upto 11th term",
                "solution": "The value of a is 10, common ratio is 6 , 6th term is 77760 , sum upto 11th term is 725594110.0"
            },
            {
                "problem": "For the given GP [11, 55, 275, 1375, 6875, 34375] ,Find the value of a,common ratio,9th term value, sum upto 9th term",
                "solution": "The value of a is 11, common ratio is 5 , 9th term is 4296875 , sum upto 9th term is 5371091.0"
            },
            {
                "problem": "For the given GP [11, 121, 1331, 14641, 161051, 1771561] ,Find the value of a,common ratio,7th term value, sum upto 6th term",
                "solution": "The value of a is 11, common ratio is 11 , 7th term is 19487171 , sum upto 6th term is 1948716.0"
            },
            {
                "problem": "For the given GP [8, 24, 72, 216, 648, 1944] ,Find the value of a,common ratio,6th term value, sum upto 7th term",
                "solution": "The value of a is 8, common ratio is 3 , 6th term is 1944 , sum upto 7th term is 8744.0"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "geometric_mean",
        "id": 67,
        "kwargs": [
            "maxValue=100",
            "maxNum=4"
        ],
        "name": "Geometric Mean of N Numbers",
        "samples": [
            {
                "problem": "Geometric mean of 3 numbers 39 , 58 and 44 = ",
                "solution": "(39*58*44)^(1/3) = 46.34274547271732"
            },
            {
                "problem": "Geometric mean of 3 numbers 57 , 50 and 4 = ",
                "solution": "(57*50*4)^(1/3) = 22.506171146771315"
            },
            {
                "problem": "Geometric mean of 3 numbers 9 , 25 and 28 = ",
                "solution": "(9*25*28)^(1/3) = 18.469147504478332"
            },
            {
                "problem": "Geometric mean of 4 numbers 5 , 50 , 33 , 47 = ",
                "solution": "(5*50*33*47)^(1/4) = 24.953872492144974"
            },
            {
                "problem": "Geometric mean of 2 numbers 17 and 46 = ",
                "solution": "(17*46)^(1/2) = 27.964262908219126"
            },
            {
                "problem": "Geometric mean of 4 numbers 81 , 100 , 6 , 48 = ",
                "solution": "(81*100*6*48)^(1/4) = 39.081333745957835"
            },
            {
                "problem": "Geometric mean of 3 numbers 91 , 86 and 90 = ",
                "solution": "(91*86*90)^(1/3) = 88.97352240183"
            },
            {
                "problem": "Geometric mean of 3 numbers 65 , 59 and 59 = ",
                "solution": "(65*59*59)^(1/3) = 60.935791974918"
            },
            {
                "problem": "Geometric mean of 2 numbers 85 and 62 = ",
                "solution": "(85*62)^(1/2) = 72.59476565152615"
            },
            {
                "problem": "Geometric mean of 3 numbers 57 , 21 and 70 = ",
                "solution": "(57*21*70)^(1/3) = 43.75866495040786"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "harmonic_mean",
        "id": 68,
        "kwargs": [
            "maxValue=100",
            "maxNum=4"
        ],
        "name": "Harmonic Mean of N Numbers",
        "samples": [
            {
                "problem": "Harmonic mean of 2 numbers 32 and 64 = ",
                "solution": " 2/((1/32) + (1/64)) = 42.666666666666664"
            },
            {
                "problem": "Harmonic mean of 3 numbers 42 , 31 and 81 = ",
                "solution": " 3/((1/42) + (1/31) + (1/81)) = 43.85114345114345"
            },
            {
                "problem": "Harmonic mean of 2 numbers 48 and 6 = ",
                "solution": " 2/((1/48) + (1/6)) = 10.666666666666666"
            },
            {
                "problem": "Harmonic mean of 4 numbers 93 , 4 , 80 , 13 = ",
                "solution": " 4/((1/93) + (1/4) + (1/80) + (1/13)) = 11.422835040892851"
            },
            {
                "problem": "Harmonic mean of 4 numbers 85 , 25 , 28 , 2 = ",
                "solution": " 4/((1/85) + (1/25) + (1/28) + (1/2)) = 6.808754112430268"
            },
            {
                "problem": "Harmonic mean of 4 numbers 31 , 64 , 97 , 9 = ",
                "solution": " 4/((1/31) + (1/64) + (1/97) + (1/9)) = 23.62621615815086"
            },
            {
                "problem": "Harmonic mean of 3 numbers 31 , 75 and 60 = ",
                "solution": " 3/((1/31) + (1/75) + (1/60)) = 48.18652849740933"
            },
            {
                "problem": "Harmonic mean of 4 numbers 62 , 72 , 22 , 49 = ",
                "solution": " 4/((1/62) + (1/72) + (1/22) + (1/49)) = 41.71854112302664"
            },
            {
                "problem": "Harmonic mean of 4 numbers 15 , 71 , 61 , 54 = ",
                "solution": " 4/((1/15) + (1/71) + (1/61) + (1/54)) = 34.58318854295284"
            },
            {
                "problem": "Harmonic mean of 4 numbers 19 , 34 , 55 , 8 = ",
                "solution": " 4/((1/19) + (1/34) + (1/55) + (1/8)) = 17.760004998594145"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "euclidian_norm",
        "id": 69,
        "kwargs": [
            "maxEltAmt=20"
        ],
        "name": "Euclidian norm or L2 norm of a vector",
        "samples": [
            {
                "problem": "Euclidian norm or L2 norm of the vector[85.06416414459395, 366.11518049588057, 564.0354858155122, 19.985517803811526] is:",
                "solution": 678.0941583527888
            },
            {
                "problem": "Euclidian norm or L2 norm of the vector[244.43098375555329, 444.70188313710236, 823.1064381140793, 280.94677479701954, 800.3703579093169, 105.91750373047404, 941.1823607151185, 180.37826831242597, 264.59854213813094, 502.3761530133334, 363.8622095596028, 907.8541197925456] is:",
                "solution": 1965.4776393091163
            },
            {
                "problem": "Euclidian norm or L2 norm of the vector[977.2254829426947, 249.6882241654662, 806.6443790808063, 183.82782143020293, 213.9475943015491, 817.0739119435051, 856.3411078519205, 54.93254831545602, 480.4339860530773] is:",
                "solution": 1839.1083490475316
            },
            {
                "problem": "Euclidian norm or L2 norm of the vector[302.25225652507913, 669.3498145761899, 357.7121898513218, 499.57179016141, 933.9415802171206, 845.9955237479224, 61.79662835820987, 541.7496672070051, 965.1832891058697] is:",
                "solution": 1932.294282288681
            },
            {
                "problem": "Euclidian norm or L2 norm of the vector[766.1858800257842, 543.330060432399, 429.27463736953575, 863.0792918299801, 732.6040771855223, 706.9842449803324, 374.1233328657568, 912.9061574011972, 319.5327337705635, 796.9564191116914, 931.9379911758097, 700.3214746186051, 239.4735944103894, 488.2885351660526, 110.82986151223717, 362.7497568201039] is:",
                "solution": 2521.3439951666687
            },
            {
                "problem": "Euclidian norm or L2 norm of the vector[730.095510100048, 250.22580886847868, 469.7942677312579, 345.56429220308314, 917.5050287973152, 453.36663147537024, 465.49611535404756, 480.086921221349, 208.99775784475693] is:",
                "solution": 1572.8892751419044
            },
            {
                "problem": "Euclidian norm or L2 norm of the vector[323.51542444613744, 987.5289351376969, 213.04845129798989, 37.694428025290435, 187.0026749577932, 309.9131434529293, 885.5564928843833, 892.3075592010593, 51.52529322441113, 285.99380959933404, 52.33613230222345, 126.48663521642267, 695.9230048878921, 707.1662820992466, 36.41683462410394, 615.0446944467063] is:",
                "solution": 2074.924040826976
            },
            {
                "problem": "Euclidian norm or L2 norm of the vector[984.8094536524919, 85.84033191510399, 516.542502738468, 468.0082569936496, 737.0788351606426, 687.7523758152641, 41.98246897392899, 216.73543904191993, 635.6587283755173, 41.93807828920748, 711.4454156428567, 403.44556187414616, 329.24819996629293, 106.48820564834749] is:",
                "solution": 1929.3986792740172
            },
            {
                "problem": "Euclidian norm or L2 norm of the vector[953.6677699930799, 311.7691879143607, 535.6342128703112, 241.4514924091582, 355.79248519271044, 245.848779474372, 321.48698379696805, 532.3847653014718, 644.8461155661232, 23.68727818582228, 654.7311995161649] is:",
                "solution": 1664.5608888632541
            },
            {
                "problem": "Euclidian norm or L2 norm of the vector[895.9668519847088, 523.9112077462805] is:",
                "solution": 1037.9015143343588
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "angle_btw_vectors",
        "id": 70,
        "kwargs": [
            "maxEltAmt=20"
        ],
        "name": "Angle between 2 vectors",
        "samples": [
            {
                "problem": "angle between the vectors [774.16, 508.48, 670.08, 681.21, 344.09, 551.84, 326.58, 53.53, 631.5, 607.17] and [625.45, 880.58, 568.96, 347.48, 787.63, 580.97, 65.75, 253.36, 402.86, 906.47] is:",
                "solution": "0.46 radians"
            },
            {
                "problem": "angle between the vectors [275.75, 258.76, 240.87, 393.58, 829.74, 487.62, 428.65, 323.78, 776.02, 601.54, 944.17, 895.65, 867.95, 15.62, 83.36, 176.6, 274.61, 548.6, 481.07] and [764.9, 447.78, 876.46, 645.86, 699.62, 959.4, 889.33, 312.48, 629.87, 763.59, 970.58, 119.54, 769.77, 92.26, 395.82, 443.63, 742.42, 536.67, 238.83] is:",
                "solution": "0.56 radians"
            },
            {
                "problem": "angle between the vectors [916.44, 47.84, 896.57, 244.38, 392.49] and [784.62, 580.93, 105.63, 547.63, 33.82] is:",
                "solution": "0.87 radians"
            },
            {
                "problem": "angle between the vectors [490.98, 273.58, 607.45, 991.61, 101.29, 846.1, 391.06, 723.43, 7.08, 306.74, 399.48, 327.82, 665.17, 107.06, 326.83, 139.18, 449.91, 873.14, 661.11] and [201.54, 302.91, 16.6, 781.71, 955.81, 589.91, 839.64, 136.59, 349.72, 371.62, 243.52, 278.83, 267.15, 621.26, 6.3, 961.39, 1.11, 485.03, 209.7] is:",
                "solution": "0.88 radians"
            },
            {
                "problem": "angle between the vectors [364.24, 793.27, 650.8, 973.39, 895.31, 632.74, 823.13, 566.65, 375.77, 932.26, 872.28, 864.64, 782.7] and [824.9, 268.19, 616.2, 730.39, 137.51, 317.38, 770.68, 480.81, 234.73, 447.25, 888.84, 802.86, 500.38] is:",
                "solution": "0.46 radians"
            },
            {
                "problem": "angle between the vectors [889.45, 681.66, 441.73, 119.74, 997.89, 663.97, 678.46, 176.03] and [317.92, 402.66, 159.0, 45.92, 333.07, 906.36, 710.75, 319.13] is:",
                "solution": "0.56 radians"
            },
            {
                "problem": "angle between the vectors [306.27, 0.81, 676.14, 641.7, 663.73, 548.21, 468.53, 202.3, 670.2, 543.81, 135.23, 116.05, 192.76, 402.95, 610.0] and [858.38, 643.21, 609.93, 974.0, 595.6, 757.82, 260.48, 186.37, 631.36, 789.36, 352.69, 473.09, 620.09, 508.39, 395.9] is:",
                "solution": "0.51 radians"
            },
            {
                "problem": "angle between the vectors [58.22, 897.43, 713.2, 922.29] and [916.38, 544.91, 259.77, 217.85] is:",
                "solution": "0.97 radians"
            },
            {
                "problem": "angle between the vectors [705.39, 573.98, 139.52, 474.86, 824.51, 777.87, 469.91, 24.13, 457.17, 167.51, 795.36, 393.88, 493.86, 312.9, 970.47, 403.91, 623.84, 716.42] and [899.79, 817.37, 650.27, 245.09, 971.76, 626.48, 945.38, 204.7, 933.8, 147.33, 595.46, 561.66, 686.48, 796.28, 197.91, 170.51, 139.24, 833.49] is:",
                "solution": "0.56 radians"
            },
            {
                "problem": "angle between the vectors [140.75, 879.09, 497.13, 20.09, 906.14, 583.52] and [497.48, 727.72, 430.49, 713.04, 372.45, 794.95] is:",
                "solution": "0.67 radians"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "absolute_difference",
        "id": 71,
        "kwargs": [
            "maxA=100",
            "maxB=100"
        ],
        "name": "Absolute difference between two numbers",
        "samples": [
            {
                "problem": "|-69-43|=",
                "solution": 112
            },
            {
                "problem": "|96--67|=",
                "solution": 163
            },
            {
                "problem": "|-95-6|=",
                "solution": 101
            },
            {
                "problem": "|9--31|=",
                "solution": 40
            },
            {
                "problem": "|97-17|=",
                "solution": 80
            },
            {
                "problem": "|-29--72|=",
                "solution": 43
            },
            {
                "problem": "|-94-79|=",
                "solution": 173
            },
            {
                "problem": "|-4-64|=",
                "solution": 68
            },
            {
                "problem": "|-79-74|=",
                "solution": 153
            },
            {
                "problem": "|65--56|=",
                "solution": 121
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "vector_dot",
        "id": 72,
        "kwargs": [
            "minVal=-20",
            "maxVal=20"
        ],
        "name": "Dot Product of 2 Vectors",
        "samples": [
            {
                "problem": "[14, 9, -5] . [-6, 3, -19] = ",
                "solution": "38"
            },
            {
                "problem": "[8, 0, -14] . [8, -1, -14] = ",
                "solution": "260"
            },
            {
                "problem": "[10, 5, 18] . [15, -2, -19] = ",
                "solution": "-202"
            },
            {
                "problem": "[-14, -19, 11] . [6, -6, -4] = ",
                "solution": "-14"
            },
            {
                "problem": "[-18, 19, -16] . [5, 5, 3] = ",
                "solution": "-43"
            },
            {
                "problem": "[-18, 11, -11] . [4, 2, -20] = ",
                "solution": "170"
            },
            {
                "problem": "[7, -9, -3] . [14, -2, 3] = ",
                "solution": "107"
            },
            {
                "problem": "[3, 20, 15] . [20, -3, -10] = ",
                "solution": "-150"
            },
            {
                "problem": "[-3, 4, -20] . [20, -15, -18] = ",
                "solution": "240"
            },
            {
                "problem": "[8, -4, -9] . [14, -4, 14] = ",
                "solution": "2"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "binary_2s_complement",
        "id": 73,
        "kwargs": [
            "maxDigits=10"
        ],
        "name": "Binary 2's Complement",
        "samples": [
            {
                "problem": "2's complement of  =",
                "solution": ""
            },
            {
                "problem": "2's complement of 110 =",
                "solution": "10"
            },
            {
                "problem": "2's complement of 10 =",
                "solution": "10"
            },
            {
                "problem": "2's complement of 11111100 =",
                "solution": "100"
            },
            {
                "problem": "2's complement of 1010001 =",
                "solution": "101111"
            },
            {
                "problem": "2's complement of 111001000 =",
                "solution": "111000"
            },
            {
                "problem": "2's complement of 10 =",
                "solution": "10"
            },
            {
                "problem": "2's complement of 100100110 =",
                "solution": "11011010"
            },
            {
                "problem": "2's complement of 111000 =",
                "solution": "1000"
            },
            {
                "problem": "2's complement of  =",
                "solution": ""
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "invert_matrix",
        "id": 74,
        "kwargs": [
            "SquareMatrixDimension=3",
            "MaxMatrixElement=99",
            "OnlyIntegerElementsInInvertedMatrix=False"
        ],
        "name": "Inverse of a Matrix",
        "samples": [
            {
                "problem": "Inverse of Matrix Matrix([[17, 9, 57], [83, 3, 41], [15, 56, 13]]) is:",
                "solution": "Matrix([[-2257/219826, 3075/219826, 99/109913], [-232/109913, -317/109913, 2017/109913], [4603/219826, -817/219826, -348/109913]])"
            },
            {
                "problem": "Inverse of Matrix Matrix([[29, 36, 23], [25, 37, 92], [52, 8, 13]]) is:",
                "solution": "Matrix([[-255/113477, -284/113477, 2461/113477], [49/1247, -9/1247, -23/1247], [-1724/113477, 1640/113477, 173/113477]])"
            },
            {
                "problem": "Inverse of Matrix Matrix([[3, 2, 84], [59, 45, 20], [61, 16, 67]]) is:",
                "solution": "Matrix([[-49/2703, -22/2703, 4/159], [911/49555, 1641/49555, -96/2915], [1801/148665, -74/148665, -1/8745]])"
            },
            {
                "problem": "Inverse of Matrix Matrix([[13, 49, 89], [43, 88, 36], [73, 93, 48]]) is:",
                "solution": "Matrix([[-876/176801, -5925/176801, 6068/176801], [-564/176801, 5873/176801, -3359/176801], [2425/176801, -2368/176801, 963/176801]])"
            },
            {
                "problem": "Inverse of Matrix Matrix([[7, 4, 29], [58, 3, 2], [36, 13, 82]]) is:",
                "solution": "Matrix([[110/769, 49/1538, -79/1538], [-2342/769, -235/769, 834/769], [323/769, 53/1538, -211/1538]])"
            },
            {
                "problem": "Inverse of Matrix Matrix([[5, 86, 12], [15, 93, 11], [13, 81, 17]]) is:",
                "solution": "Matrix([[-69/611, 49/611, 17/611], [56/3055, 71/6110, -25/1222], [-3/3055, -713/6110, 165/1222]])"
            },
            {
                "problem": "Inverse of Matrix Matrix([[59, 9, 96], [10, 99, 5], [19, 27, 31]]) is:",
                "solution": "Matrix([[326/1835, 257/1835, -1051/1835], [-43/3303, 1/3303, 133/3303], [-179/1835, -158/1835, 639/1835]])"
            },
            {
                "problem": "Inverse of Matrix Matrix([[69, 32, 67], [58, 37, 55], [25, 43, 70]]) is:",
                "solution": "Matrix([[75/11576, 641/34728, -719/34728], [-895/11576, 3155/34728, 91/34728], [523/11576, -2167/34728, 697/34728]])"
            },
            {
                "problem": "Inverse of Matrix Matrix([[37, 3, 11], [22, 77, 23], [80, 67, 57]]) is:",
                "solution": "Matrix([[712/13897, 283/27794, -389/27794], [293/27794, 1229/55588, -609/55588], [-2343/27794, -2239/55588, 2783/55588]])"
            },
            {
                "problem": "Inverse of Matrix Matrix([[61, 38, 58], [7, 31, 46], [37, 89, 76]]) is:",
                "solution": "Matrix([[869/45975, -379/15325, 1/1839], [-39/3065, -83/3065, 16/613], [262/45975, 1341/30650, -65/3678]])"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "sector_area",
        "id": 75,
        "kwargs": [
            "maxRadius=49",
            "maxAngle=359"
        ],
        "name": "Area of a Sector",
        "samples": [
            {
                "problem": "Given radius, 18 and angle, 289. Find the area of the sector.",
                "solution": "Area of sector = 817.12825"
            },
            {
                "problem": "Given radius, 18 and angle, 5. Find the area of the sector.",
                "solution": "Area of sector = 14.13717"
            },
            {
                "problem": "Given radius, 29 and angle, 184. Find the area of the sector.",
                "solution": "Area of sector = 1350.39615"
            },
            {
                "problem": "Given radius, 49 and angle, 190. Find the area of the sector.",
                "solution": "Area of sector = 3981.00876"
            },
            {
                "problem": "Given radius, 14 and angle, 3. Find the area of the sector.",
                "solution": "Area of sector = 5.13127"
            },
            {
                "problem": "Given radius, 15 and angle, 309. Find the area of the sector.",
                "solution": "Area of sector = 606.72008"
            },
            {
                "problem": "Given radius, 17 and angle, 14. Find the area of the sector.",
                "solution": "Area of sector = 35.30801"
            },
            {
                "problem": "Given radius, 7 and angle, 84. Find the area of the sector.",
                "solution": "Area of sector = 35.91888"
            },
            {
                "problem": "Given radius, 28 and angle, 264. Find the area of the sector.",
                "solution": "Area of sector = 1806.20634"
            },
            {
                "problem": "Given radius, 33 and angle, 117. Find the area of the sector.",
                "solution": "Area of sector = 1111.88818"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "mean_median",
        "id": 76,
        "kwargs": [
            "maxlen=10"
        ],
        "name": "Mean and Median",
        "samples": [
            {
                "problem": "Given the series of numbers [81, 64, 14, 94, 32, 15, 3, 11, 74, 90]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 47.8 and Arithmetic median of this series is 48.0"
            },
            {
                "problem": "Given the series of numbers [75, 64, 1, 89, 69, 44, 72, 45, 70, 18]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 54.7 and Arithmetic median of this series is 66.5"
            },
            {
                "problem": "Given the series of numbers [68, 96, 78, 73, 90, 26, 98, 15, 20, 81]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 64.5 and Arithmetic median of this series is 75.5"
            },
            {
                "problem": "Given the series of numbers [93, 33, 92, 66, 7, 39, 36, 4, 72, 52]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 49.4 and Arithmetic median of this series is 45.5"
            },
            {
                "problem": "Given the series of numbers [12, 1, 49, 91, 21, 95, 6, 80, 93, 78]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 52.6 and Arithmetic median of this series is 63.5"
            },
            {
                "problem": "Given the series of numbers [19, 66, 46, 12, 64, 2, 73, 11, 68, 48]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 40.9 and Arithmetic median of this series is 47.0"
            },
            {
                "problem": "Given the series of numbers [9, 98, 72, 69, 8, 51, 31, 84, 78, 50]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 55.0 and Arithmetic median of this series is 60.0"
            },
            {
                "problem": "Given the series of numbers [71, 74, 98, 42, 35, 10, 94, 59, 69, 60]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 61.2 and Arithmetic median of this series is 64.5"
            },
            {
                "problem": "Given the series of numbers [92, 39, 57, 59, 51, 2, 61, 62, 34, 74]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 53.1 and Arithmetic median of this series is 58.0"
            },
            {
                "problem": "Given the series of numbers [39, 66, 81, 33, 79, 35, 95, 46, 50, 14]. find the arithmatic mean and mdian of the series",
                "solution": "Arithmetic mean of the series is 53.8 and Arithmetic median of this series is 48.0"
            }
        ],
        "subject": "statistics"
    },
    {
        "function_name": "int_matrix_22_determinant",
        "id": 77,
        "kwargs": [
            "maxMatrixVal=100"
        ],
        "name": "Determinant to 2x2 Matrix",
        "samples": [
            {
                "problem": "Det([[5, 15], [0, 57]]) = ",
                "solution": " 285"
            },
            {
                "problem": "Det([[42, 49], [49, 45]]) = ",
                "solution": " -511"
            },
            {
                "problem": "Det([[3, 97], [95, 92]]) = ",
                "solution": " -8939"
            },
            {
                "problem": "Det([[54, 75], [22, 16]]) = ",
                "solution": " -786"
            },
            {
                "problem": "Det([[98, 73], [26, 4]]) = ",
                "solution": " -1506"
            },
            {
                "problem": "Det([[47, 18], [53, 98]]) = ",
                "solution": " 3652"
            },
            {
                "problem": "Det([[71, 95], [93, 79]]) = ",
                "solution": " -3226"
            },
            {
                "problem": "Det([[17, 3], [6, 12]]) = ",
                "solution": " 186"
            },
            {
                "problem": "Det([[39, 53], [61, 76]]) = ",
                "solution": " -269"
            },
            {
                "problem": "Det([[24, 63], [87, 73]]) = ",
                "solution": " -3729"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "compound_interest",
        "id": 78,
        "kwargs": [
            "maxPrinciple=10000",
            "maxRate=10",
            "maxTime=10"
        ],
        "name": "Compound Interest",
        "samples": [
            {
                "problem": "Compound interest for a principle amount of 5187 dollars, 9% rate of interest and for a time period of 7 year is = ",
                "solution": 9482.04
            },
            {
                "problem": "Compound interest for a principle amount of 5793 dollars, 10% rate of interest and for a time period of 7 year is = ",
                "solution": 11288.92
            },
            {
                "problem": "Compound interest for a principle amount of 2935 dollars, 5% rate of interest and for a time period of 7 year is = ",
                "solution": 4129.84
            },
            {
                "problem": "Compound interest for a principle amount of 8438 dollars, 3% rate of interest and for a time period of 10 year is = ",
                "solution": 11339.97
            },
            {
                "problem": "Compound interest for a principle amount of 5957 dollars, 3% rate of interest and for a time period of 1 year is = ",
                "solution": 6135.71
            },
            {
                "problem": "Compound interest for a principle amount of 9860 dollars, 6% rate of interest and for a time period of 9 year is = ",
                "solution": 16658.26
            },
            {
                "problem": "Compound interest for a principle amount of 7160 dollars, 8% rate of interest and for a time period of 10 year is = ",
                "solution": 15457.9
            },
            {
                "problem": "Compound interest for a principle amount of 1862 dollars, 7% rate of interest and for a time period of 5 year is = ",
                "solution": 2611.55
            },
            {
                "problem": "Compound interest for a principle amount of 9849 dollars, 8% rate of interest and for a time period of 6 year is = ",
                "solution": 15629.13
            },
            {
                "problem": "Compound interest for a principle amount of 6818 dollars, 6% rate of interest and for a time period of 1 year is = ",
                "solution": 7227.08
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "decimal_to_hexadeci",
        "id": 79,
        "kwargs": [
            "max_dec=1000"
        ],
        "name": "Decimal to Hexadecimal",
        "samples": [
            {
                "problem": "Binary of 21=",
                "solution": "0x15"
            },
            {
                "problem": "Binary of 679=",
                "solution": "0x2a7"
            },
            {
                "problem": "Binary of 886=",
                "solution": "0x376"
            },
            {
                "problem": "Binary of 835=",
                "solution": "0x343"
            },
            {
                "problem": "Binary of 168=",
                "solution": "0xa8"
            },
            {
                "problem": "Binary of 78=",
                "solution": "0x4e"
            },
            {
                "problem": "Binary of 485=",
                "solution": "0x1e5"
            },
            {
                "problem": "Binary of 224=",
                "solution": "0xe0"
            },
            {
                "problem": "Binary of 231=",
                "solution": "0xe7"
            },
            {
                "problem": "Binary of 904=",
                "solution": "0x388"
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "percentage",
        "id": 80,
        "kwargs": [
            "maxValue=99",
            "maxpercentage=99"
        ],
        "name": "Percentage of a number",
        "samples": [
            {
                "problem": "What is 70% of 49?",
                "solution": "34.30"
            },
            {
                "problem": "What is 63% of 90?",
                "solution": "56.70"
            },
            {
                "problem": "What is 69% of 81?",
                "solution": "55.89"
            },
            {
                "problem": "What is 43% of 33?",
                "solution": "14.19"
            },
            {
                "problem": "What is 33% of 89?",
                "solution": "29.37"
            },
            {
                "problem": "What is 33% of 93?",
                "solution": "30.69"
            },
            {
                "problem": "What is 24% of 8?",
                "solution": "1.92"
            },
            {
                "problem": "What is 59% of 49?",
                "solution": "28.91"
            },
            {
                "problem": "What is 2% of 36?",
                "solution": "0.72"
            },
            {
                "problem": "What is 80% of 13?",
                "solution": "10.40"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "celsius_to_fahrenheit",
        "id": 81,
        "kwargs": [
            "maxTemp=100"
        ],
        "name": "Celsius To Fahrenheit",
        "samples": [
            {
                "problem": "Convert 47 degrees Celsius to degrees Fahrenheit =",
                "solution": "116.60000000000001"
            },
            {
                "problem": "Convert 72 degrees Celsius to degrees Fahrenheit =",
                "solution": "161.6"
            },
            {
                "problem": "Convert 46 degrees Celsius to degrees Fahrenheit =",
                "solution": "114.8"
            },
            {
                "problem": "Convert 47 degrees Celsius to degrees Fahrenheit =",
                "solution": "116.60000000000001"
            },
            {
                "problem": "Convert 11 degrees Celsius to degrees Fahrenheit =",
                "solution": "51.8"
            },
            {
                "problem": "Convert 23 degrees Celsius to degrees Fahrenheit =",
                "solution": "73.4"
            },
            {
                "problem": "Convert 51 degrees Celsius to degrees Fahrenheit =",
                "solution": "123.8"
            },
            {
                "problem": "Convert 98 degrees Celsius to degrees Fahrenheit =",
                "solution": "208.4"
            },
            {
                "problem": "Convert 41 degrees Celsius to degrees Fahrenheit =",
                "solution": "105.8"
            },
            {
                "problem": "Convert -50 degrees Celsius to degrees Fahrenheit =",
                "solution": "-58.0"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "arithmetic_progression_term",
        "id": 82,
        "kwargs": [
            "maxd=100",
            "maxa=100",
            "maxn=100"
        ],
        "name": "AP Term Calculation",
        "samples": [
            {
                "problem": "Find the term number 47 of the AP series: -91, -85, -79 ... ",
                "solution": 185
            },
            {
                "problem": "Find the term number 77 of the AP series: 20, 24, 28 ... ",
                "solution": 324
            },
            {
                "problem": "Find the term number 64 of the AP series: 68, 71, 74 ... ",
                "solution": 257
            },
            {
                "problem": "Find the term number 40 of the AP series: -23, -83, -143 ... ",
                "solution": -2363
            },
            {
                "problem": "Find the term number 27 of the AP series: 57, 83, 109 ... ",
                "solution": 733
            },
            {
                "problem": "Find the term number 94 of the AP series: 39, 119, 199 ... ",
                "solution": 7479
            },
            {
                "problem": "Find the term number 8 of the AP series: 57, -42, -141 ... ",
                "solution": -636
            },
            {
                "problem": "Find the term number 60 of the AP series: -56, -12, 32 ... ",
                "solution": 2540
            },
            {
                "problem": "Find the term number 35 of the AP series: 94, 61, 28 ... ",
                "solution": -1028
            },
            {
                "problem": "Find the term number 7 of the AP series: 64, -33, -130 ... ",
                "solution": -518
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "arithmetic_progression_sum",
        "id": 83,
        "kwargs": [
            "maxd=100",
            "maxa=100",
            "maxn=100"
        ],
        "name": "AP Sum Calculation",
        "samples": [
            {
                "problem": "Find the sum of first 37 terms of the AP series: -81, -114, -147 ... ",
                "solution": -24975.0
            },
            {
                "problem": "Find the sum of first 59 terms of the AP series: 8, 16, 24 ... ",
                "solution": 14160.0
            },
            {
                "problem": "Find the sum of first 64 terms of the AP series: 34, 26, 18 ... ",
                "solution": -13952.0
            },
            {
                "problem": "Find the sum of first 36 terms of the AP series: -21, 17, 55 ... ",
                "solution": 23184.0
            },
            {
                "problem": "Find the sum of first 28 terms of the AP series: -76, -49, -22 ... ",
                "solution": 8078.0
            },
            {
                "problem": "Find the sum of first 33 terms of the AP series: 37, -28, -93 ... ",
                "solution": -33099.0
            },
            {
                "problem": "Find the sum of first 63 terms of the AP series: -82, -129, -176 ... ",
                "solution": -96957.0
            },
            {
                "problem": "Find the sum of first 44 terms of the AP series: 65, 40, 15 ... ",
                "solution": -20790.0
            },
            {
                "problem": "Find the sum of first 25 terms of the AP series: -90, -134, -178 ... ",
                "solution": -15450.0
            },
            {
                "problem": "Find the sum of first 11 terms of the AP series: 72, 39, 6 ... ",
                "solution": -1023.0
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "decimal_to_octal",
        "id": 84,
        "kwargs": [
            "maxDecimal=4096"
        ],
        "name": "Converts decimal to octal",
        "samples": [
            {
                "problem": "The decimal number 2900 in Octal is: ",
                "solution": "0o5524"
            },
            {
                "problem": "The decimal number 1307 in Octal is: ",
                "solution": "0o2433"
            },
            {
                "problem": "The decimal number 1305 in Octal is: ",
                "solution": "0o2431"
            },
            {
                "problem": "The decimal number 1233 in Octal is: ",
                "solution": "0o2321"
            },
            {
                "problem": "The decimal number 1038 in Octal is: ",
                "solution": "0o2016"
            },
            {
                "problem": "The decimal number 1737 in Octal is: ",
                "solution": "0o3311"
            },
            {
                "problem": "The decimal number 2112 in Octal is: ",
                "solution": "0o4100"
            },
            {
                "problem": "The decimal number 7 in Octal is: ",
                "solution": "0o7"
            },
            {
                "problem": "The decimal number 2305 in Octal is: ",
                "solution": "0o4401"
            },
            {
                "problem": "The decimal number 3986 in Octal is: ",
                "solution": "0o7622"
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "decimal_to_roman_numerals",
        "id": 85,
        "kwargs": [
            "maxDecimal=4000"
        ],
        "name": "Converts decimal to Roman Numerals",
        "samples": [
            {
                "problem": "The number 3878 in Roman Numerals is: ",
                "solution": "MMMDCCCLXXVIII"
            },
            {
                "problem": "The number 188 in Roman Numerals is: ",
                "solution": "CLXXXVIII"
            },
            {
                "problem": "The number 1542 in Roman Numerals is: ",
                "solution": "MDXLII"
            },
            {
                "problem": "The number 988 in Roman Numerals is: ",
                "solution": "CMLXXXVIII"
            },
            {
                "problem": "The number 2645 in Roman Numerals is: ",
                "solution": "MMDCXLV"
            },
            {
                "problem": "The number 3103 in Roman Numerals is: ",
                "solution": "MMMCIII"
            },
            {
                "problem": "The number 2601 in Roman Numerals is: ",
                "solution": "MMDCI"
            },
            {
                "problem": "The number 608 in Roman Numerals is: ",
                "solution": "DCVIII"
            },
            {
                "problem": "The number 3590 in Roman Numerals is: ",
                "solution": "MMMDXC"
            },
            {
                "problem": "The number 1222 in Roman Numerals is: ",
                "solution": "MCCXXII"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "degree_to_rad",
        "id": 86,
        "kwargs": [
            "max_deg=360"
        ],
        "name": "Degrees to Radians",
        "samples": [
            {
                "problem": "Angle 174 in radians is = ",
                "solution": "3.04"
            },
            {
                "problem": "Angle 83 in radians is = ",
                "solution": "1.45"
            },
            {
                "problem": "Angle 57 in radians is = ",
                "solution": "0.99"
            },
            {
                "problem": "Angle 172 in radians is = ",
                "solution": "3.0"
            },
            {
                "problem": "Angle 74 in radians is = ",
                "solution": "1.29"
            },
            {
                "problem": "Angle 41 in radians is = ",
                "solution": "0.72"
            },
            {
                "problem": "Angle 147 in radians is = ",
                "solution": "2.57"
            },
            {
                "problem": "Angle 295 in radians is = ",
                "solution": "5.15"
            },
            {
                "problem": "Angle 217 in radians is = ",
                "solution": "3.79"
            },
            {
                "problem": "Angle 325 in radians is = ",
                "solution": "5.67"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "radian_to_deg",
        "id": 87,
        "kwargs": [
            "max_rad=3"
        ],
        "name": "Radians to Degrees",
        "samples": [
            {
                "problem": "Angle 1 in degrees is = ",
                "solution": "57.3"
            },
            {
                "problem": "Angle 3 in degrees is = ",
                "solution": "171.89"
            },
            {
                "problem": "Angle 0 in degrees is = ",
                "solution": "0.0"
            },
            {
                "problem": "Angle 1 in degrees is = ",
                "solution": "57.3"
            },
            {
                "problem": "Angle 0 in degrees is = ",
                "solution": "0.0"
            },
            {
                "problem": "Angle 2 in degrees is = ",
                "solution": "114.59"
            },
            {
                "problem": "Angle 2 in degrees is = ",
                "solution": "114.59"
            },
            {
                "problem": "Angle 0 in degrees is = ",
                "solution": "0.0"
            },
            {
                "problem": "Angle 1 in degrees is = ",
                "solution": "57.3"
            },
            {
                "problem": "Angle 3 in degrees is = ",
                "solution": "171.89"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "differentiation",
        "id": 88,
        "kwargs": [
            "diff_lvl=2"
        ],
        "name": "Differentiation",
        "samples": [
            {
                "problem": "differentiate w.r.t x : d(cos(x)+3*x^4)/dx",
                "solution": "12*x^3 - sin(x)"
            },
            {
                "problem": "differentiate w.r.t x : d(tan(x)+6*x^(-2))/dx",
                "solution": "tan(x)^2 + 1 - 12/x^3"
            },
            {
                "problem": "differentiate w.r.t x : d(ln(x)+5*x^3)/dx",
                "solution": "15*x^2 + 1/x"
            },
            {
                "problem": "differentiate w.r.t x : d(exp(x)+7*x^2)/dx",
                "solution": "14*x + exp(x)"
            },
            {
                "problem": "differentiate w.r.t x : d(sin(x)+7*x^(-2))/dx",
                "solution": "cos(x) - 14/x^3"
            },
            {
                "problem": "differentiate w.r.t x : d(ln(x)+5*x^(-4))/dx",
                "solution": "1/x - 20/x^5"
            },
            {
                "problem": "differentiate w.r.t x : d(exp(x)+9*x^4)/dx",
                "solution": "36*x^3 + exp(x)"
            },
            {
                "problem": "differentiate w.r.t x : d(cot(x)+8*x^(-3))/dx",
                "solution": "-cot(x)^2 - 1 - 24/x^4"
            },
            {
                "problem": "differentiate w.r.t x : d(sin(x)+5*x^(-3))/dx",
                "solution": "cos(x) - 15/x^4"
            },
            {
                "problem": "differentiate w.r.t x : d(tan(x)+4*x^3)/dx",
                "solution": "12*x^2 + tan(x)^2 + 1"
            }
        ],
        "subject": "calculus"
    },
    {
        "function_name": "definite_integral",
        "id": 89,
        "kwargs": [
            "max_coeff=100"
        ],
        "name": "Definite Integral of Quadratic Equation",
        "samples": [
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 12x^2 + 50x + 4 is = ",
                "solution": "33.0"
            },
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 89x^2 + 14x + 61 is = ",
                "solution": "97.6667"
            },
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 88x^2 + 96x + 0 is = ",
                "solution": "77.3333"
            },
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 99x^2 + 81x + 20 is = ",
                "solution": "93.5"
            },
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 75x^2 + 27x + 47 is = ",
                "solution": "85.5"
            },
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 50x^2 + 75x + 71 is = ",
                "solution": "125.1667"
            },
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 3x^2 + 75x + 55 is = ",
                "solution": "93.5"
            },
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 24x^2 + 65x + 90 is = ",
                "solution": "130.5"
            },
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 30x^2 + 52x + 94 is = ",
                "solution": "130.0"
            },
            {
                "problem": "The definite integral within limits 0 to 1 of the equation 55x^2 + 34x + 86 is = ",
                "solution": "121.3333"
            }
        ],
        "subject": "calculus"
    },
    {
        "function_name": "is_prime",
        "id": 90,
        "kwargs": [
            "max_num=100"
        ],
        "name": "isprime",
        "samples": [
            {
                "problem": "Is 7 prime?",
                "solution": "Yes"
            },
            {
                "problem": "Is 37 prime?",
                "solution": "Yes"
            },
            {
                "problem": "Is 31 prime?",
                "solution": "Yes"
            },
            {
                "problem": "Is 46 prime?",
                "solution": "No"
            },
            {
                "problem": "Is 40 prime?",
                "solution": "No"
            },
            {
                "problem": "Is 32 prime?",
                "solution": "No"
            },
            {
                "problem": "Is 33 prime?",
                "solution": "No"
            },
            {
                "problem": "Is 52 prime?",
                "solution": "No"
            },
            {
                "problem": "Is 95 prime?",
                "solution": "No"
            },
            {
                "problem": "Is 29 prime?",
                "solution": "Yes"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "bcd_to_decimal",
        "id": 91,
        "kwargs": [
            "maxNumber=10000"
        ],
        "name": "Binary Coded Decimal to Integer",
        "samples": [
            {
                "problem": "Integer of Binary Coded Decimal 6 is = ",
                "solution": 26902
            },
            {
                "problem": "Integer of Binary Coded Decimal 2 is = ",
                "solution": 8599
            },
            {
                "problem": "Integer of Binary Coded Decimal 7 is = ",
                "solution": 30775
            },
            {
                "problem": "Integer of Binary Coded Decimal 3 is = ",
                "solution": 13364
            },
            {
                "problem": "Integer of Binary Coded Decimal 4 is = ",
                "solution": 18049
            },
            {
                "problem": "Integer of Binary Coded Decimal 6 is = ",
                "solution": 26132
            },
            {
                "problem": "Integer of Binary Coded Decimal 1 is = ",
                "solution": 6032
            },
            {
                "problem": "Integer of Binary Coded Decimal 7 is = ",
                "solution": 28755
            },
            {
                "problem": "Integer of Binary Coded Decimal 6 is = ",
                "solution": 27033
            },
            {
                "problem": "Integer of Binary Coded Decimal 5 is = ",
                "solution": 21785
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "complex_to_polar",
        "id": 92,
        "kwargs": [
            "minRealImaginaryNum=-20, maxRealImaginaryNum=20"
        ],
        "name": "Complex To Polar Form",
        "samples": [
            {
                "problem": "rexp(itheta) = ",
                "solution": "12.53exp(i1.07)"
            },
            {
                "problem": "rexp(itheta) = ",
                "solution": "6.71exp(i0.46)"
            },
            {
                "problem": "rexp(itheta) = ",
                "solution": "8.06exp(i-1.45)"
            },
            {
                "problem": "rexp(itheta) = ",
                "solution": "5.83exp(i1.03)"
            },
            {
                "problem": "rexp(itheta) = ",
                "solution": "17.49exp(i0.54)"
            },
            {
                "problem": "rexp(itheta) = ",
                "solution": "2.0exp(i3.14)"
            },
            {
                "problem": "rexp(itheta) = ",
                "solution": "6.0exp(i1.57)"
            },
            {
                "problem": "rexp(itheta) = ",
                "solution": "11.4exp(i-0.27)"
            },
            {
                "problem": "rexp(itheta) = ",
                "solution": "5.0exp(i1.57)"
            },
            {
                "problem": "rexp(itheta) = ",
                "solution": "17.46exp(i-2.91)"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "set_operation",
        "id": 93,
        "kwargs": [
            "minval=3",
            "maxval=7",
            "n_a=4",
            "n_b=5"
        ],
        "name": "Union,Intersection,Difference of Two Sets",
        "samples": [
            {
                "problem": "Given the two sets a={3, 4, 5, 6, 7, 9} ,b={8, 10, 2}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {2, 3, 4, 5, 6, 7, 8, 9, 10},Intersection is set(), a-b is {3, 4, 5, 6, 7, 9},b-a is {8, 10, 2}, Symmetric difference is {2, 3, 4, 5, 6, 7, 8, 9, 10}"
            },
            {
                "problem": "Given the two sets a={4, 5, 6, 8, 10} ,b={10, 2, 5}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {2, 4, 5, 6, 8, 10},Intersection is {10, 5}, a-b is {8, 4, 6},b-a is {2}, Symmetric difference is {2, 4, 6, 8}"
            },
            {
                "problem": "Given the two sets a={2, 3, 5, 6, 8} ,b={1, 10, 7}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {1, 2, 3, 5, 6, 7, 8, 10},Intersection is set(), a-b is {2, 3, 5, 6, 8},b-a is {1, 10, 7}, Symmetric difference is {1, 2, 3, 5, 6, 7, 8, 10}"
            },
            {
                "problem": "Given the two sets a={1, 3, 6, 7, 10} ,b={8, 10, 4}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {1, 3, 4, 6, 7, 8, 10},Intersection is {10}, a-b is {1, 3, 6, 7},b-a is {8, 4}, Symmetric difference is {1, 3, 4, 6, 7, 8}"
            },
            {
                "problem": "Given the two sets a={1, 2, 3, 4, 5} ,b={8, 7}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {1, 2, 3, 4, 5, 7, 8},Intersection is set(), a-b is {1, 2, 3, 4, 5},b-a is {8, 7}, Symmetric difference is {1, 2, 3, 4, 5, 7, 8}"
            },
            {
                "problem": "Given the two sets a={1, 2, 3, 5, 8, 9} ,b={8, 1, 5}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {1, 2, 3, 5, 8, 9},Intersection is {8, 1, 5}, a-b is {9, 2, 3},b-a is set(), Symmetric difference is {2, 3, 9}"
            },
            {
                "problem": "Given the two sets a={8, 9, 3} ,b={1, 2, 4, 5, 6, 9}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {1, 2, 3, 4, 5, 6, 8, 9},Intersection is {9}, a-b is {8, 3},b-a is {1, 2, 4, 5, 6}, Symmetric difference is {1, 2, 3, 4, 5, 6, 8}"
            },
            {
                "problem": "Given the two sets a={1, 3, 4, 6, 7, 8} ,b={2, 3, 5, 6, 7, 8, 10}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {1, 2, 3, 4, 5, 6, 7, 8, 10},Intersection is {8, 3, 6, 7}, a-b is {1, 4},b-a is {2, 10, 5}, Symmetric difference is {1, 2, 4, 5, 10}"
            },
            {
                "problem": "Given the two sets a={1, 10, 4} ,b={9, 3, 4}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {1, 3, 4, 9, 10},Intersection is {4}, a-b is {1, 10},b-a is {9, 3}, Symmetric difference is {1, 3, 9, 10}"
            },
            {
                "problem": "Given the two sets a={8, 5, 7} ,b={1, 2, 3, 5, 6, 9, 10}.Find the Union,intersection,a-b,b-a and symmetric difference",
                "solution": "Union is {1, 2, 3, 5, 6, 7, 8, 9, 10},Intersection is {5}, a-b is {8, 7},b-a is {1, 2, 3, 6, 9, 10}, Symmetric difference is {1, 2, 3, 6, 7, 8, 9, 10}"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "base_conversion",
        "id": 94,
        "kwargs": [
            "maxNum=60000",
            "maxBase=16"
        ],
        "name": "Base Conversion",
        "samples": [
            {
                "problem": "Convert 4273 from base 14 to base 4.",
                "solution": "2303031"
            },
            {
                "problem": "Convert 151432 from base 6 to base 12.",
                "solution": "8578"
            },
            {
                "problem": "Convert 13203 from base 4 to base 16.",
                "solution": "1E3"
            },
            {
                "problem": "Convert 92C4 from base 16 to base 11.",
                "solution": "26257"
            },
            {
                "problem": "Convert E05C from base 16 to base 2.",
                "solution": "1110000001011100"
            },
            {
                "problem": "Convert 32798 from base 10 to base 2.",
                "solution": "1000000000011110"
            },
            {
                "problem": "Convert 4EB6 from base 16 to base 2.",
                "solution": "100111010110110"
            },
            {
                "problem": "Convert 5765 from base 13 to base 16.",
                "solution": "2FDB"
            },
            {
                "problem": "Convert 18112 from base 9 to base 14.",
                "solution": "479B"
            },
            {
                "problem": "Convert AAED from base 16 to base 13.",
                "solution": "16BBC"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "curved_surface_area_cylinder",
        "id": 95,
        "kwargs": [
            "maxRadius=49",
            "maxHeight=99"
        ],
        "name": "Curved surface area of a cylinder",
        "samples": [
            {
                "problem": "What is the curved surface area of a cylinder of radius, 32 and height, 56?",
                "solution": "CSA of cylinder = 11259.47"
            },
            {
                "problem": "What is the curved surface area of a cylinder of radius, 36 and height, 68?",
                "solution": "CSA of cylinder = 15381.24"
            },
            {
                "problem": "What is the curved surface area of a cylinder of radius, 40 and height, 22?",
                "solution": "CSA of cylinder = 5529.2"
            },
            {
                "problem": "What is the curved surface area of a cylinder of radius, 38 and height, 50?",
                "solution": "CSA of cylinder = 11938.05"
            },
            {
                "problem": "What is the curved surface area of a cylinder of radius, 7 and height, 92?",
                "solution": "CSA of cylinder = 4046.37"
            },
            {
                "problem": "What is the curved surface area of a cylinder of radius, 43 and height, 48?",
                "solution": "CSA of cylinder = 12968.49"
            },
            {
                "problem": "What is the curved surface area of a cylinder of radius, 3 and height, 54?",
                "solution": "CSA of cylinder = 1017.88"
            },
            {
                "problem": "What is the curved surface area of a cylinder of radius, 10 and height, 98?",
                "solution": "CSA of cylinder = 6157.52"
            },
            {
                "problem": "What is the curved surface area of a cylinder of radius, 46 and height, 31?",
                "solution": "CSA of cylinder = 8959.82"
            },
            {
                "problem": "What is the curved surface area of a cylinder of radius, 5 and height, 46?",
                "solution": "CSA of cylinder = 1445.13"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "perimeter_of_polygons",
        "id": 96,
        "kwargs": [
            "maxSides=12",
            "maxLength=120"
        ],
        "name": "Perimeter of Polygons",
        "samples": [
            {
                "problem": "The perimeter of a 9 sided polygon with lengths of [7, 83, 90, 33, 29, 81, 20, 90, 39]cm is: ",
                "solution": 472
            },
            {
                "problem": "The perimeter of a 9 sided polygon with lengths of [100, 90, 109, 5, 35, 112, 31, 73, 92]cm is: ",
                "solution": 647
            },
            {
                "problem": "The perimeter of a 9 sided polygon with lengths of [56, 6, 104, 72, 2, 79, 62, 82, 79]cm is: ",
                "solution": 542
            },
            {
                "problem": "The perimeter of a 9 sided polygon with lengths of [49, 54, 14, 22, 84, 20, 12, 108, 97]cm is: ",
                "solution": 460
            },
            {
                "problem": "The perimeter of a 6 sided polygon with lengths of [46, 64, 1, 35, 22, 40]cm is: ",
                "solution": 208
            },
            {
                "problem": "The perimeter of a 7 sided polygon with lengths of [110, 64, 40, 41, 101, 41, 41]cm is: ",
                "solution": 438
            },
            {
                "problem": "The perimeter of a 5 sided polygon with lengths of [30, 94, 41, 16, 71]cm is: ",
                "solution": 252
            },
            {
                "problem": "The perimeter of a 11 sided polygon with lengths of [49, 72, 78, 6, 59, 104, 14, 5, 46, 102, 46]cm is: ",
                "solution": 581
            },
            {
                "problem": "The perimeter of a 5 sided polygon with lengths of [87, 36, 107, 68, 74]cm is: ",
                "solution": 372
            },
            {
                "problem": "The perimeter of a 3 sided polygon with lengths of [2, 65, 114]cm is: ",
                "solution": 181
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "power_of_powers",
        "id": 97,
        "kwargs": [
            "maxBase=50",
            "maxPower=10"
        ],
        "name": "Power of Powers",
        "samples": [
            {
                "problem": "Simplify 4^3^10=",
                "solution": "4^30"
            },
            {
                "problem": "Simplify 45^9^6=",
                "solution": "45^54"
            },
            {
                "problem": "Simplify 29^2^3=",
                "solution": "29^6"
            },
            {
                "problem": "Simplify 1^6^2=",
                "solution": "1^12"
            },
            {
                "problem": "Simplify 48^5^5=",
                "solution": "48^25"
            },
            {
                "problem": "Simplify 37^4^1=",
                "solution": "37^4"
            },
            {
                "problem": "Simplify 14^7^6=",
                "solution": "14^42"
            },
            {
                "problem": "Simplify 11^3^10=",
                "solution": "11^30"
            },
            {
                "problem": "Simplify 50^4^9=",
                "solution": "50^36"
            },
            {
                "problem": "Simplify 15^5^9=",
                "solution": "15^45"
            }
        ],
        "subject": "basic_math"
    },
    {
        "function_name": "quotient_of_power_same_base",
        "id": 98,
        "kwargs": [
            "maxBase=50",
            "maxPower=10"
        ],
        "name": "Quotient of Powers with Same Base",
        "samples": [
            {
                "problem": "The Quotient of 5^7 and 5^2 = 5^(7-2) = 5^5",
                "solution": "3125"
            },
            {
                "problem": "The Quotient of 50^10 and 50^10 = 50^(10-10) = 50^0",
                "solution": "1"
            },
            {
                "problem": "The Quotient of 1^7 and 1^5 = 1^(7-5) = 1^2",
                "solution": "1"
            },
            {
                "problem": "The Quotient of 37^10 and 37^5 = 37^(10-5) = 37^5",
                "solution": "69343957"
            },
            {
                "problem": "The Quotient of 5^7 and 5^5 = 5^(7-5) = 5^2",
                "solution": "25"
            },
            {
                "problem": "The Quotient of 44^5 and 44^9 = 44^(5-9) = 44^-4",
                "solution": "2.668021310019807e-07"
            },
            {
                "problem": "The Quotient of 47^1 and 47^6 = 47^(1-6) = 47^-5",
                "solution": "4.360243168494181e-09"
            },
            {
                "problem": "The Quotient of 15^8 and 15^5 = 15^(8-5) = 15^3",
                "solution": "3375"
            },
            {
                "problem": "The Quotient of 39^2 and 39^6 = 39^(2-6) = 39^-4",
                "solution": "4.322565390688589e-07"
            },
            {
                "problem": "The Quotient of 30^4 and 30^4 = 30^(4-4) = 30^0",
                "solution": "1"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "quotient_of_power_same_power",
        "id": 99,
        "kwargs": [
            "maxBase=50",
            "maxPower=10"
        ],
        "name": "Quotient of Powers with Same Power",
        "samples": [
            {
                "problem": "The Quotient of 19^10 and 2^10 = (19/2)^10 = 9.5^10",
                "solution": "5987369392.383789"
            },
            {
                "problem": "The Quotient of 10^10 and 42^10 = (10/42)^10 = 0.23809523809523808^10",
                "solution": "5.854733024032202e-07"
            },
            {
                "problem": "The Quotient of 35^3 and 31^3 = (35/31)^3 = 1.1290322580645162^3",
                "solution": "1.4391930448793264"
            },
            {
                "problem": "The Quotient of 18^5 and 20^5 = (18/20)^5 = 0.9^5",
                "solution": "0.5904900000000001"
            },
            {
                "problem": "The Quotient of 11^1 and 5^1 = (11/5)^1 = 2.2^1",
                "solution": "2.2"
            },
            {
                "problem": "The Quotient of 46^8 and 11^8 = (46/11)^8 = 4.181818181818182^8",
                "solution": "93523.59061781067"
            },
            {
                "problem": "The Quotient of 36^9 and 6^9 = (36/6)^9 = 6.0^9",
                "solution": "10077696.0"
            },
            {
                "problem": "The Quotient of 44^5 and 40^5 = (44/40)^5 = 1.1^5",
                "solution": "1.6105100000000006"
            },
            {
                "problem": "The Quotient of 7^1 and 18^1 = (7/18)^1 = 0.3888888888888889^1",
                "solution": "0.3888888888888889"
            },
            {
                "problem": "The Quotient of 4^3 and 14^3 = (4/14)^3 = 0.2857142857142857^3",
                "solution": "0.02332361516034985"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "complex_quadratic",
        "id": 100,
        "kwargs": [
            "prob_type=0",
            "max_range=10"
        ],
        "name": "complex Quadratic Equation",
        "samples": [
            {
                "problem": "Find the roots of given Quadratic Equation x^2 + 9x + 9 = 0",
                "solution": "simplified solution : ((-1.146, -7.854)), generalized solution : ((-9 + sqrt(45))/2*1, (-9 - sqrt(45))/2*1)"
            },
            {
                "problem": "Find the roots of given Quadratic Equation 5x^2 + 7x + 1 = 0",
                "solution": "simplified solution : ((-0.161, -1.239)), generalized solution : ((-7 + sqrt(29))/2*5, (-7 - sqrt(29))/2*5)"
            },
            {
                "problem": "Find the roots of given Quadratic Equation 3x^2 + 9x + 1 = 0",
                "solution": "simplified solution : ((-0.116, -2.884)), generalized solution : ((-9 + sqrt(69))/2*3, (-9 - sqrt(69))/2*3)"
            },
            {
                "problem": "Find the roots of given Quadratic Equation x^2 + 6x + 9 = 0",
                "solution": "simplified solution : ((-3.0, -3.0)), generalized solution : ((-6 + 0)/2*1, (-6 - 0)/2*1)"
            },
            {
                "problem": "Find the roots of given Quadratic Equation 7x^2 + 7x + 1 = 0",
                "solution": "simplified solution : ((-0.173, -0.827)), generalized solution : ((-7 + sqrt(21))/2*7, (-7 - sqrt(21))/2*7)"
            },
            {
                "problem": "Find the roots of given Quadratic Equation 2x^2 + 9x + 1 = 0",
                "solution": "simplified solution : ((-0.114, -4.386)), generalized solution : ((-9 + sqrt(73))/2*2, (-9 - sqrt(73))/2*2)"
            },
            {
                "problem": "Find the roots of given Quadratic Equation 3x^2 + 7x + 3 = 0",
                "solution": "simplified solution : ((-0.566, -1.768)), generalized solution : ((-7 + sqrt(13))/2*3, (-7 - sqrt(13))/2*3)"
            },
            {
                "problem": "Find the roots of given Quadratic Equation 3x^2 + 6x + 3 = 0",
                "solution": "simplified solution : ((-1.0, -1.0)), generalized solution : ((-6 + 0)/2*3, (-6 - 0)/2*3)"
            },
            {
                "problem": "Find the roots of given Quadratic Equation 2x^2 + 9x + 1 = 0",
                "solution": "simplified solution : ((-0.114, -4.386)), generalized solution : ((-9 + sqrt(73))/2*2, (-9 - sqrt(73))/2*2)"
            },
            {
                "problem": "Find the roots of given Quadratic Equation 2x^2 + 6x + 1 = 0",
                "solution": "simplified solution : ((-0.177, -2.823)), generalized solution : ((-6 + sqrt(28))/2*2, (-6 - sqrt(28))/2*2)"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "is_leap_year",
        "id": 101,
        "kwargs": [
            "minNumber=1900",
            "maxNumber=2099"
        ],
        "name": "Leap Year or Not",
        "samples": [
            {
                "problem": "Year 2058 ",
                "solution": "is not a leap year"
            },
            {
                "problem": "Year 2094 ",
                "solution": "is not a leap year"
            },
            {
                "problem": "Year 1902 ",
                "solution": "is not a leap year"
            },
            {
                "problem": "Year 1942 ",
                "solution": "is not a leap year"
            },
            {
                "problem": "Year 2079 ",
                "solution": "is not a leap year"
            },
            {
                "problem": "Year 1946 ",
                "solution": "is not a leap year"
            },
            {
                "problem": "Year 2010 ",
                "solution": "is not a leap year"
            },
            {
                "problem": "Year 2073 ",
                "solution": "is not a leap year"
            },
            {
                "problem": "Year 2068 ",
                "solution": "is a leap year"
            },
            {
                "problem": "Year 2052 ",
                "solution": "is a leap year"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "minutes_to_hours",
        "id": 102,
        "kwargs": [
            "maxMinutes=999"
        ],
        "name": "Minute to Hour conversion",
        "samples": [
            {
                "problem": "Convert 403 minutes to Hours & Minutes",
                "solution": "6 hours and 43 minutes"
            },
            {
                "problem": "Convert 411 minutes to Hours & Minutes",
                "solution": "6 hours and 51 minutes"
            },
            {
                "problem": "Convert 55 minutes to Hours & Minutes",
                "solution": "0 hours and 55 minutes"
            },
            {
                "problem": "Convert 266 minutes to Hours & Minutes",
                "solution": "4 hours and 26 minutes"
            },
            {
                "problem": "Convert 788 minutes to Hours & Minutes",
                "solution": "13 hours and 8 minutes"
            },
            {
                "problem": "Convert 635 minutes to Hours & Minutes",
                "solution": "10 hours and 35 minutes"
            },
            {
                "problem": "Convert 166 minutes to Hours & Minutes",
                "solution": "2 hours and 46 minutes"
            },
            {
                "problem": "Convert 282 minutes to Hours & Minutes",
                "solution": "4 hours and 42 minutes"
            },
            {
                "problem": "Convert 644 minutes to Hours & Minutes",
                "solution": "10 hours and 44 minutes"
            },
            {
                "problem": "Convert 482 minutes to Hours & Minutes",
                "solution": "8 hours and 2 minutes"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "decimal_to_bcd",
        "id": 103,
        "kwargs": [
            "maxNumber=10000"
        ],
        "name": "Decimal to Binary Coded Decimal",
        "samples": [
            {
                "problem": "BCD of Decimal Number 7839 is = ",
                "solution": 114915
            },
            {
                "problem": "BCD of Decimal Number 8720 is = ",
                "solution": 2210
            },
            {
                "problem": "BCD of Decimal Number 3927 is = ",
                "solution": 1557
            },
            {
                "problem": "BCD of Decimal Number 9669 is = ",
                "solution": 25125
            },
            {
                "problem": "BCD of Decimal Number 2166 is = ",
                "solution": 876
            },
            {
                "problem": "BCD of Decimal Number 7203 is = ",
                "solution": 11223
            },
            {
                "problem": "BCD of Decimal Number 9170 is = ",
                "solution": 23132
            },
            {
                "problem": "BCD of Decimal Number 2337 is = ",
                "solution": 921
            },
            {
                "problem": "BCD of Decimal Number 6899 is = ",
                "solution": 110153
            },
            {
                "problem": "BCD of Decimal Number 1884 is = ",
                "solution": 7512
            }
        ],
        "subject": "computer_science"
    },
    {
        "function_name": "circumference",
        "id": 104,
        "kwargs": [
            "maxRadius=100"
        ],
        "name": "Circumference",
        "samples": [
            {
                "problem": "Circumference of circle with radius 73",
                "solution": 458.6725274241098
            },
            {
                "problem": "Circumference of circle with radius 78",
                "solution": 490.0884539600077
            },
            {
                "problem": "Circumference of circle with radius 65",
                "solution": 408.4070449666731
            },
            {
                "problem": "Circumference of circle with radius 38",
                "solution": 238.76104167282426
            },
            {
                "problem": "Circumference of circle with radius 85",
                "solution": 534.0707511102648
            },
            {
                "problem": "Circumference of circle with radius 6",
                "solution": 37.69911184307752
            },
            {
                "problem": "Circumference of circle with radius 46",
                "solution": 289.02652413026095
            },
            {
                "problem": "Circumference of circle with radius 92",
                "solution": 578.0530482605219
            },
            {
                "problem": "Circumference of circle with radius 94",
                "solution": 590.6194188748811
            },
            {
                "problem": "Circumference of circle with radius 82",
                "solution": 515.221195188726
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "combine_like_terms",
        "id": 105,
        "kwargs": [
            "maxCoef=10",
            "maxExp=20",
            "maxTerms=10"
        ],
        "name": "Combine Like terms",
        "samples": [
            {
                "problem": "4x^2 + 6x^1",
                "solution": "6x^1 + 4x^2 "
            },
            {
                "problem": "4x^1 + 8x^1",
                "solution": "12x^1 "
            },
            {
                "problem": "10x^6 + 9x^8 + 8x^1 + 9x^4 + 2x^2 + 2x^4 + 6x^5 + 9x^3 + 8x^4 + 3x^7",
                "solution": "8x^1 + 2x^2 + 9x^3 + 19x^4 + 6x^5 + 10x^6 + 3x^7 + 9x^8 "
            },
            {
                "problem": "1x^2 + 5x^1",
                "solution": "5x^1 + 1x^2 "
            },
            {
                "problem": "3x^8 + 7x^7 + 9x^2 + 3x^8 + 3x^1 + 10x^7 + 5x^6 + 3x^2 + 10x^7 + 4x^8",
                "solution": "3x^1 + 12x^2 + 5x^6 + 27x^7 + 10x^8 "
            },
            {
                "problem": "3x^1 + 7x^1 + 10x^1 + 8x^1",
                "solution": "28x^1 "
            },
            {
                "problem": "5x^7 + 1x^4 + 6x^1 + 7x^4 + 3x^6 + 9x^4 + 4x^4 + 2x^4 + 5x^4",
                "solution": "6x^1 + 28x^4 + 3x^6 + 5x^7 "
            },
            {
                "problem": "8x^6 + 10x^6 + 6x^6 + 8x^4 + 5x^3 + 7x^3 + 1x^3 + 6x^2",
                "solution": "6x^2 + 13x^3 + 8x^4 + 24x^6 "
            },
            {
                "problem": "2x^3 + 5x^3 + 3x^3 + 9x^4 + 4x^6 + 5x^4 + 9x^3 + 2x^6",
                "solution": "19x^3 + 14x^4 + 6x^6 "
            },
            {
                "problem": "8x^2 + 7x^6 + 1x^5 + 8x^1 + 3x^6 + 4x^1 + 4x^7 + 5x^4 + 3x^9 + 8x^2",
                "solution": "12x^1 + 16x^2 + 5x^4 + 1x^5 + 10x^6 + 4x^7 + 3x^9 "
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "signum_function",
        "id": 106,
        "kwargs": [
            "min=-999",
            "max=999"
        ],
        "name": "signum function",
        "samples": [
            {
                "problem": "signum of -219 is =",
                "solution": "-1"
            },
            {
                "problem": "signum of -901 is =",
                "solution": "-1"
            },
            {
                "problem": "signum of 335 is =",
                "solution": "1"
            },
            {
                "problem": "signum of 885 is =",
                "solution": "1"
            },
            {
                "problem": "signum of -385 is =",
                "solution": "-1"
            },
            {
                "problem": "signum of -360 is =",
                "solution": "-1"
            },
            {
                "problem": "signum of -291 is =",
                "solution": "-1"
            },
            {
                "problem": "signum of -448 is =",
                "solution": "-1"
            },
            {
                "problem": "signum of 590 is =",
                "solution": "1"
            },
            {
                "problem": "signum of 36 is =",
                "solution": "1"
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "conditional_probability",
        "id": 107,
        "kwargs": [
            ""
        ],
        "name": "Conditional Probability",
        "samples": [
            {
                "problem": "Someone tested positive for a nasty disease which only 1.86% of population have. Test sensitivity (true positive) is equal to SN= 92.68% whereas test specificity (true negative) SP= 96.53%. What is the probability that this guy really has that disease?",
                "solution": "33.61%"
            },
            {
                "problem": "Someone tested positive for a nasty disease which only 1.34% of population have. Test sensitivity (true positive) is equal to SN= 91.88% whereas test specificity (true negative) SP= 95.48%. What is the probability that this guy really has that disease?",
                "solution": "21.64%"
            },
            {
                "problem": "Someone tested positive for a nasty disease which only 1.55% of population have. Test sensitivity (true positive) is equal to SN= 90.40% whereas test specificity (true negative) SP= 94.66%. What is the probability that this guy really has that disease?",
                "solution": "21.04%"
            },
            {
                "problem": "Someone tested positive for a nasty disease which only 1.39% of population have. Test sensitivity (true positive) is equal to SN= 96.20% whereas test specificity (true negative) SP= 93.60%. What is the probability that this guy really has that disease?",
                "solution": "17.48%"
            },
            {
                "problem": "Someone tested positive for a nasty disease which only 0.96% of population have. Test sensitivity (true positive) is equal to SN= 99.55% whereas test specificity (true negative) SP= 97.49%. What is the probability that this guy really has that disease?",
                "solution": "27.77%"
            },
            {
                "problem": "Someone tested positive for a nasty disease which only 0.77% of population have. Test sensitivity (true positive) is equal to SN= 90.82% whereas test specificity (true negative) SP= 96.11%. What is the probability that this guy really has that disease?",
                "solution": "15.34%"
            },
            {
                "problem": "Someone tested positive for a nasty disease which only 0.90% of population have. Test sensitivity (true positive) is equal to SN= 99.41% whereas test specificity (true negative) SP= 97.85%. What is the probability that this guy really has that disease?",
                "solution": "29.57%"
            },
            {
                "problem": "Someone tested positive for a nasty disease which only 0.55% of population have. Test sensitivity (true positive) is equal to SN= 91.66% whereas test specificity (true negative) SP= 98.07%. What is the probability that this guy really has that disease?",
                "solution": "20.8%"
            },
            {
                "problem": "Someone tested positive for a nasty disease which only 1.77% of population have. Test sensitivity (true positive) is equal to SN= 90.43% whereas test specificity (true negative) SP= 96.85%. What is the probability that this guy really has that disease?",
                "solution": "34.09%"
            },
            {
                "problem": "Someone tested positive for a nasty disease which only 1.37% of population have. Test sensitivity (true positive) is equal to SN= 93.11% whereas test specificity (true negative) SP= 90.50%. What is the probability that this guy really has that disease?",
                "solution": "11.98%"
            }
        ],
        "subject": "statistics"
    },
    {
        "function_name": "arc_length",
        "id": 108,
        "kwargs": [
            "maxRadius=49",
            "maxAngle=359"
        ],
        "name": "Arc length of Angle",
        "samples": [
            {
                "problem": "Given radius, 2 and angle, 296. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 10.33235"
            },
            {
                "problem": "Given radius, 45 and angle, 338. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 265.46458"
            },
            {
                "problem": "Given radius, 15 and angle, 206. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 53.93067"
            },
            {
                "problem": "Given radius, 47 and angle, 202. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 165.70156"
            },
            {
                "problem": "Given radius, 39 and angle, 332. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 225.98523"
            },
            {
                "problem": "Given radius, 6 and angle, 198. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 20.73451"
            },
            {
                "problem": "Given radius, 24 and angle, 251. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 105.13863"
            },
            {
                "problem": "Given radius, 30 and angle, 287. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 150.27285"
            },
            {
                "problem": "Given radius, 36 and angle, 341. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 214.25662"
            },
            {
                "problem": "Given radius, 14 and angle, 272. Find the arc length of the angle.",
                "solution": "Arc length of the angle = 66.46214"
            }
        ],
        "subject": "geometry"
    },
    {
        "function_name": "binomial_distribution",
        "id": 109,
        "kwargs": [
            ""
        ],
        "name": "Binomial distribution",
        "samples": [
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 30.8% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 12 pistons will contain no more than 1 rejected pistons?",
                "solution": 7.65
            },
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 39.79% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 14 pistons will contain no more than 2 rejected pistons?",
                "solution": 4.11
            },
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 38.65% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 20 pistons will contain no more than 8 rejected pistons?",
                "solution": 64.35
            },
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 40.37% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 16 pistons will contain no more than 9 rejected pistons?",
                "solution": 93.8
            },
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 34.01% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 13 pistons will contain no more than 7 rejected pistons?",
                "solution": 96.1
            },
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 32.47% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 11 pistons will contain no more than 3 rejected pistons?",
                "solution": 49.74
            },
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 39.73% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 12 pistons will contain no more than 3 rejected pistons?",
                "solution": 23.11
            },
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 39.2% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain no more than 6 rejected pistons?",
                "solution": 95.09
            },
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 34.84% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 17 pistons will contain no more than 5 rejected pistons?",
                "solution": 42.52
            },
            {
                "problem": "A manufacturer of metal pistons finds that, on average, 33.81% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 15 pistons will contain no more than 4 rejected pistons?",
                "solution": 38.89
            }
        ],
        "subject": "misc"
    },
    {
        "function_name": "stationary_points",
        "id": 110,
        "kwargs": [
            "maxExp=3",
            "maxCoef=10"
        ],
        "name": "Stationary Points",
        "samples": [
            {
                "problem": "f(x)=x^3 + 4*x^2 + 4*x + 5",
                "solution": "(-2,5),(-2/3,103/27)"
            },
            {
                "problem": "f(x)=2*x^3 + 10*x^2 + 4*x + 8",
                "solution": "(-5/3 - sqrt(19)/3,2*(-5/3 - sqrt(19)/3)**3 - 4*sqrt(19)/3 + 4/3 + 10*(-5/3 - sqrt(19)/3)**2),(-5/3 + sqrt(19)/3,2*(-5/3 + sqrt(19)/3)**3 + 10*(-5/3 + sqrt(19)/3)**2 + 4/3 + 4*sqrt(19)/3)"
            },
            {
                "problem": "f(x)=3*x^3 + 3*x^2",
                "solution": "(-2/3,4/9),(0,0)"
            },
            {
                "problem": "f(x)=4*x^3 + 8*x^2 + 5*x + 3",
                "solution": "(-5/6,56/27),(-1/2,2)"
            },
            {
                "problem": "f(x)=6*x^3 + 7*x^2 + 1",
                "solution": "(-7/9,586/243),(0,1)"
            },
            {
                "problem": "f(x)=x^2 + 3",
                "solution": "(0,3)"
            },
            {
                "problem": "f(x)=4*x^3 + 7*x^2 + x + 4",
                "solution": "(-7/12 - sqrt(37)/12,4*(-7/12 - sqrt(37)/12)**3 - sqrt(37)/12 + 41/12 + 7*(-7/12 - sqrt(37)/12)**2),(-7/12 + sqrt(37)/12,4*(-7/12 + sqrt(37)/12)**3 + 7*(-7/12 + sqrt(37)/12)**2 + sqrt(37)/12 + 41/12)"
            },
            {
                "problem": "f(x)=x^3 + 10*x^2 + 2*x + 8",
                "solution": "(-10/3 - sqrt(94)/3,(-10/3 - sqrt(94)/3)**3 - 2*sqrt(94)/3 + 4/3 + 10*(-10/3 - sqrt(94)/3)**2),(-10/3 + sqrt(94)/3,(-10/3 + sqrt(94)/3)**3 + 10*(-10/3 + sqrt(94)/3)**2 + 4/3 + 2*sqrt(94)/3)"
            },
            {
                "problem": "f(x)=3*x^3 + 5*x^2 + x + 4",
                "solution": "(-1,5),(-1/9,959/243)"
            },
            {
                "problem": "f(x)=3*x^3 + 8*x^2 + 6*x + 9",
                "solution": "(-8/9 - sqrt(10)/9,3*(-8/9 - sqrt(10)/9)**3 - 2*sqrt(10)/3 + 11/3 + 8*(-8/9 - sqrt(10)/9)**2),(-8/9 + sqrt(10)/9,3*(-8/9 + sqrt(10)/9)**3 + 2*sqrt(10)/3 + 8*(-8/9 + sqrt(10)/9)**2 + 11/3)"
            }
        ],
        "subject": "calculus"
    },
    {
        "function_name": "expanding",
        "id": 111,
        "kwargs": [
            "range_x1=10",
            "range_x2=10",
            "range_a=10",
            "range_b=10"
        ],
        "name": "Expanding Factored Binomial",
        "samples": [
            {
                "problem": "(-1x-7)(+4x-8)",
                "solution": "-4*x^2-20*x+56"
            },
            {
                "problem": "(-5x-2)(+9x+7)",
                "solution": "-45*x^2-53*x-14"
            },
            {
                "problem": "(-7x-10)(-1x-10)",
                "solution": "7*x^2+80*x+100"
            },
            {
                "problem": "(x-4)(+2x-7)",
                "solution": "2*x^2-15*x+28"
            },
            {
                "problem": "(7x+2)(+7x+1)",
                "solution": "49*x^2+21*x+2"
            },
            {
                "problem": "(4x+6)(+2x+7)",
                "solution": "8*x^2+40*x+42"
            },
            {
                "problem": "(7x-2)(+4x-8)",
                "solution": "28*x^2-64*x+16"
            },
            {
                "problem": "(2x+9)(-2x-9)",
                "solution": "-4*x^2-36*x-81"
            },
            {
                "problem": "(4x)(-6x+5)",
                "solution": "-24*x^2+20*x"
            },
            {
                "problem": "(-7x+9)(-6x-4)",
                "solution": "42*x^2-26*x-36"
            }
        ],
        "subject": "algebra"
    },
    {
        "function_name": "area_of_circle",
        "id": 112,
        "kwargs": [
            "maxRadius=100"
        ],
        "name": "Area of Circle",
        "samples": [
            {
                "problem": "Area of circle with radius 45",
                "solution": 6364.285714285714
            },
            {
                "problem": "Area of circle with radius 98",
                "solution": 30184.0
            },
            {
                "problem": "Area of circle with radius 77",
                "solution": 18634.0
            },
            {
                "problem": "Area of circle with radius 19",
                "solution": 1134.5714285714287
            },
            {
                "problem": "Area of circle with radius 38",
                "solution": 4538.285714285715
            },
            {
                "problem": "Area of circle with radius 49",
                "solution": 7546.0
            },
            {
                "problem": "Area of circle with radius 32",
                "solution": 3218.285714285714
            },
            {
                "problem": "Area of circle with radius 34",
                "solution": 3633.1428571428573
            },
            {
                "problem": "Area of circle with radius 58",
                "solution": 10572.571428571428
            },
            {
                "problem": "Area of circle with radius 51",
                "solution": 8174.571428571428
            }
        ],
        "subject": "geometry"
    }
]
