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
| 0 | Addition | 15+24= | 39 | addition |
| 1 | Subtraction | 25-1= | 24 | subtraction |
| 2 | Multiplication | 1*88= | 88 | multiplication |
| 3 | Division | 42/80= | 0.525 | division |
| 4 | Binary Complement 1s | 00100011= | 11011100 | binary_complement_1s |
| 5 | Modulo Division | 27%18= | 9 | modulo_division |
| 6 | Square Root | sqrt(36)= | 6 | square_root |
| 7 | Power Rule Differentiation | 1x^7 | 7x^6 | power_rule_differentiation |
| 8 | Square | 15^2= | 225 | square |
| 9 | LCM (Least Common Multiple) | LCM of 19 and 6 = | 114 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 14 and 17 =  | 1 | gcd |
| 11 | Basic Algebra | 8x + 10 = 10 | 0 | basic_algebra |
| 12 | Logarithm | log3(3) | 1 | log |
| 13 | Easy Division | 169/13 =  | 13 | int_division |
| 14 | Decimal to Binary | Binary of 55= | 110111 | decimal_to_binary |
| 15 | Binary to Decimal | 0 | 0 | binary_to_decimal |
| 16 | Fraction Division | (1/3)/(8/4) | 1/6 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 2 * [[6, 1], [9, 2]] =  | [[12,2],[18,4]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 10 12 1 =  | (5.827134701491688e-16+9.51643315533714j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 24, 11 and 22 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (-1,6),(4,13)= | (1.5,9.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-15x+54 | (x-6)(x-9) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 30 and 49 =  | 101 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -x + 3y = 23, 2x + 6y = 74 | x = 7, y = 10 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-2, -1) and (9, 21) | sqrt(605) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 1 and 2 =  | 2.24 | pythagorean_theorem |
| 26 | Linear Equations | -3x + 5y = 47, -2x + 5y = 63 | x = 16, y = 19 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 58 | [2, 29] | prime_factors |
| 28 | Fraction Multiplication | (3/5)*(5/9) | 1/3 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 6 sides | 120.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 14 objects picked 8 at a time  | 3003 | combinations |
| 31 | Factorial | 1! =  | 1 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 10m is | 600 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 7m, 20m, 12m is | 928 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 33m and radius = 6m is | 1470 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 18m is | 5832 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 3m, 20m, 20m is | 1200 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 14m and radius = 10m is | 4398 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 19m and radius = 1m is | 62 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 17m and radius = 13m is | 3008 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 81 and 74 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -7/2x - 5 and y = -10/4x + 6 | (-11, 67/2) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 17 objects picked 8 at a time =   | 980179200 | permutation |
| 43 | Cross Product of 2 Vectors | [3, -10, 2] X [8, 8, -9] =  | [74, 43, 104] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 5/6 and 10/7? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 1332 dollars, 7% rate of interest and for a time period of 8 years is =  | 745.92 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>2</td><td>-10</td><td>-8</td></tr><tr><td>-10</td><td>6</td><td>0</td></tr><tr><td>0</td><td>0</td><td>-2</td></tr><tr><td>6</td><td>-1</td><td>-2</td></tr></table>and<table><tr><td>-1</td><td>7</td><td>-3</td></tr><tr><td>-10</td><td>-8</td><td>10</td></tr><tr><td>7</td><td>7</td><td>3</td></tr></table> | <table><tr><td>42</td><td>38</td><td>-130</td></tr><tr><td>-50</td><td>-118</td><td>90</td></tr><tr><td>-14</td><td>-14</td><td>-6</td></tr><tr><td>-10</td><td>36</td><td>-34</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 845 upto 2 decimal places is: | 9.45 | cube_root |
| 48 | Power Rule Integration | 10x^7 + 7x^2 + 1x^10 + 9x^10 + 6x^1 | (10/7)x^8 + (7/2)x^3 + (1/10)x^11 + (9/10)x^11 + (6/1)x^2 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 24 , 205, 108 = | 23 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 4x^2+38x+53=0 | [-1.7, -7.8] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 3 and 5 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 6 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 13^7 = | 62748517 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [246, 234, 252, 233, 250, 229, 272, 299, 214, 287, 263, 237, 209, 279, 230, 244, 265, 284, 266, 260] with 90% confidence is | (261.450577042693, 243.849422957307) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 61^(1/3) _ 54^(1/6) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 12 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] | fibonacci_series |
| 57 | Trigonometric Values | What is tan(60)? | √3 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 10 sides =  | 1440 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[48, 15, 20, 21, 30, 17, 8, 13, 27, 7, 41, 34, 50, 18, 19] | The Mean is 24.533333333333335 , Standard Deviation is 170.91555555555558, Variance is 13.073467617872298 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 18m is | 4071.5040790523717 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 32 m =  | 137258.27743044044 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 67th Fibonacci number? | 44945570212853 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 15 and SP = 981 is:  | 6440.000000000001 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 1011 | 0xb | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (-13-6j) * (-13-17j) =  | (67+299j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [7, 49, 343, 2401, 16807, 117649] ,Find the value of a,common ratio,6th term value, sum upto 9th term | The value of a is 7, common ratio is 7 , 6th term is 117649 , sum upto 9th term is 47079207.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 67 , 39 and 61 =  | (67*39*61)^(1/3) = 54.2196131865444 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 51 and 18 =  |  2/((1/51) + (1/18)) = 26.608695652173914 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[475.73215854843386, 666.5961230551579, 318.8322922614731, 347.0393782548222, 132.48630879767597, 29.71776575489249, 241.27251126475247, 183.2591565913506, 829.9340763816024, 450.0454983692942, 227.01770730801584, 543.7951344512942, 704.1995480202837, 416.40405265214866] is: | 1706.1257272861317 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [520.47, 629.68, 925.7, 911.2, 727.7, 843.94, 808.55, 80.4, 157.49, 661.37, 877.4, 196.54, 283.16, 69.83] and [840.19, 459.69, 241.22, 334.45, 5.59, 696.72, 776.19, 223.28, 414.7, 875.6, 837.18, 68.45, 863.78, 961.51] is: | 0.72 radians | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 6 and -66 =  | 72 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [-7, -13, -11] . [0, -3, -17] =  | 226 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 10110 = | 1010 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[1, 94, 7], [25, 90, 5], [73, 43, 60]]) is: | Matrix([[-1037/27994, 5339/139970, 16/13997], [227/27994, 451/139970, -17/13997], [1099/27994, -6819/139970, 226/13997]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 21 and angle, 2. Find the area of the sector. | Area of sector = 7.69690 | sector_area |
| 76 | Mean and Median | Given the series of numbers [96, 45, 60, 15, 20, 4, 29, 36, 69, 47]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 42.1 and Arithmetic median of this series is 40.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[59, 81], [33, 79]]) =  |  1988 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 8179 dollars, 7% rate of interest and for a time period of 1 year is =  | 8751.53 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 106= | 0x6a | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 5% of 98? | Required percentage = 4.90% | percentage |
| 81 | Celsius To Fahrenheit | Convert 67 degrees Celsius to degrees Fahrenheit = | 152.60000000000002 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 56 of the AP series: -55, -142, -229 ...  | -4840 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 46 terms of the AP series: 96, 169, 242 ...  | 79971.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 7 in Octal is:  | 0o7 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 2558 in Roman Numerals is:  | MMDLVIII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 313 in radians is =  | 5.46 | degree_to_rad |
| 87 | Radians to Degrees | Angle 0 in degrees is =  | 0.0 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(sin(x)+2*x^(-3))/dx | cos(x) - 6/x^4 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 22x^2 + 32x + 88 is =  | 111.3333 | definite_integral |
| 90 | isprime | 28 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 6 is =  | 25632 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 23.85exp(i-2.15) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={1, 2, 5, 6, 7, 9} ,b={9, 3, 6, 7}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 3, 5, 6, 7, 9},Intersection is {9, 6, 7}, a-b is {1, 2, 5},b-a is {3}, Symmetric difference is {1, 2, 3, 5} | set_operation |
| 94 | Base Conversion | Convert 215 from base 16 to base 2. | 1000010101 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 3 and height, 33? | CSA of cylinder = 622.04 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 5 sided polygon with lengths of [21, 36, 107, 101, 15]cm is:  | 280 | perimeter_of_polygons |
| 97 | Power of Powers | The 47^10^9 = 47^(10*9) = 47^90 | 3081819609348702575993710664086973378213775077494296491025662508716527867059742510518129558368670228609205866092648641076825215755720847840202232380449 | power_of_powers |
| 98 | Quotient of Powers with Same Base | The Quotient of 21^2 and 21^9 = 21^(2-9) = 21^-7 | 5.552197891641574e-10 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 25^1 and 3^1 = (25/3)^1 = 8.333333333333334^1 | 8.333333333333334 | quotient_of_power_same_power |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 3x^2 + 5x + 2 = 0 | simplified solution : ((-0.667, -1.0)), generalized solution : ((-5 + 1)/2*3, (-5 - 1)/2*3) | complex_quadratic |
| 101 | Leap Year or Not | Year 2049  | is not a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 960 minutes to Hours & Minutes | 16 hours and 0 minutes | minutes_to_hours |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 6561 is =  | 19101 | decimal_to_bcd |
| 104 | Circumference | Circumference of circle with radius 11 | 69.14285714285714 | circumference |
