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
| 0 | Addition | 43+23= | 66 | addition |
| 1 | Subtraction | 84-10= | 74 | subtraction |
| 2 | Multiplication | 6*2= | 12 | multiplication |
| 3 | Division | 87/23= | 3.782608695652174 | division |
| 4 | Binary Complement 1s | 1011= | 0100 | binary_complement_1s |
| 5 | Modulo Division | 68%0= | 0 | modulo_division |
| 6 | Square Root | sqrt(81)= | 9 | square_root |
| 7 | Power Rule Differentiation | 7x^1 + 9x^10 + 4x^3 + 7x^6 | 7x^0 + 90x^9 + 12x^2 + 42x^5 | power_rule_differentiation |
| 8 | Square | 19^2= | 361 | square |
| 9 | LCM (Least Common Multiple) | LCM of 9 and 6 = | 18 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 19 and 12 =  | 1 | gcd |
| 11 | Basic Algebra | 2x + 1 = 10 | 9/2 | basic_algebra |
| 12 | Logarithm | log2(128) | 7 | log |
| 13 | Easy Division | 50/2 =  | 25 | int_division |
| 14 | Decimal to Binary | Binary of 59= | 111011 | decimal_to_binary |
| 15 | Binary to Decimal | 10011 | 19 | binary_to_decimal |
| 16 | Fraction Division | (6/5)/(7/1) | 6/35 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 1 * [[7, 7], [4, 5]] =  | [[7,7],[4,5]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 19 6 19 =  | 56.28498911788115 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 29, 34 and 13 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (-8,2),(5,-17)= | (-1.5,-7.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+8x | (x+8)(x) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 64 and 78 =  | 38 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | 8x - 3y = -63, 9x + 10y = -111 | x = -9, y = -3 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-12, -3) and (10, -9) | sqrt(520) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 11 and 18 =  | 21.10 | pythagorean_theorem |
| 26 | Linear Equations | 20x + 2y = -42-8x + 7y = 165 | x = -4, y = 19 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 62 | [2, 31] | prime_factors |
| 28 | Fraction Multiplication | (9/8)*(4/7) | 9/14 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 7 sides | 128.57 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 14 objects picked 7 at a time  | 3432 | combinations |
| 31 | Factorial | 6! =  | 720 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 16m is | 1536 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 11m, 12m, 5m is | 494 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 9m and radius = 10m is | 1193 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 20m is | 8000 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 19m, 9m, 14m is | 2394 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 15m and radius = 1m is | 47 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 35m and radius = 11m is | 1647 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 15m and radius = 8m is | 1005 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 74 and 18 =  | [1, 2] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 5x + 8 and y = -5/5x + 10 | (1/3, 29/3) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 15 objects picked 6 at a time =   | 3603600 | permutation |
| 43 | Cross Product of 2 Vectors | [7, -11, -16] X [2, -2, 11] =  | [-153, -109, 8] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 2/9 and 3/9? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 7140 dollars, 8% rate of interest and for a time period of 10 years is =  | 5712.0 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>5</td><td>4</td></tr><tr><td>6</td><td>-5</td></tr></table>and<table><tr><td>-2</td><td>-5</td><td>10</td><td>5</td></tr><tr><td>-8</td><td>-8</td><td>-6</td><td>2</td></tr></table> | <table><tr><td>-42</td><td>-57</td><td>26</td><td>33</td></tr><tr><td>28</td><td>10</td><td>90</td><td>20</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 417 upto 2 decimal places is: | 7.47 | cube_root |
| 48 | Power Rule Integration | 10x^10 | (10/10)x^11 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 170 , 23, 98 = | 69 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 45x^2+157x+48=0 | [-0.34, -3.15] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 12 and 16 =  | 4 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 12 = | 25/216 | dice_sum_probability |
| 53 | Exponentiation | 13^3 = | 2197 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [203, 218, 249, 286, 283, 204, 214, 252, 292, 291, 270, 256, 248, 227, 207, 264, 260, 261, 245, 294, 281, 233, 244, 240, 255, 210, 250, 216, 222, 293, 287, 237, 257, 274, 205] with 90% confidence is | (257.3268184855506, 241.41603865730656) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 89^(1/4) _ 49^(1/2) | < | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 11 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55] | fibonacci_series |
| 57 | Trigonometric Values | What is cos(0)? | 1 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 5 sides =  | 540 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[31, 28, 42, 17, 18, 27, 29, 38, 37, 34, 20, 46, 40, 13, 9] | The Mean is 28.6 , Standard Deviation is 117.17333333333335, Variance is 10.824663197223892 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 9m is | 1017.8760197630929 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 45 m =  | 381703.5074111598 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 89th Fibonacci number? | 1779979416004719360 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 611 and SP = 934 is:  | 52.864157119476275 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 1 | 0x1 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (-7+0j) * (1+18j) =  | (-7-126j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [3, 36, 432, 5184, 62208, 746496] ,Find the value of a,common ratio,11th term value, sum upto 8th term | The value of a is 3, common ratio is 12 , 11th term is 185752092672 , sum upto 8th term is 117267735.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 69 , 84 , 53 , 42 =  | (69*84*53*42)^(1/4) = 59.93263663932908 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 38 , 26 , 56 , 54 =  |  4/((1/38) + (1/26) + (1/56) + (1/54)) = 39.54406120126003 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[404.01048129643635, 493.0541616029289, 462.1933998344141, 423.5178469230799] is: | 894.045290119131 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [754.1998988977049, 801.3293889971126, 64.28064667477207, 995.3287765441996, 264.0816063333957, 611.5398134986185, 856.5578548001416, 50.735010026939364, 572.2950776638381, 930.5293279220055, 524.3714207350181, 735.6775022444679, 438.8794763353797, 344.63393543289243] and [657.7394862034466, 411.3411278292859, 992.683482628856, 378.5934722176586, 591.4194475121323, 126.57656661119732, 568.2839501217117, 5.58456959028919, 65.00223534144212, 583.768000413094, 930.1126329066044, 899.527968007742, 902.085497788947, 59.26218061705124] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -73 and 34 =  | 107 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [20, 8, -17] . [18, 18, 17] =  | 215 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 10 = | 10 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[3, 21, 81], [28, 53, 11], [42, 89, 63]]) is: | Matrix([[590/321, 981/214, -677/214], [-217/214, -1071/428, 745/428], [133/642, 205/428, -143/428]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 15 and angle, 45. Find the area of the sector. | Area of sector = 88.35729 | sector_area |
| 76 | Mean and Median | Given the series of numbers [96, 21, 61, 79, 63, 59, 56, 85, 77, 8]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 60.5 and Arithmetic median of this series is 62.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[79, 23], [15, 44]]) =  |  3131 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound Interest for a principle amount of 2943 dollars, 1% rate of interest and for a time period of 3 compounded monthly is =  | 2943.0 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 937= | 0x3a9 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 41% of 75? | Required percentage = 30.75% | percentage |
| 81 | Celsius To Fahrenheit | Convert -40 degrees Celsius to degrees Fahrenheit = | -40.0 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 52 of the AP series: 50, -43, -136 ...  | -4693 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 67 terms of the AP series: -45, -87, -129 ...  | -95877.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 200 in Octal is:  | 0o310 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 1225 in Roman Numerals is:  | MCCXXV | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 263 in radians is =  | 4.59 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(cot(x)+9*x^3)/dx | 27*x^2 - cot(x)^2 - 1 | differentiation |
