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
| 0 | Addition | 20+9= | 29 | addition |
| 1 | Subtraction | 52-50= | 2 | subtraction |
| 2 | Multiplication | 53*1= | 53 | multiplication |
| 3 | Division | 35/79= | 0.4430379746835443 | division |
| 4 | Binary Complement 1s | 011011= | 100100 | binary_complement_1s |
| 5 | Modulo Division | 27%39= | 27 | modulo_division |
| 6 | Square Root | sqrt(16)= | 4 | square_root |
| 7 | Power Rule Differentiation | 7x^5 | 35x^4 | power_rule_differentiation |
| 8 | Square | 10^2= | 100 | square |
| 9 | LCM (Least Common Multiple) | LCM of 14 and 14 = | 14 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 17 and 7 =  | 1 | gcd |
| 11 | Basic Algebra | 6x + 5 = 5 | 0 | basic_algebra |
| 12 | Logarithm | log2(64) | 6 | log |
| 13 | Easy Division | 252/12 =  | 21 | int_division |
| 14 | Decimal to Binary | Binary of 19= | 10011 | decimal_to_binary |
| 15 | Binary to Decimal | 1000010100 | 532 | binary_to_decimal |
| 16 | Fraction Division | (10/9)/(10/8) | 8/9 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 15 * [[5, 3], [3, 2]] =  | [[75,45],[45,30]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 3 17 2 =  | (4.221036154550547e-15+68.93475175845634j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 24, 20 and 17 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (4,-10),(2,4)= | (3.0,-3.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-3x-54 | (x+6)(x-9) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 6 and 29 =  | 145 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 |  - 5y = -20, 3x + 9y = 9 | x = -9, y = 4 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-2, -4) and (21, -13) | sqrt(610) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 16 and 11 =  | 19.42 | pythagorean_theorem |
| 26 | Linear Equations | 11x + 4y = -72, 17x + -18y = -208 | x = -8, y = 4 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 88 | [2, 2, 2, 11] | prime_factors |
| 28 | Fraction Multiplication | (7/3)*(2/10) | 7/15 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 9 sides | 140.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 16 objects picked 6 at a time  | 8008 | combinations |
| 31 | Factorial | 2! =  | 2 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 3m is | 54 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 9m, 1m, 14m is | 298 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 30m and radius = 3m is | 622 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 16m is | 4096 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 4m, 12m, 11m is | 528 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 32m and radius = 17m is | 29053 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 18m and radius = 16m is | 2014 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 24m and radius = 6m is | 904 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 73 and 75 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -10/4x - 6 and y = -2/5x + 2 | (-80/21, 74/21) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 18 objects picked 5 at a time =   | 1028160 | permutation |
| 43 | Cross Product of 2 Vectors | [-19, -17, 16] X [-3, -10, 19] =  | [-163, 313, 139] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 10/8 and 4/7? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 8277 dollars, 8% rate of interest and for a time period of 8 years is =  | 5297.28 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>5</td><td>-3</td><td>6</td></tr><tr><td>6</td><td>7</td><td>-2</td></tr><tr><td>5</td><td>5</td><td>-2</td></tr></table>and<table><tr><td>-6</td><td>4</td></tr><tr><td>-5</td><td>-2</td></tr><tr><td>-5</td><td>1</td></tr></table> | <table><tr><td>-45</td><td>32</td></tr><tr><td>-61</td><td>8</td></tr><tr><td>-45</td><td>8</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 725 upto 2 decimal places is: | 8.98 | cube_root |
| 48 | Power Rule Integration | 6x^8 + 10x^3 + 2x^8 + 8x^8 + 6x^9 | (6/8)x^9 + (10/3)x^4 + (2/8)x^9 + (8/8)x^9 + (6/9)x^10 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 34 , 200, 57 = | 69 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 28x^2+105x+65=0 | [-0.78, -2.97] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 14 and 7 =  | 7 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 3 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 2^2 = | 4 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [271, 209, 205, 219, 291, 221, 226, 217, 230, 272, 276, 293, 237, 252, 283, 253, 266, 240, 234, 207, 279] with 80% confidence is | (254.68568495447266, 238.74288647409878) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 8^(1/2) _ 55^(1/6) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 19 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584] | fibonacci_series |
| 57 | Trigonometric Values | What is cos(45)? | 1/√2 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 6 sides =  | 720 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[25, 45, 11, 49, 43, 21, 18, 22, 46, 41, 48, 45, 47, 46, 22] | The Mean is 35.266666666666666 , Standard Deviation is 169.9288888888889, Variance is 13.035677538543553 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 20m is | 5026.548245743669 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 6 m =  | 904.7786842338604 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 98th Fibonacci number? | 135301852344707186688 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 88 and SP = 155 is:  | 76.13636363636364 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 0111100 | 0x3c | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (6+15j) * (-11+14j) =  | (-276-81j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [4, 8, 16, 32, 64, 128] ,Find the value of a,common ratio,10th term value, sum upto 7th term | The value of a is 4, common ratio is 2 , 10th term is 2048 , sum upto 7th term is 508.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 15 and 89 =  | (15*89)^(1/2) = 36.53765181289022 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 57 , 38 , 60 , 25 =  |  4/((1/57) + (1/38) + (1/60) + (1/25)) = 39.79057591623037 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[987.2988424731678, 717.1306649026507, 239.90848831697863, 979.8627407501484, 102.29066104606976, 458.7906478877879, 275.5546983244834, 225.6916602424589, 26.12527792643693, 366.7028959774343, 752.5264100654856] is: | 1885.7336411802055 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [204.34, 989.9, 769.23, 587.22, 313.6, 598.75, 907.67, 221.31, 7.76, 716.11, 697.58, 26.04, 416.61, 562.5, 818.67, 197.06, 492.85, 507.85, 609.86, 475.4] and [877.86, 605.89, 409.16, 650.41, 32.59, 244.04, 903.77, 499.35, 438.81, 709.82, 656.49, 745.17, 497.04, 832.24, 195.85, 37.89, 851.83, 608.87, 119.84, 17.96] is: | 0.66 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -40 and -6 =  | 34 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [-17, 12, 6] . [-2, -9, 9] =  | -20 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 10100110 = | 1011010 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[54, 47, 44], [59, 41, 7], [86, 33, 5]]) is: | Matrix([[26/56451, -1217/56451, 1475/56451], [-307/56451, 3514/56451, -2218/56451], [1579/56451, -2260/56451, 559/56451]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 23 and angle, 4. Find the area of the sector. | Area of sector = 18.46558 | sector_area |
| 76 | Mean and Median | Given the series of numbers [19, 93, 45, 37, 39, 8, 48, 44, 12, 10]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 35.5 and Arithmetic median of this series is 38.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[73, 67], [64, 58]]) =  |  -54 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 2095 dollars, 6% rate of interest and for a time period of 3 year is =  | 2495.18 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 494= | 0x1ee | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 14% of 51? | Required percentage = 7.14% | percentage |
| 81 | Celsius To Fahrenheit | Convert -22 degrees Celsius to degrees Fahrenheit = | -7.600000000000001 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 39 of the AP series: -42, -102, -162 ...  | -2322 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 49 terms of the AP series: 18, -50, -118 ...  | -79086.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 3746 in Octal is:  | 0o7242 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 2967 in Roman Numerals is:  | MMCMLXVII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 109 in radians is =  | 1.9 | degree_to_rad |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(sin(x)+9*x^3)/dx | 27*x^2 + cos(x) | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 50x^2 + 38x + 41 is =  | 76.6667 | definite_integral |
| 90 | isprime | 11 | True | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 7 is =  | 29331 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 14.42exp(i-2.55) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={2, 3, 4, 5, 6, 8, 10} ,b={4, 5, 6, 7}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {2, 3, 4, 5, 6, 7, 8, 10},Intersection is {4, 5, 6}, a-b is {8, 10, 2, 3},b-a is {7}, Symmetric difference is {2, 3, 7, 8, 10} | set_operation |
| 94 | Base Conversion | Convert 33210 from base 10 to base 11. | 22A51 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 3 and height, 21? | CSA of cylinder = 395.84 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 10 sided polygon with lengths of [11, 117, 72, 120, 46, 96, 40, 76, 15, 19]cm is:  | 612 | perimeter_of_polygons |
| 97 | Power of Powers | The 41^3^4 = 41^(3*4) = 41^12 | 22563490300366186081 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 19^2 and 19^2 = 19^(2-2) = 19^0 | 1 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 29^3 and 22^3 = (29/22)^3 = 1.3181818181818181^3 | 2.2904770848985723 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 9x^2 + 9x + 2 = 0 | simplified solution : ((-0.333, -0.667)), generalized solution : ((-9 + 3)/2*9, (-9 - 3)/2*9) | complex_quadratic |
