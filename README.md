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
| 0 | Addition | 48+45= | 93 | addition |
| 1 | Subtraction | 71-33= | 38 | subtraction |
| 2 | Multiplication | 87*0= | 0 | multiplication |
| 3 | Division | 14/26= | 0.5384615384615384 | division |
| 4 | Binary Complement 1s | 010= | 101 | binary_complement_1s |
| 5 | Modulo Division | 87%32= | 23 | modulo_division |
| 6 | Square Root | sqrt(25)= | 5 | square_root |
| 7 | Power Rule Differentiation | 3x^8 + 10x^10 + 10x^10 + 9x^4 | 24x^7 + 100x^9 + 100x^9 + 36x^3 | power_rule_differentiation |
| 8 | Square | 7^2= | 49 | square |
| 9 | LCM (Least Common Multiple) | LCM of 19 and 1 = | 19 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 7 and 14 =  | 7 | gcd |
| 11 | Basic Algebra | 1x + 6 = 6 | 0 | basic_algebra |
| 12 | Logarithm | log3(6561) | 8 | log |
| 13 | Easy Division | 18/18 =  | 1 | int_division |
| 14 | Decimal to Binary | Binary of 51= | 110011 | decimal_to_binary |
| 15 | Binary to Decimal | 110 | 6 | binary_to_decimal |
| 16 | Fraction Division | (6/2)/(3/4) | 4 | divide_fractions |
| 17 | Integer Multiplication with 2x2 Matrix | 6 * [[9, 7], [7, 0]] =  | [[54,42],[42,0]] | multiply_int_to_22_matrix |
| 18 | Area of Triangle | Area of triangle with side lengths: 1 11 12 =  | 0.0 | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 12, 13 and 20 exist? | Yes | valid_triangle |
| 20 | Midpoint of the two point | (-14,-9),(-5,0)= | (-9.5,-4.5) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2-7x-30 | (x-10)(x+3) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 46 and 1 =  | 133 | third_angle_of_triangle |
| 23 | Solve a System of Equations in R^2 | -3x + 9y = 45, -9x + 6y = 9 | x = 3, y = 6 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-12, 9) and (-17, -14) | sqrt(554) | distance_two_points |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 6 and 14 =  | 15.23 | pythagorean_theorem |
| 26 | Linear Equations | 13x + 14y = 113, 15x + 13y = 102 | x = -1, y = 9 | linear_equations |
| 27 | Prime Factorisation | Find prime factors of 18 | [2, 3, 3] | prime_factors |
| 28 | Fraction Multiplication | (3/7)*(9/10) | 27/70 | fraction_multiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 20 sides | 162.0 | angle_regular_polygon |
| 30 | Combinations of Objects | Number of combinations from 10 objects picked 9 at a time  | 10 | combinations |
| 31 | Factorial | 3! =  | 6 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 10m is | 600 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 14m, 2m, 14m is | 504 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 25m and radius = 7m is | 1407 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 4m is | 64 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 5m, 18m, 8m is | 720 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 34m and radius = 8m is | 6836 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 2m and radius = 20m is | 2519 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 44m and radius = 12m is | 6635 m^3 | volume_cone |
| 40 | Common Factors | Common Factors of 17 and 86 =  | [1] | common_factors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -5/4x - 2 and y = -9x - 6 | (-16/31, -42/31) | intersection_of_two_lines |
| 42 | Permutations | Number of Permutations from 12 objects picked 4 at a time =   | 11880 | permutation |
| 43 | Cross Product of 2 Vectors | [-13, -1, -10] X [0, 18, -12] =  | [192, -156, -234] | vector_cross |
| 44 | Compare Fractions | Which symbol represents the comparison between 5/2 and 10/8? | > | compare_fractions |
| 45 | Simple Interest | Simple interest for a principle amount of 5498 dollars, 5% rate of interest and for a time period of 3 years is =  | 824.7 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-6</td><td>3</td><td>-5</td></tr><tr><td>-9</td><td>6</td><td>-5</td></tr><tr><td>-10</td><td>-10</td><td>9</td></tr><tr><td>4</td><td>-4</td><td>-4</td></tr></table>and<table><tr><td>0</td><td>-4</td></tr><tr><td>-4</td><td>-1</td></tr><tr><td>-2</td><td>6</td></tr></table> | <table><tr><td>-2</td><td>-9</td></tr><tr><td>-14</td><td>0</td></tr><tr><td>22</td><td>104</td></tr><tr><td>24</td><td>-36</td></tr></table> | matrix_multiplication |
| 47 | Cube Root | cuberoot of 968 upto 2 decimal places is: | 9.89 | cube_root |
| 48 | Power Rule Integration | 7x^9 + 7x^5 + 10x^7 + 4x^4 | (7/9)x^10 + (7/5)x^6 + (10/7)x^8 + (4/4)x^5 + c | power_rule_integration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 173 , 31, 114 = | 42 | fourth_angle_of_quadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 68x^2+182x+87=0 | [-0.62, -2.05] | quadratic_equation |
| 51 | HCF (Highest Common Factor) | HCF of 7 and 14 =  | 7 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 10 = | 27/216 | dice_sum_probability |
| 53 | Exponentiation | 11^4 = | 14641 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [235, 253, 263, 269, 298, 284, 208, 206, 259, 234, 246, 262, 268, 224, 280, 242, 287, 230, 239, 258, 225] with 90% confidence is | (259.8648254059283, 242.03993649883367) | confidence_interval |
| 55 | Comparing surds | Fill in the blanks 73^(1/1) _ 48^(1/3) | > | surds_comparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 8 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13] | fibonacci_series |
| 57 | Trigonometric Values | What is tan(0)? | 0 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 6 sides =  | 720 | sum_of_polygon_angles |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[11, 16, 26, 47, 12, 32, 21, 44, 35, 49, 25, 19, 35, 38, 46] | The Mean is 30.4 , Standard Deviation is 156.10666666666668, Variance is 12.494265351218802 | data_summary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 14m is | 2463.0086404143976 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 99 m =  | 4064378.94691403 m^3 | volume_sphere |
| 62 | nth Fibonacci number | What is the 68th Fibonacci number? | 72723460248141 | nth_fibonacci_number |
| 63 | Profit or Loss Percent | Profit percent when CP = 114 and SP = 746 is:  | 554.3859649122808 | profit_loss_percent |
| 64 | Binary to Hexidecimal | 001111 | 0xf | binary_to_hex |
| 65 | Multiplication of 2 complex numbers | (7+4j) * (16-11j) =  | (156-13j) | multiply_complex_numbers |
| 66 | Geometric Progression | For the given GP [4, 36, 324, 2916, 26244, 236196] ,Find the value of a,common ratio,11th term value, sum upto 9th term | The value of a is 4, common ratio is 9 , 11th term is 13947137604 , sum upto 9th term is 193710244.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 4 numbers 56 , 8 , 51 , 33 =  | (56*8*51*33)^(1/4) = 29.467312750334496 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 97 and 28 =  |  2/((1/97) + (1/28)) = 43.456 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[473.48308338171165, 718.7895179222332, 313.2067061144618, 613.6012136748973, 19.16574105047797] is: | 1102.640837776255 | euclidian_norm |
| 70 | Angle between 2 vectors | angle between the vectors [127.16446951950677, 696.3193812597515, 791.5623049234473, 264.1941927989295] and [932.5653922587298, 157.61937181749875, 728.0808842217069, 965.6177311470876] is: | NaN | angle_btw_vectors |
| 71 | Absolute difference between two numbers | Absolute difference between numbers 69 and -54 =  | 123 | absolute_difference |
| 72 | Dot Product of 2 Vectors | [11, -4, 17] . [11, -11, 14] =  | 403 | vector_dot |
| 73 | Binary 2's Complement | 2's complement of 111111010 = | 110 | binary_2s_complement |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[31, 66, 59], [43, 17, 28], [51, 5, 95]]) is: | Matrix([[-295/33621, 1195/33621, -169/33621], [2657/168105, 64/168105, -1669/168105], [652/168105, -3211/168105, 2311/168105]]) | invert_matrix |
| 75 | Area of a Sector | Given radius, 12 and angle, 138. Find the area of the sector. | Area of sector = 173.41591 | sector_area |
| 76 | Mean and Median | Given the series of numbers [39, 22, 54, 49, 93, 66, 33, 71, 1, 75]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 50.3 and Arithmetic median of this series is 51.5 | mean_median |
| 77 | Determinant to 2x2 Matrix | Det([[15, 29], [10, 80]]) =  |  910 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 8382 dollars, 3% rate of interest and for a time period of 2 year is =  | 8892.46 | compound_interest |
| 79 | Decimal to Hexadecimal | Binary of 814= | 0x32e | decimal_to_hexadeci |
| 80 | Percentage of a number | What is 84% of 67? | Required percentage = 56.28% | percentage |
| 81 | Celsius To Fahrenheit | Convert 62 degrees Celsius to degrees Fahrenheit = | 143.60000000000002 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 62 of the AP series: -34, -70, -106 ...  | -2230 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 81 terms of the AP series: 8, 80, 152 ...  | 233928.0 | arithmetic_progression_sum |
| 84 | Converts decimal to octal | The decimal number 2544 in Octal is:  | 0o4760 | decimal_to_octal |
| 85 | Converts decimal to Roman Numerals | The number 2921 in Roman Numerals is:  | MMCMXXI | decimal_to_roman_numerals |
| 86 | Degrees to Radians | Angle 99 in radians is =  | 1.73 | degree_to_rad |
| 87 | Radians to Degrees | Angle 2 in degrees is =  | 114.59 | radian_to_deg |
| 88 | Differentiation | differentiate w.r.t x : d(cos(x)+6*x^4)/dx | 24*x^3 - sin(x) | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 76x^2 + 60x + 37 is =  | 92.3333 | definite_integral |
| 90 | isprime | 56 | False | is_prime |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 8 is =  | 35153 | bcd_to_decimal |
| 92 | Complex To Polar Form | rexp(itheta) =  | 18.11exp(i1.46) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={1, 10, 9} ,b={8, 1, 2}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 8, 9, 10},Intersection is {1}, a-b is {9, 10},b-a is {8, 2}, Symmetric difference is {8, 9, 2, 10} | set_operation |
| 94 | Base Conversion | Convert 26897 from base 10 to base 9. | 40805 | base_conversion |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 38 and height, 88? | CSA of cylinder = 21010.97 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 9 sided polygon with lengths of [113, 56, 99, 80, 103, 80, 70, 88, 82]cm is:  | 771 | perimeter_of_polygons |
