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
| 0 | Addition | 33+23= | 56 | addition |
| 1 | Subtraction | 14-1= | 13 | subtraction |
| 2 | Multiplication | 52*1= | 52 | multiplication |
| 3 | Division | 14/26= | 0.5384615384615384 | division |
| 4 | Binary Complement 1s | 0110111= | 1001000 | binaryComplement1s |
| 5 | Modulo Division | 23%70= | 23 | moduloDivision |
| 6 | Square Root | sqrt(121)= | 11 | squareRoot |
| 7 | Power Rule Differentiation | 3x^2 + 3x^5 + 1x^2 + 6x^4 + 6x^3 | 6x^1 + 15x^4 + 2x^1 + 24x^3 + 18x^2 | powerRuleDifferentiation |
| 8 | Square | 18^2= | 324 | square |
| 9 | LCM (Least Common Multiple) | LCM of 17 and 11 = | 187 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 15 and 12 =  | 3 | gcd |
| 11 | Basic Algebra | 2x + 3 = 10 | 7/2 | basicAlgebra |
| 12 | Logarithm | log2(32) | 5 | log |
| 13 | Easy Division | 196/14 =  | 14 | intDivision |
| 14 | Decimal to Binary | Binary of 61= | 111101 | decimalToBinary |
| 15 | Binary to Decimal | 1 | 1 | binaryToDecimal |
| 16 | Fraction Division | (2/1)/(10/5) | 1 | fractionDivision |
| 17 | Integer Multiplication with 2x2 Matrix | 16 * [[4, 1], [1, 2]] =  | [[64,16],[16,32]] | intMatrix22Multiplication |
| 18 | Area of Triangle | Area of triangle with side lengths: 15 13 11 =  | 69.62892717829278 | areaOfTriangle |
| 19 | Triangle exists check | Does triangle with sides 35, 14 and 37 exist? | Yes | doesTriangleExist |
| 20 | Midpoint of the two point | (15,5),(9,10)= | (12.0,7.5) | midPointOfTwoPoint |
| 21 | Factoring Quadratic | x^2-12x+35 | (x-7)(x-5) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 37 and 54 =  | 89 | thirdAngleOfTriangle |
| 23 | Solve a System of Equations in R^2 | -4x - 8y = 60, -9x + 10y = 51 | x = -9, y = -3 | systemOfEquations |
| 24 | Distance between 2 points | Find the distance between (16, 7) and (19, 14) | sqrt(58) | distance2Point |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 18 and 8 =  | 19.70 | pythagoreanTheorem |
| 26 | Linear Equations | -8x + 15y = -109
6x + -14y = 90 | x = 8, y = -3 | linearEquations |
| 27 | Prime Factorisation | Find prime factors of 130 | [2, 5, 13] | primeFactors |
| 28 | Fraction Multiplication | (8/9)*(3/2) | 4/3 | fractionMultiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 8 sides | 135.0 | angleRegularPolygon |
| 30 | Combinations of Objects | Number of combinations from 11 objects picked 9 at a time  | 55 | combinations |
| 31 | Factorial | 2! =  | 2 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 17m is | 1734 m^2 | surfaceAreaCubeGen |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 8m, 4m, 17m is | 472 m^2 | surfaceAreaCuboidGen |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 32m and radius = 18m is | 5654 m^2 | surfaceAreaCylinderGen |
| 35 | Volum of Cube | Volume of cube with side = 11m is | 1331 m^3 | volumeCubeGen |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 14m, 19m, 1m is | 266 m^3 | volumeCuboidGen |
| 37 | Volume of cylinder | Volume of cylinder with height = 16m and radius = 18m is | 16286 m^3 | volumeCylinderGen |
| 38 | Surface Area of cone | Surface area of cone with height = 48m and radius = 20m is | 4523 m^2 | surfaceAreaConeGen |
| 39 | Volume of cone | Volume of cone with height = 29m and radius = 6m is | 1093 m^3 | volumeConeGen |
| 40 | Common Factors | Common Factors of 59 and 57 =  | [1] | commonFactors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -1/4x - 2 and y = 4/5x + 3 | (-100/21, -17/21) | intersectionOfTwoLines |
| 42 | Permutations | Number of Permutations from 13 objects picked 8 at a time =   | 51891840 | permutations |
| 43 | Cross Product of 2 Vectors | [4, -11, 9] X [-8, -19, -5] =  | [226, -52, -164] | vectorCross |
| 44 | Compare Fractions | Which symbol represents the comparison between 3/7 and 2/4? | < | compareFractions |
| 45 | Simple Interest | Simple interest for a principle amount of 2398 dollars, 9% rate of interest and for a time period of 5 years is =  | 1079.1 | simpleInterest |
| 46 | Multiplication of two matrices | Multiply <table><tr><td>-50</td><td>36</td><td>7</td><td>-26</td><td>-2</td><td>63</td></tr><tr><td>88</td><td>-37</td><td>60</td><td>-19</td><td>61</td><td>-56</td></tr><tr><td>48</td><td>-5</td><td>69</td><td>-87</td><td>-64</td><td>-92</td></tr><tr><td>-84</td><td>-50</td><td>-79</td><td>-19</td><td>86</td><td>-13</td></tr><tr><td>0</td><td>28</td><td>12</td><td>-14</td><td>73</td><td>-49</td></tr><tr><td>94</td><td>-90</td><td>2</td><td>26</td><td>-38</td><td>19</td></tr><tr><td>2</td><td>-11</td><td>79</td><td>-77</td><td>98</td><td>-77</td></tr><tr><td>-87</td><td>70</td><td>72</td><td>-32</td><td>64</td><td>-99</td></tr></table> and <table><tr><td>34</td><td>32</td><td>-6</td><td>-32</td><td>46</td><td>-23</td><td>78</td><td>-81</td><td>-18</td></tr><tr><td>-17</td><td>24</td><td>49</td><td>-62</td><td>-50</td><td>77</td><td>38</td><td>-98</td><td>-64</td></tr><tr><td>-23</td><td>-78</td><td>43</td><td> 5</td><td>-83</td><td>-5</td><td> 4</td><td>-92</td><td>-16</td></tr><tr><td> 46</td><td>-47</td><td>-92</td><td>52</td><td>-25</td><td>-37</td><td>44</td><td>51</td><td>-7</td></tr><tr><td> 20</td><td>26</td><td>70</td><td>37</td><td>96</td><td>-73</td><td>49</td><td>84</td><td>42</td></tr><tr><td>-72</td><td>-15</td><td>-80</td><td>-24</td><td>58</td><td>-47</td><td>-41</td><td>45</td><td>-69</td></tr></table>|  <table><tr><td>-8245</td><td>-1057</td><td>-423</td><td>-3535</td><td>-569</td><td>2034</td><td>-6329</td><td>1219</td><td>-5765</td></tr><tr><td>6619</td><td> 567</td><td>10737</td><td>2391</td><td>4001</td><td>-6291</td><td>10147</td><td>-7387</td><td>6383</td></tr><tr><td>1472</td><td>-161</td><td>13318</td><td>-5565<td>-12574</td><td>10381</td><td> 638<td>-23699</td><td>2621</td></tr><tr><td>1593</td><td>5598</td><td>3465</td><td>7899</td><td>13170</td><td>-6487</td><td>-4857</td><td>24642</td><td>10618</td></tr><tr><td>3592</td><td>3027</td><td>12206</td><td>1473</td><td>2120</td><td>-412</td><td>6082</td><td>-635</td><td>4561</td></tr><tr><td>3748</td><td>-1803<td>-11460</td><td>2072</td><td>5462</td><td>-8183</td><td>2423</td><td>11</td><td> 947</td></tr><tr><td>2400</td><td> 960</td><td>22950</td><td>2483</td><td> 952</td><td>-1974</td><td>4625</td><td>-5512</td><td>9372</td></tr><tr><td>1132</td><td>-2067</td><td>22392</td><td>1884<td>-12276</td><td>8196</td><td>1949</td><td>-7148</td><td>5677</td></tr></table>   | matrixMultiplication |
 [ 10584,  13902,  11916,  -7446,   4430,    554]
 [ -1800,   6587,  14343,   6224,   4525,   4853]
 [-12452, -10675,  -8693,    427,   2955,  17691]] | matrixMultiplication |
| 47 | Cube Root | cuberoot of 221 upto 2 decimal places is: | 6.05 | CubeRoot |
| 48 | Power Rule Integration | 4x^5 + 2x^5 + 9x^8 + 9x^5 | (4/5)x^6 + (2/5)x^6 + (9/8)x^9 + (9/5)x^6 + c | powerRuleIntegration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 27 , 155, 116 = | 62 | fourthAngleOfQuadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 53x^2+200x+78=0 | [-0.44, -3.33] | quadraticEquationSolve |
| 51 | HCF (Highest Common Factor) | HCF of 7 and 4 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 11 = | 2/36 | diceSumProbability |
| 53 | Exponentiation | 9^10 = | 3486784401 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [266, 201, 278, 209, 229, 275, 216, 234, 219, 276, 282, 281, 208, 247, 265, 273, 286, 202, 231, 207, 251, 203, 259, 288, 291, 260, 210, 263, 222] with 99% confidence is | (260.5668079141175, 231.29526105139982) | confidenceInterval |
| 55 | Comparing surds | Fill in the blanks 15^(1/9) _ 55^(1/1) | < | surdsComparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 10 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] | fibonacciSeries |
| 57 | Trigonometric Values | What is tan(30)? | 1/√3 | basicTrigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 3 sides =  | 180 | sumOfAnglesOfPolygon |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[36, 13, 31, 23, 38, 34, 24, 20, 41, 14, 19, 31, 11, 49, 49] | The Mean is 28.866666666666667 , Standard Deviation is 143.5822222222222, Variance is 11.982579948501167 | dataSummary |
| 59 | Surface Area of Sphere | Surface area of Sphere with radius = 11m is | 1520.5308443374597 m^2 | surfaceAreaSphereGen |
| 60 | Volume of Sphere | Volume of sphere with radius 73 m =  | 1629510.5990953872 m^3 | volumeSphere |
| 61 | nth Fibonacci number | What is the 68th Fibonacci number? | 72723460248141 | nthFibonacciNumberGen |
| 62 | Profit or Loss Percent | Profit percent when CP = 825 and SP = 972 is:  | 17.81818181818182 | profitLossPercent |
| 63 | Binary to Hexidecimal | 100000 | 0x20 | binaryToHex |
| 64 | Multiplication of 2 complex numbers | (3+14j) * (-3+16j) =  | (-233+6j) | complexNumMultiply |
| 65 | Geometric Progression | For the given GP [4, 16, 64, 256, 1024, 4096] ,Find the value of a,common ratio,8th term value, sum upto 7th term | The value of a is 4, common ratio is 4 , 8th term is 65536 , sum upto 7th term is 21844.0 | geometricprogression |
| 66 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 81 , 35 and 99 =  | (81*35*99)^(1/3) = 65.47307713912309 | geometricMean |
| 67 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 99 and 25 =  |  2/((1/99) + (1/25)) = 39.91935483870967 | harmonicMean |
