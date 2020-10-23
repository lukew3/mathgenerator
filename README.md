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
| 0 | Addition | 37+8= | 45 | addition |
| 1 | Subtraction | 45-36= | 9 | subtraction |
| 2 | Multiplication | 92*1= | 92 | multiplication |
| 3 | Division | 26/67= | 0.3880597014925373 | division |
| 4 | Binary Complement 1s | 010111011= | 101000100 | binary_complement_1s |
| 5 | Modulo Division | 64%55= | 9 | modulo_division |
| 6 | Square Root | sqrt(81)= | 9 | square_root |
| 7 | Power Rule Differentiation | 10x^7 + 5x^9 + 8x^9 + 3x^2 + 7x^5 | 70x^6 + 45x^8 + 72x^8 + 6x^1 + 35x^4 | power_rule_differentiation |
| 8 | Square | 16^2= | 256 | square |
| 9 | LCM (Least Common Multiple) | LCM of 16 and 1 = | 16 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 2 and 18 =  | 2 | gcd |
| 11 | Basic Algebra | 4x + 5 = 10 | 5/4 | basic_algebra |
| 12 | Logarithm | log2(2) | 1 | log |
| 13 | Easy Division | 4/1 =  | 4 | int_division |
| 14 | Decimal to Binary | Binary of 37= | 100101 | decimal_to_binary |
| 15 | Binary to Decimal | 0100110 | 38 | binary_to_decimal |
| 16 | Fraction Division | (10/8)/(1/2) | 5/2 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 7 * [[7, 10], [3, 9]] =  | [[49,70],[21,63]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 9 2 5 =  | (7.347880794884119e-16+12j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 8, 33 and 19 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (-2,1),(6,2)= | (2.0,1.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+13x+30 | (x+3)(x+10) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 57 and 85 =  | 38 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -3x + 3y = 39, 4x - 8y = -72 | x = -8, y = 5 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (17, 21) and (-14, 1) | sqrt(1361) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 17 and 14 =  | 22.02 | pythagorean_theorem |
| 26 | Linear Equations | -16x + 4y = -160, 12x + -1y = 96 | x = 7, y = -12 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 117 | [3, 3, 13] | prime_factors |
| 28 | Fraction Multiplication | (1/2)*(1/4) | 1/8 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 19 sides | 161.05 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 17 objects picked 4 at a time  | 2380 | combinations |
| 31 | Factorial | 6! =  | 720 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 3m is | 54 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 17m, 7m, 16m is | 1006 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 4m and radius = 19m is | 2745 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 7m is | 343 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 11m, 18m, 9m is | 1782 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 28m and radius = 17m is | 25421 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 21m and radius = 7m is | 640 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 23m and radius = 13m is | 4070 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 86 and 2 =  | [1, 2] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 10/4x - 8 and y = -9/4x - 2 | (24/19, -92/19) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 20 objects picked 5 at a time =   | 1860480 | permutation |
| 43 | Cross Product of 2 Vectors | [17, -12, 17] X [-13, -17, 10] =  | [169, -391, -445] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 4/10 and 10/3? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 8120 dollars, 3% rate of interest and for a time period of 9 years is =  | 2192.4 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>1</td><td>4</td><td>-3</td><td>-9</td></tr><tr><td>-10</td><td>-9</td><td>-5</td><td>7</td></tr><tr><td>5</td><td>8</td><td>-7</td><td>5</td></tr></table>and<table><tr><td>-6</td><td>-1</td><td>0</td></tr><tr><td>-4</td><td>7</td><td>-7</td></tr><tr><td>3</td><td>0</td><td>2</td></tr><tr><td>-7</td><td>-8</td><td>-7</td></tr></table> | <table><tr><td>32</td><td>99</td><td>29</td></tr><tr><td>32</td><td>-109</td><td>4</td></tr><tr><td>-118</td><td>11</td><td>-105</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 7 upto 2 decimal places is: | 1.91 | cube_root |
| 48 | Power Rule Integration | 8x^1 | (8/1)x^2 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 44 , 100, 31 = | 185 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 19x^2+181x+1=0 | [-0.01, -9.52] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 9 and 4 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 2 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 2^1 = | 2 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [241, 269, 277, 202, 271, 215, 260, 265, 216, 267, 297, 219, 262, 273, 212, 268, 294, 210, 286, 235, 270, 231, 272, 289, 245, 283, 250] with 80% confidence is | (261.63267428757547, 247.92288126798007) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 57^(1/5) _ 94^(1/7) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 9 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21] | fibonacci_series |
| 57 | Trigonometric Values | What is sin(90)? | 1 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 10 sides =  | 1440 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[39, 33, 10, 49, 21, 9, 9, 20, 50, 10, 41, 12, 50, 50, 29] | The Mean is 28.8 , Standard Deviation is 262.56000000000006, Variance is 16.203703280423277 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 3m is | 113.09733552923255 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 38 m =  | 229847.29611703884 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 24th Fibonacci number? | 46368 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 173 and SP = 357 is:  | 106.35838150289017 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 1000110 | 0x46 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (14-4j) * (5-12j) =  | (22-188j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [11, 66, 396, 2376, 14256, 85536] ,Find the value of a,common ratio,11th term value, sum upto 7th term | The value of a is 11, common ratio is 6 , 11th term is 665127936 , sum upto 7th term is 615857.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 61 and 67 =  | (61*67)^(1/2) = 63.92964883369844 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 62 and 84 =  |  2/((1/62) + (1/84)) = 71.34246575342466 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[783.9868296299311, 482.5604033573253, 863.1029339509203, 956.7790571651393, 863.0425006034349] is: | 1803.5285106129884 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [379.65, 308.56] and [100.22, 686.67] is: | 0.74 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 18 and 79 =  | 61 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [14, 11, -1] . [-20, 10, 18] =  | -188 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 111110 = | 10 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[68, 2, 85], [70, 19, 47], [17, 38, 6]]) is: | Matrix([[-1672/85707, 3218/85707, -169/9523], [379/85707, -1037/85707, 306/9523], [779/28569, -850/28569, 128/9523]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 18 and angle, 67. Find the area of the sector. | Area of sector = 189.43804 | sector_area |
| 76 | Mean and Median | Given the series of numbers [40, 66, 30, 32, 78, 27, 6, 35, 86, 3]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 40.3 and Arithmetic median of this series is 33.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[65, 36], [75, 98]]) =  |  3670 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 9481 dollars, 5% rate of interest and for a time period of 1 year is =  | 9955.05 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 972= | 0x3cc | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 92% of 17? | Required percentage = 15.64% | percentage |
| 81 | Celsius To Fahrenheit | Convert 68 degrees Celsius to degrees Fahrenheit = | 154.4 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 58 of the AP series: 21, -42, -105 ...  | -3570 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 6 terms of the AP series: -37, -108, -179 ...  | -1287.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 988 in Octal is:  | 0o1734 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 1930 in Roman Numerals is:  | MCMXXX | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 87 in radians is =  | 1.52 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(cos(x)+7*x^(-4))/dx | -sin(x) - 28/x^5 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 12x^2 + 95x + 87 is =  | 138.5 | definite_integral |
| 90 | isprime | 77 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 3 is =  | 13891 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 21.63exp(i-2.16) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={1, 3, 4, 5, 7} ,b={1, 3, 4, 7}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 3, 4, 5, 7},Intersection is {1, 3, 4, 7}, a-b is {5},b-a is set(), Symmetric difference is {5} | set_operation |
| 94 | Base Conversion | Convert 6C38 from base 15 to base 10. | 23003 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 15 and height, 67? | CSA of cylinder = 6314.6 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 11 sided polygon with lengths of [34, 21, 86, 40, 83, 32, 4, 75, 86, 106, 48]cm is:  | 615 | perimeter_of_polygons |
| 97 | Power of Powers | The 4^8^4 = 4^(8*4) = 4^32 | 18446744073709551616 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 17^6 and 17^5 = 17^(6-5) = 17^1 | 17 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 45^7 and 41^7 = (45/41)^7 = 1.0975609756097562^7 | 1.9186713887127431 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 6x^2 + 8x + 2 = 0 | simplified solution : ((-0.333, -1.0)), generalized solution : ((-8 + 4)/2*6, (-8 - 4)/2*6) | complex_quadratic |
| 101 | Conditional Probability | Someone tested positive for a nasty disease which only 1.96% of population have. Test sensitivity (true positive) is equal to SN= 99.00% whereas test specificity (true negative) SP= 94.80%. What is the probability that this guy really has that disease? | 27.57% | conitionalProbability |
