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
| 0 | Addition | 48+19= | 67 | addition |
| 1 | Subtraction | 31-0= | 31 | subtraction |
| 2 | Multiplication | 44*1= | 44 | multiplication |
| 3 | Division | 19/73= | 0.2602739726027397 | division |
| 4 | Binary Complement 1s | 001110110= | 110001001 | binary_complement_1s |
| 5 | Modulo Division | 99%80= | 19 | modulo_division |
| 6 | Square Root | sqrt(144)= | 12 | square_root |
| 7 | Power Rule Differentiation | 7x^8 + 9x^3 | 56x^7 + 27x^2 | power_rule_differentiation |
| 8 | Square | 15^2= | 225 | square |
| 9 | LCM (Least Common Multiple) | LCM of 18 and 10 = | 90 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 9 and 8 =  | 1 | gcd |
| 11 | Basic Algebra | 9x + 10 = 10 | 0 | basic_algebra |
| 12 | Logarithm | log2(32) | 5 | log |
| 13 | Easy Division | 475/19 =  | 25 | int_division |
| 14 | Decimal to Binary | Binary of 97= | 1100001 | decimal_to_binary |
| 15 | Binary to Decimal | 0110 | 6 | binary_to_decimal |
| 16 | Fraction Division | (3/6)/(7/1) | 1/14 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 12 * [[2, 6], [3, 3]] =  | [[24,72],[36,36]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 12 2 2 =  | (2.0782945349651837e-15+33.94112549695428j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 40, 5 and 39 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (-14,11),(-2,9)= | (-8.0,10.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-5x-14 | (x+2)(x-7) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 27 and 88 =  | 65 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -7x - 7y = -14, -7x - 8y = -18 | x = -2, y = 4 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (5, 9) and (5, 8) | sqrt(1) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 13 and 17 =  | 21.40 | pythagorean_theorem |
| 26 | Linear Equations | 2x + -1y = -19, -14x + -9y = 149 | x = -10, y = -1 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 8 | [2, 2, 2] | prime_factors |
| 28 | Fraction Multiplication | (3/1)*(2/10) | 3/5 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 20 sides | 162.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 16 objects picked 5 at a time  | 4368 | combinations |
| 31 | Factorial | 0! =  | 1 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 4m is | 96 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 19m, 10m, 16m is | 1308 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 32m and radius = 5m is | 1162 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 20m is | 8000 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 11m, 17m, 1m is | 187 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 16m and radius = 17m is | 14526 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 36m and radius = 1m is | 116 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 17m and radius = 17m is | 5144 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 80 and 59 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 10/6x + 6 and y = 5x + 7 | (-3/10, 11/2) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 15 objects picked 1 at a time =   | 15 | permutation |
| 43 | Cross Product of 2 Vectors | [16, -8, 0] X [11, -6, -13] =  | [104, 208, -8] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 4/6 and 7/9? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 1857 dollars, 8% rate of interest and for a time period of 7 years is =  | 1039.92 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>5</td><td>-3</td><td>0</td><td>3</td></tr><tr><td>-6</td><td>-6</td><td>-9</td><td>8</td></tr><tr><td>-4</td><td>-2</td><td>-8</td><td>-2</td></tr></table>and<table><tr><td>-10</td><td>-10</td><td>-2</td><td>10</td></tr><tr><td>-6</td><td>-9</td><td>-5</td><td>-9</td></tr><tr><td>2</td><td>7</td><td>-8</td><td>-8</td></tr><tr><td>-2</td><td>6</td><td>10</td><td>0</td></tr></table> | <table><tr><td>-38</td><td>-5</td><td>35</td><td>77</td></tr><tr><td>62</td><td>99</td><td>194</td><td>66</td></tr><tr><td>40</td><td>-10</td><td>62</td><td>42</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 616 upto 2 decimal places is: | 8.51 | cube_root |
| 48 | Power Rule Integration | 4x^1 | (4/1)x^2 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 72 , 42, 103 = | 143 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 88x^2+181x+68=0 | [-0.49, -1.56] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 2 and 1 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 16 = | 6/216 | dice_sum_probability |
| 53 | Exponentiation | 17^10 = | 2015993900449 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [289, 211, 294, 290, 264, 258, 229, 265, 272, 228, 257, 262, 210, 259, 246, 224, 266, 283, 273, 222, 250, 241, 225, 237] with 99% confidence is | (265.1917573633045, 239.39157597002884) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 81^(1/7) _ 54^(1/9) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 20 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181] | fibonacci_series |
| 57 | Trigonometric Values | What is cos(90)? | 0 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 9 sides =  | 1260 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[43, 23, 43, 13, 16, 40, 36, 19, 17, 39, 45, 26, 12, 17, 12] | The Mean is 26.733333333333334 , Standard Deviation is 151.79555555555555, Variance is 12.3205338989654 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 10m is | 1256.6370614359173 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 93 m =  | 3369282.722751367 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 52th Fibonacci number? | 32951280099 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Loss percent when CP = 798 and SP = 713 is:  | 10.651629072681704 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 0000 | 0x0 | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (14-1j) * (-15+4j) =  | (-206+71j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [8, 24, 72, 216, 648, 1944] ,Find the value of a,common ratio,11th term value, sum upto 8th term | The value of a is 8, common ratio is 3 , 11th term is 472392 , sum upto 8th term is 26240.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 65 , 75 , 65 , 23 =  | (65*75*65*23)^(1/4) = 51.95818275737109 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 2 and 12 =  |  2/((1/2) + (1/12)) = 3.4285714285714284 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[488.10260237588165, 438.9926997215375, 481.4248776631771, 480.58824363943177, 509.73053046857785, 268.09288505668803, 410.3732502610836, 318.6216647891933, 296.4238196042428, 808.0996438115192, 121.7211186065138, 615.1986904309553, 380.29841107431093, 195.23491823519456, 81.69943837555405, 155.69629311805645, 97.46954246782546, 634.0953876946306, 199.72352388042535, 568.2278203619796] is: | 1901.9741243296269 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [955.8351549798066, 177.1594811522551, 900.6055058476991, 712.0208070601419, 601.3956854892953, 628.8267644026017, 893.2727217464875, 492.4340309181726] and [668.7008663033757, 138.7169080640255, 515.5875138676224, 230.03917249114247, 51.099523634880015, 894.1460097286858, 313.47733623460283, 837.2412043583688] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -63 and 84 =  | 147 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [7, -9, 12] . [6, 12, 14] =  | 102 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 11101 = | 11 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[61, 90, 56], [2, 74, 38], [29, 91, 7]]) is: | Matrix([[735/47851, -2233/95702, 181/47851], [-272/47851, 1197/191404, 1103/95702], [491/47851, 2941/191404, -2167/95702]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 17 and angle, 98. Find the area of the sector. | Area of sector = 247.15608 | sector_area |
| 76 | Mean and Median | Given the series of numbers [13, 89, 68, 53, 61, 3, 17, 66, 63, 48]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 48.1 and Arithmetic median of this series is 57.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[49, 6], [62, 19]]) =  |  559 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 7750 dollars, 9% rate of interest and for a time period of 7 year is =  | 14167.3 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 972= | 0x3cc | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 38% of 82? | Required percentage = 31.16% | percentage |
| 81 | Celsius To Fahrenheit | Convert -49 degrees Celsius to degrees Fahrenheit = | -56.2 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 83 of the AP series: -41, -110, -179 ...  | -5699 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 99 terms of the AP series: 20, -59, -138 ...  | -381249.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 1424 in Octal is:  | 0o2620 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 3563 in Roman Numerals is:  | MMMDLXIII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 286 in radians is =  | 4.99 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(exp(x)+6*x^(-3))/dx | exp(x) - 18/x^4 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 94x^2 + 86x + 97 is =  | 171.3333 | definite_integral |
| 90 | isprime | 28 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 9 is =  | 37408 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 15.65exp(i-2.68) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={2, 3, 5} ,b={2, 3, 6, 7}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {2, 3, 5, 6, 7},Intersection is {2, 3}, a-b is {5},b-a is {6, 7}, Symmetric difference is {5, 6, 7} | set_operation |
| 94 | Base Conversion | Convert E656 from base 16 to base 12. | 2A15A | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 43 and height, 85? | CSA of cylinder = 22965.04 | curved_surface_area_cylinder |
