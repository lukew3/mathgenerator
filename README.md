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
| 0 | Addition | 29+29= | 58 | addition |
| 1 | Subtraction | 10-8= | 2 | subtraction |
| 2 | Multiplication | 96*0= | 0 | multiplication |
| 3 | Division | 25/95= | 0.2631578947368421 | division |
| 4 | Binary Complement 1s | 100101100= | 011010011 | binary_complement_1s |
| 5 | Modulo Division | 74%50= | 24 | modulo_division |
| 6 | Square Root | sqrt(49)= | 7 | square_root |
| 7 | Power Rule Differentiation | 10x^7 + 7x^5 + 5x^8 | 70x^6 + 35x^4 + 40x^7 | power_rule_differentiation |
| 8 | Square | 9^2= | 81 | square |
| 9 | LCM (Least Common Multiple) | LCM of 19 and 7 = | 133 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 1 and 7 =  | 1 | gcd |
| 11 | Basic Algebra | 3x + 2 = 8 | 6 | basic_algebra |
| 12 | Logarithm | log2(128) | 7 | log |
| 13 | Easy Division | 228/12 =  | 19 | int_division |
| 14 | Decimal to Binary | Binary of 37= | 100101 | decimal_to_binary |
| 15 | Binary to Decimal | 10100001 | 161 | binary_to_decimal |
| 16 | Fraction Division | (8/2)/(8/2) | 1 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 6 * [[3, 7], [10, 6]] =  | [[18,42],[60,36]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 2 1 19 =  | (5.449334243437888e-15+88.99438184514796j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 48, 16 and 30 exist? | No | valid_triangle |
| 20 | Midpoint of the two point | (2,-5),(12,-7)= | (7.0,-6.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-18x+81 | (x-9)(x-9) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 45 and 1 =  | 134 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -7x - 10y = -133, 7x - 2y = 49 | x = 9, y = 7 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-10, 7) and (16, 6) | sqrt(677) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 10 and 8 =  | 12.81 | pythagorean_theorem |
| 26 | Linear Equations | 18x + -2y = -174, -13x + 6y = 194 | x = -8, y = 15 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 16 | [2, 2, 2, 2] | prime_factors |
| 28 | Fraction Multiplication | (6/8)*(2/5) | 3/10 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 17 sides | 158.82 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 17 objects picked 3 at a time  | 680 | combinations |
| 31 | Factorial | 1! =  | 1 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 17m is | 1734 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 12m, 11m, 1m is | 310 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 38m and radius = 16m is | 5428 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 11m is | 1331 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 17m, 19m, 8m is | 2584 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 35m and radius = 19m is | 39694 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 8m and radius = 19m is | 2364 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 43m and radius = 13m is | 7609 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 21 and 65 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 5/4x - 1 and y = 0/4x - 5 | (-16/5, -5) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 10 objects picked 5 at a time =   | 30240 | permutation |
| 43 | Cross Product of 2 Vectors | [12, -16, 4] X [-14, 10, -9] =  | [104, 52, -104] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 7/10 and 7/5? | < | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 6138 dollars, 9% rate of interest and for a time period of 8 years is =  | 4419.36 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-8</td><td>-8</td></tr><tr><td>-2</td><td>-9</td></tr></table>and<table><tr><td>-10</td><td>-8</td></tr><tr><td>9</td><td>-9</td></tr></table> | <table><tr><td>8</td><td>136</td></tr><tr><td>-61</td><td>97</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 633 upto 2 decimal places is: | 8.59 | cube_root |
| 48 | Power Rule Integration | 2x^5 + 3x^3 + 4x^7 + 9x^1 + 6x^9 | (2/5)x^6 + (3/3)x^4 + (4/7)x^8 + (9/1)x^2 + (6/9)x^10 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 79 , 44, 37 = | 200 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 79x^2+182x+98=0 | [-0.86, -1.45] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 1 and 20 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 1 dice are rolled at the same time, the probability of getting a sum of 2 = | 1/6 | dice_sum_probability |
| 53 | Exponentiation | 6^9 = | 10077696 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [260, 249, 281, 261, 236, 237, 275, 229, 256, 242, 277, 240, 278, 293, 271, 255, 216, 292, 200, 298, 282, 223] with 99% confidence is | (271.2437114485249, 242.48356127874783) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 71^(1/5) _ 31^(1/8) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 19 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584] | fibonacci_series |
| 57 | Trigonometric Values | What is cos(45)? | 1/√2 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 10 sides =  | 1440 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[13, 22, 36, 17, 9, 39, 50, 14, 32, 40, 37, 48, 47, 28, 47] | The Mean is 31.933333333333334 , Standard Deviation is 182.59555555555553, Variance is 13.51279229306643 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 18m is | 4071.5040790523717 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 61 m =  | 950775.7894726198 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 85th Fibonacci number? | 259695496911123328 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 353 and SP = 752 is:  | 113.03116147308782 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 111101011 | 0x1eb | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (-19-9j) * (-17-2j) =  | (305+191j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [7, 77, 847, 9317, 102487, 1127357] ,Find the value of a,common ratio,6th term value, sum upto 7th term | The value of a is 7, common ratio is 11 , 6th term is 1127357 , sum upto 7th term is 13641019.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 32 , 5 and 18 =  | (32*5*18)^(1/3) = 14.227573217960249 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 3 numbers 48 , 85 and 79 =  |  3/((1/48) + (1/85) + (1/79)) = 66.28916158223076 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[743.1109024649227, 951.2861991520674, 821.2679183199273, 831.5922742303677, 972.3005129207023, 775.1712986008336, 869.5254070360901, 34.05779748860371, 495.5299489221041, 516.2458991121815, 620.0871728488738, 12.438787805084894, 967.8138977993306, 627.6791615554401, 129.81896901435886, 566.4442009627315, 521.5300881726977, 741.5947979192599] is: | 2917.827115551868 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [341.1766244080324, 386.90517658729595, 306.3074773969527, 542.1138441520038, 149.80203485453225, 85.6719016065689, 875.0827941729921, 292.0422074695527, 312.8929536855103, 408.95388654647445, 119.81564007869672, 177.5529661884936, 360.30983184002406, 111.71502530193955, 29.528755078141455, 478.2846569662712, 855.8978282979257] and [230.45166329807688, 922.2895458023412, 219.89492715268733, 375.8793126730714, 731.2614314505195, 277.5554009411926, 329.1490487358273, 477.7600322879586, 168.93745868538923, 423.6897582803929, 724.5555882496458, 519.6421532094823, 158.0479000313908, 679.3674240323584, 496.6795371750926, 853.4421897526636, 715.2567898992207] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 53 and -70 =  | 123 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [-8, -4, -10] . [-9, -6, -9] =  | 186 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of  = |  | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[43, 95, 41], [46, 80, 67], [57, 75, 71]]) is: | Matrix([[131/7038, -367/3519, 617/7038], [553/35190, 358/17595, -199/7038], [-37/1173, 73/1173, -31/1173]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 40 and angle, 199. Find the area of the sector. | Area of sector = 2778.56417 | sector_area |
| 76 | Mean and Median | Given the series of numbers [44, 64, 22, 37, 63, 56, 27, 62, 98, 72]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 54.5 and Arithmetic median of this series is 59.0 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[73, 52], [55, 80]]) =  |  2980 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound Interest for a principle amount of 8506 dollars, 8% rate of interest and for a time period of 10 compounded monthly is =  | 8506.0 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 293= | 0x125 | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 57% of 4? | Required percentage = 2.28% | percentage |
| 81 | Celsius To Fahrenheit | Convert 57 degrees Celsius to degrees Fahrenheit = | 134.60000000000002 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 89 of the AP series: 20, 115, 210 ...  | 8380 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 98 terms of the AP series: -58, -106, -154 ...  | -233828.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 1716 in Octal is:  | 0o3264 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 587 in Roman Numerals is:  | DLXXXVII | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 245 in radians is =  | 4.28 | degree_to_rad |
| 87 | Radians to Degrees | Angle 0 in degrees is =  | 0.0 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(exp(x)+5*x^(-2))/dx | exp(x) - 10/x^3 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 39x^2 + 72x + 74 is =  | 123.0 | definite_integral |
