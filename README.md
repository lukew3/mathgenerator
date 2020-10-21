# mathgenerator

A math problem generator, created for the purpose of giving self-studying students and teaching organizations the means to easily get access to random math problems to suit their needs.

To try out generators, go to <https://todarith.ml/generate/>

If you have an idea for a generator, please add it as an issue and tag it with the "New Generator" label.

## Usage

The project can be install via pip

```bash
pip install mathgenerator
```

Here is an example of how you would generate an addition problem:

```python
from mathgenerator import mathgen

#generate an addition problem
problem, solution = mathgen.addition()

#another way to generate an addition problem using genById()
problem, solution = mathgen.genById(0)
```

## List of Generators

| Id   | Skill                             | Example problem    | Example Solution      | Function Name            |
|------|-----------------------------------|--------------------|-----------------------|--------------------------|
[//]: # list start
| 0 | Addition | 38+43= | 81 | addition |
| 1 | Subtraction | 58-47= | 11 | subtraction |
| 2 | Multiplication | 59*0= | 0 | multiplication |
| 3 | Division | 10/27= | 0.37037037037037035 | division |
| 4 | Binary Complement 1s | 0001= | 1110 | binary_complement_1s |
| 5 | Modulo Division | 52%59= | 52 | modulo_division |
| 6 | Square Root | sqrt(25)= | 5 | square_root |
| 7 | Power Rule Differentiation | 5x^9 + 8x^9 + 9x^7 + 1x^7 + 6x^6 | 45x^8 + 72x^8 + 63x^6 + 7x^6 + 36x^5 | power_rule_differentiation |
| 8 | Square | 16^2= | 256 | square |
| 9 | LCM (Least Common Multiple) | LCM of 19 and 11 = | 209 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 13 and 3 =  | 1 | gcd |
| 11 | Basic Algebra | 9x + 2 = 2 | 0 | basic_algebra |
| 12 | Logarithm | log3(81) | 4 | log |
| 13 | Easy Division | 525/25 =  | 21 | int_division |
| 14 | Decimal to Binary | Binary of 31= | 11111 | decimal_to_binary |
| 15 | Binary to Decimal | 0101100100 | 356 | binary_to_decimal |
| 16 | Fraction Division | (8/1)/(8/5) | 5 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 10 * [[5, 6], [0, 3]] =  | [[50,60],[0,30]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 20 14 20 =  | 131.14495796636635 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 46, 37 and 27 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (-12,13),(15,-19)= | (1.5,-3.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+6x+5 | (x+5)(x+1) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 16 and 76 =  | 88 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -8x + 7y = -63, 6x - 7y = 49 | x = 7, y = -1 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-1, -19) and (16, 19) | sqrt(1733) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 17 and 20 =  | 26.25 | pythagorean_theorem |
| 26 | Linear Equations | -20x + -2y = -58, -16x + -13y = -149 | x = 2, y = 9 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 25 | [5, 5] | prime_factors |
| 28 | Fraction Multiplication | (1/5)*(5/2) | 1/2 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 18 sides | 160.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 13 objects picked 0 at a time  | 1 | combinations |
| 31 | Factorial | 2! =  | 2 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 15m is | 1350 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 9m, 7m, 20m is | 766 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 41m and radius = 20m is | 7665 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 2m is | 8 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 6m, 8m, 18m is | 864 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 24m and radius = 13m is | 12742 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 33m and radius = 20m is | 3681 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 9m and radius = 6m is | 339 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 32 and 64 =  | [1, 2, 4, 8, 16, 32] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -5/5x - 10 and y = 6x + 5 | (-15/7, -55/7) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 13 objects picked 6 at a time =   | 1235520 | permutation |
| 43 | Cross Product of 2 Vectors | [-8, -17, -14] X [18, -14, -16] =  | [76, -380, 418] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 5/2 and 7/9? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 3209 dollars, 8% rate of interest and for a time period of 1 years is =  | 256.72 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>4</td><td>-5</td><td>1</td><td>-10</td></tr><tr><td>-4</td><td>-9</td><td>6</td><td>6</td></tr><tr><td>-10</td><td>-4</td><td>7</td><td>9</td></tr><tr><td>10</td><td>7</td><td>2</td><td>6</td></tr></table>and<table><tr><td>8</td><td>4</td></tr><tr><td>-8</td><td>-2</td></tr><tr><td>-8</td><td>0</td></tr><tr><td>-3</td><td>-2</td></tr></table> | <table><tr><td>94</td><td>46</td></tr><tr><td>-26</td><td>-10</td></tr><tr><td>-131</td><td>-50</td></tr><tr><td>-10</td><td>14</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 722 upto 2 decimal places is: | 8.97 | cube_root |
| 48 | Power Rule Integration | 9x^6 + 6x^2 + 1x^6 | (9/6)x^7 + (6/2)x^3 + (1/6)x^7 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 159 , 23, 7 = | 171 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 54x^2+188x+92=0 | [-0.59, -2.89] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 7 and 2 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 4 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 19^6 = | 47045881 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [251, 210, 218, 219, 213, 250, 270, 206, 229, 289, 265, 277, 271, 282, 291, 239, 290, 217, 256, 254, 234, 268] with 90% confidence is | (259.6447431593175, 240.2643477497734) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 48^(1/9) _ 22^(1/3) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 8 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13] | fibonacci_series |
| 57 | Trigonometric Values | What is tan(60)? | √3 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 5 sides =  | 540 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[31, 24, 39, 33, 38, 19, 25, 27, 44, 42, 41, 46, 42, 23, 40] | The Mean is 34.266666666666666 , Standard Deviation is 72.19555555555556, Variance is 8.496796782055904 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 2m is | 50.26548245743669 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 15 m =  | 14137.166941154068 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 67th Fibonacci number? | 44945570212853 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 265 and SP = 414 is:  | 56.22641509433962 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 01011010 | 0x5a | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (16+6j) * (16-1j) =  | (262+80j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [6, 66, 726, 7986, 87846, 966306] ,Find the value of a,common ratio,7th term value, sum upto 9th term | The value of a is 6, common ratio is 11 , 7th term is 10629366 , sum upto 9th term is 1414768614.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 2 , 89 , 20 , 28 =  | (2*89*20*28)^(1/4) = 17.76855076168954 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 87 , 71 , 16 , 70 =  |  4/((1/87) + (1/71) + (1/16) + (1/70)) = 39.07605671988274 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[253.2276484990589, 544.0394196945418, 597.5968973121911, 717.9622962318546, 957.6520745649788, 708.5846670633276, 239.4894009576103, 228.68124684005775, 265.32483186305046, 796.0656747554028, 766.9152459101839, 713.2680222516796, 524.3978484738747] is: | 2199.444531958941 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [246.46961093317077, 412.8494069125837, 106.09642846104339, 23.89765614826034, 130.68657183702646, 183.13041820744112] and [225.49849035856806, 61.54856418679755, 699.5445055934789, 611.9211383202619, 482.6151709173074, 938.6436827654591] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 2 and -65 =  | 67 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [11, 9, 20] . [19, 5, 18] =  | 614 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 10 = | 10 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[65, 37, 5], [41, 27, 97], [0, 95, 3]]) is: | Matrix([[4567/289393, -14/22261, -1727/289393], [123/578786, -15/44522, 3050/289393], [-3895/578786, 475/44522, -119/289393]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 19 and angle, 313. Find the area of the sector. | Area of sector = 986.04994 | sector_area |
| 76 | Mean and Median | Given the series of numbers [49, 95, 98, 93, 53, 59, 47, 80, 56, 85]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 71.5 and Arithmetic median of this series is 69.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[91, 9], [56, 75]]) =  |  6321 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 6617 dollars, 1% rate of interest and for a time period of 7 year is =  | 7094.32 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 908= | 0x38c | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 11% of 98? | Required percentage = 10.78% | percentage |
| 81 | Celsius To Fahrenheit | Convert -16 degrees Celsius to degrees Fahrenheit = | 3.1999999999999993 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 46 of the AP series: -66, -141, -216 ...  | -3441 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 20 terms of the AP series: 25, -30, -85 ...  | -9950.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 2270 in Octal is:  | 0o4336 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 766 in Roman Numerals is:  | DCCLXVI | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 203 in radians is =  | 3.54 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(tan(x)+7*x^3)/dx | 21*x^2 + tan(x)^2 + 1 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 85x^2 + 48x + 44 is =  | 96.3333 | definite_integral |
| 90 | isprime | 93 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 2 is =  | 10065 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 7.62exp(i1.17) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={2, 5} ,b={8, 9, 4, 1}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 4, 5, 8, 9},Intersection is set(), a-b is {2, 5},b-a is {8, 9, 4, 1}, Symmetric difference is {1, 2, 4, 5, 8, 9} | set_operation |
