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
| 0 | Addition | 42+24= | 66 | addition |
| 1 | Subtraction | 3-0= | 3 | subtraction |
| 2 | Multiplication | 69*0= | 0 | multiplication |
| 3 | Division | 98/90= | 1.0888888888888888 | division |
| 4 | Binary Complement 1s | 100= | 011 | binary_complement_1s |
| 5 | Modulo Division | 37%49= | 37 | modulo_division |
| 6 | Square Root | sqrt(25)= | 5 | square_root |
| 7 | Power Rule Differentiation | 3x^10 + 1x^10 + 3x^9 + 4x^3 + 8x^7 | 30x^9 + 10x^9 + 27x^8 + 12x^2 + 56x^6 | power_rule_differentiation |
| 8 | Square | 6^2= | 36 | square |
| 9 | LCM (Least Common Multiple) | LCM of 8 and 12 = | 24 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 11 and 19 =  | 1 | gcd |
| 11 | Basic Algebra | 1x + 4 = 7 | 3 | basic_algebra |
| 12 | Logarithm | log2(64) | 6 | log |
| 13 | Easy Division | 240/15 =  | 16 | int_division |
| 14 | Decimal to Binary | Binary of 46= | 101110 | decimal_to_binary |
| 15 | Binary to Decimal | 110101 | 53 | binary_to_decimal |
| 16 | Fraction Division | (3/5)/(6/10) | 1 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 7 * [[6, 9], [0, 9]] =  | [[42,63],[0,63]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 18 12 5 =  | (1.5018315853130168e-15+24.526771087935728j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 43, 37 and 16 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (0,10),(3,-19)= | (1.5,-4.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+4x-5 | (x+5)(x-1) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 37 and 88 =  | 55 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -4x - 7y = -63, x - y = 2 | x = 7, y = 5 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (18, -18) and (14, 0) | sqrt(340) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 3 and 14 =  | 14.32 | pythagorean_theorem |
| 26 | Linear Equations | -20x + 5y = 200, 3x + -1y = -32 | x = -8, y = 8 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 70 | [2, 5, 7] | prime_factors |
| 28 | Fraction Multiplication | (8/3)*(8/4) | 16/3 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 19 sides | 161.05 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 14 objects picked 9 at a time  | 2002 | combinations |
| 31 | Factorial | 2! =  | 2 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 6m is | 216 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 6m, 19m, 8m is | 628 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 35m and radius = 4m is | 980 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 6m is | 216 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 16m, 8m, 7m is | 896 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 37m and radius = 16m is | 29757 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 5m and radius = 11m is | 797 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 50m and radius = 13m is | 8848 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 93 and 71 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -1/5x - 3 and y = -4/6x - 10 | (-15, 0) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 14 objects picked 4 at a time =   | 24024 | permutation |
| 43 | Cross Product of 2 Vectors | [4, 7, -12] X [5, -9, -17] =  | [-227, 8, -71] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 4/6 and 10/9? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 9253 dollars, 9% rate of interest and for a time period of 5 years is =  | 4163.85 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>2</td><td>0</td><td>1</td><td>10</td></tr><tr><td>5</td><td>-8</td><td>-7</td><td>5</td></tr><tr><td>3</td><td>1</td><td>-7</td><td>-6</td></tr><tr><td>6</td><td>10</td><td>4</td><td>-1</td></tr></table>and<table><tr><td>-4</td><td>1</td><td>-2</td></tr><tr><td>-10</td><td>-2</td><td>9</td></tr><tr><td>-4</td><td>-1</td><td>-5</td></tr><tr><td>-5</td><td>5</td><td>-8</td></tr></table> | <table><tr><td>-62</td><td>51</td><td>-89</td></tr><tr><td>63</td><td>53</td><td>-87</td></tr><tr><td>36</td><td>-22</td><td>86</td></tr><tr><td>-135</td><td>-23</td><td>66</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 556 upto 2 decimal places is: | 8.22 | cube_root |
| 48 | Power Rule Integration | 2x^3 + 4x^3 | (2/3)x^4 + (4/3)x^4 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 69 , 60, 101 = | 130 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 91x^2+183x+84=0 | [-0.71, -1.3] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 4 and 16 =  | 4 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 11 = | 2/36 | dice_sum_probability |
| 53 | Exponentiation | 7^1 = | 7 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [203, 201, 267, 239, 272, 283, 281, 298, 207, 265, 204, 261, 243, 235, 270, 284, 230, 222, 285, 266] with 80% confidence is | (259.5540983014814, 242.04590169851858) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 73^(1/8) _ 4^(1/5) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 17 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987] | fibonacci_series |
| 57 | Trigonometric Values | What is tan(90)? | ∞ | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 9 sides =  | 1260 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[35, 27, 43, 8, 30, 14, 16, 35, 29, 17, 6, 19, 5, 34, 40] | The Mean is 23.866666666666667 , Standard Deviation is 147.18222222222218, Variance is 12.13186804338978 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 20m is | 5026.548245743669 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 48 m =  | 463246.68632773653 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 59th Fibonacci number? | 956722026041 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Loss percent when CP = 992 and SP = 888 is:  | 10.483870967741936 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 1001 | 0x9 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (6+5j) * (19-20j) =  | (214-25j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [10, 70, 490, 3430, 24010, 168070] ,Find the value of a,common ratio,6th term value, sum upto 11th term | The value of a is 10, common ratio is 7 , 6th term is 168070 , sum upto 11th term is 3295544570.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 41 and 89 =  | (41*89)^(1/2) = 60.40695324215582 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 69 , 15 , 41 , 67 =  |  4/((1/69) + (1/15) + (1/41) + (1/67)) = 33.20189882286996 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[956.6848004224083, 711.3170367487223, 320.15804509062485, 424.1248983996525, 721.5190124346516, 94.2612318602214, 995.8301076180039, 80.46895520905917, 797.0886057296584, 923.9911613599512, 511.29812416326956, 358.730114740062, 2.3571520022257486, 218.67122157401798, 506.1431432680296, 413.8900730468059] is: | 2363.4212638753684 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [232.30943307265463, 306.39298862783016, 623.8368964487579, 808.2182550343807, 837.7902135238608, 194.4689016385932, 369.28549948572345] and [951.1858436627766, 293.2247329611225, 274.2885808744876, 590.5739827721277, 148.45211877240538, 867.5139830165438, 563.3907757868716] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 24 and 42 =  | 18 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [-8, 10, 0] . [20, 15, -17] =  | -10 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 1110011110 = | 1100010 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[32, 97, 28], [31, 73, 53], [42, 33, 47]]) is: | Matrix([[1682/71213, -3635/71213, 3097/71213], [769/71213, 328/71213, -828/71213], [-2043/71213, 3018/71213, -671/71213]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 4 and angle, 17. Find the area of the sector. | Area of sector = 2.37365 | sector_area |
| 76 | Mean and Median | Given the series of numbers [83, 16, 72, 60, 34, 73, 3, 68, 31, 79]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 51.9 and Arithmetic median of this series is 64.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[88, 47], [82, 8]]) =  |  -3150 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 2841 dollars, 7% rate of interest and for a time period of 5 year is =  | 3984.65 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 756= | 0x2f4 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 32% of 78? | Required percentage = 24.96% | percentage |
| 81 | Celsius To Fahrenheit | Convert 63 degrees Celsius to degrees Fahrenheit = | 145.4 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 41 of the AP series: -52, -109, -166 ...  | -2332 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 21 terms of the AP series: -29, 47, 123 ...  | 15351.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 4008 in Octal is:  | 0o7650 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 2529 in Roman Numerals is:  | MMDXXIX | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 174 in radians is =  | 3.04 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(sec(x)+6*x^(-2))/dx | tan(x)*sec(x) - 12/x^3 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 5x^2 + 58x + 38 is =  | 68.6667 | definite_integral |
| 90 | isprime | 83 | True | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 2 is =  | 9224 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 27.59exp(i0.81) | complex_to_polar |
