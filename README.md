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
| 0 | Addition | 42+2= | 44 | addition |
| 1 | Subtraction | 32-26= | 6 | subtraction |
| 2 | Multiplication | 77*1= | 77 | multiplication |
| 3 | Division | 66/9= | 7.333333333333333 | division |
| 4 | Binary Complement 1s | 1010000 | 0101111 | binaryComplement1s |
| 5 | Modulo Division | 61%35= | 26 | moduloDivision |
| 6 | Square Root | sqrt(1)= | 1 | squareRoot |
| 7 | Power Rule Differentiation | 5x^5 | 25x^4 | powerRuleDifferentiation |
| 8 | Square | 20^2= | 400 | square |
| 9 | LCM (Least Common Multiple) | LCM of 19 and 5 =  | 95 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 10 and 11 =  | 1 | gcd |
| 11 | Basic Algebra | 3x + 7 = 8 | 1/3 | basicAlgebra |
| 12 | Logarithm | log2(128) | 7 | log |
| 13 | Easy Division | 306/18 =  | 17 | intDivision |
| 14 | Decimal to Binary | Binary of 28= | 11100 | decimalToBinary |
| 15 | Binary to Decimal | 10001101 | 141 | binaryToDecimal |
| 16 | Fraction Division | (4/1)/(6/3) | 2 | fractionDivision |
| 17 | Integer Multiplication with 2x2 Matrix | 5 * [[10, 3], [0, 1]] =  | [[50,15],[0,5]] | intMatrix22Multiplication |
| 18 | Area of Triangle | Area of triangle with side lengths: 13 2 14 =  | 11.659223816361019 | areaOfTriangle |
| 19 | Triangle exists check | Does triangle with sides 3, 4 and 25 exist? | No | doesTriangleExist |
| 20 | Midpoint of the two point | (4,-11),(17,-5)= | (10.5,-8.0) | midPointOfTwoPoint |
| 21 | Factoring Quadratic | x^2-12x+35 | (x-7)(x-5) | factoring |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 20 and 62 =  | 98 | thirdAngleOfTriangle |
| 23 | Solve a System of Equations in R^2 | 5x - 7y = -84, 4x + 5y = 7 | x = -7, y = 7 | systemOfEquations |
| 24 | Distance between 2 points | Find the distance between (5, -18) and (1, 19) | sqrt(1385) | distance2Point |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 15 and 5 =  | 15.81 | pythagoreanTheorem |
| 26 | Linear Equations | -6x + -17y = -220
-13x + -19y = -120 | x = -20, y = 20 | linearEquations |
| 27 | Prime Factorisation | Find prime factors of 62 | [2, 31] | primeFactors |
| 28 | Fraction Multiplication | (8/4)*(1/2) | 1 | fractionMultiplication |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 19 sides | 161.05 | angleRegularPolygon |
| 30 | Combinations of Objects | Number of combinations from 12 objects picked 1 at a time  | 12 | combinations |
| 31 | Factorial | 0! =  | 1 | factorial |
| 32 | Surface Area of Cube | Surface area of cube with side = 8m is | 384 m^2 | surfaceAreaCubeGen |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 18m, 17m, 1m is | 682 m^2 | surfaceAreaCuboidGen |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 31m and radius = 1m is | 201 m^2 | surfaceAreaCylinderGen |
| 35 | Volum of Cube | Volume of cube with side = 9m is | 729 m^3 | volumeCubeGen |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 20m, 1m, 10m is | 200 m^3 | volumeCuboidGen |
| 37 | Volume of cylinder | Volume of cylinder with height = 7m and radius = 7m is | 1077 m^3 | volumeCylinderGen |
| 38 | Surface Area of cone | Surface area of cone with height = 47m and radius = 13m is | 2522 m^2 | surfaceAreaConeGen |
| 39 | Volume of cone | Volume of cone with height = 4m and radius = 4m is | 67 m^3 | volumeConeGen |
| 40 | Common Factors | Common Factors of 20 and 90 =  | [1, 2, 5, 10] | commonFactors |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = -3/6x + 1 and y = 0/2x + 6 | (-10, 6) | intersectionOfTwoLines |
| 42 | Permutations | Number of Permutations from 11 objects picked 2 at a time =   | 110 | permutations |
| 43 | Cross Product of 2 Vectors | [-19, -3, 2] X [-15, -12, 7] =  | [3, 103, 183] | vectorCross |
| 44 | Compare Fractions | Which symbol represents the comparison between 8/6 and 3/1? | < | compareFractions |
| 45 | Simple Interest | Simple interest for a principle amount of 9862 dollars, 4% rate of interest and for a time period of 1 years is =  | 394.48 | simpleInterest |
| 46 | Multiplication of two matrices | Multiply <table><tr><td>-50</td><td>36</td><td>7</td><td>-26</td><td>-2</td><td>63</td></tr><tr><td>88</td><td>-37</td><td>60</td><td>-19</td><td>61</td><td>-56</td></tr><tr><td>48</td><td>-5</td><td>69</td><td>-87</td><td>-64</td><td>-92</td></tr><tr><td>-84</td><td>-50</td><td>-79</td><td>-19</td><td>86</td><td>-13</td></tr><tr><td>0</td><td>28</td><td>12</td><td>-14</td><td>73</td><td>-49</td></tr><tr><td>94</td><td>-90</td><td>2</td><td>26</td><td>-38</td><td>19</td></tr><tr><td>2</td><td>-11</td><td>79</td><td>-77</td><td>98</td><td>-77</td></tr><tr><td>-87</td><td>70</td><td>72</td><td>-32</td><td>64</td><td>-99</td></tr></table> and <table><tr><td>34</td><td>32</td><td>-6</td><td>-32</td><td>46</td><td>-23</td><td>78</td><td>-81</td><td>-18</td></tr><tr><td>-17</td><td>24</td><td>49</td><td>-62</td><td>-50</td><td>77</td><td>38</td><td>-98</td><td>-64</td></tr><tr><td>-23</td><td>-78</td><td>43</td><td> 5</td><td>-83</td><td>-5</td><td> 4</td><td>-92</td><td>-16</td></tr><tr><td> 46</td><td>-47</td><td>-92</td><td>52</td><td>-25</td><td>-37</td><td>44</td><td>51</td><td>-7</td></tr><tr><td> 20</td><td>26</td><td>70</td><td>37</td><td>96</td><td>-73</td><td>49</td><td>84</td><td>42</td></tr><tr><td>-72</td><td>-15</td><td>-80</td><td>-24</td><td>58</td><td>-47</td><td>-41</td><td>45</td><td>-69</td></tr></table>|  <table><tr><td>-8245</td><td>-1057</td><td>-423</td><td>-3535</td><td>-569</td><td>2034</td><td>-6329</td><td>1219</td><td>-5765</td></tr><tr><td>6619</td><td> 567</td><td>10737</td><td>2391</td><td>4001</td><td>-6291</td><td>10147</td><td>-7387</td><td>6383</td></tr><tr><td>1472</td><td>-161</td><td>13318</td><td>-5565<td>-12574</td><td>10381</td><td> 638<td>-23699</td><td>2621</td></tr><tr><td>1593</td><td>5598</td><td>3465</td><td>7899</td><td>13170</td><td>-6487</td><td>-4857</td><td>24642</td><td>10618</td></tr><tr><td>3592</td><td>3027</td><td>12206</td><td>1473</td><td>2120</td><td>-412</td><td>6082</td><td>-635</td><td>4561</td></tr><tr><td>3748</td><td>-1803<td>-11460</td><td>2072</td><td>5462</td><td>-8183</td><td>2423</td><td>11</td><td> 947</td></tr><tr><td>2400</td><td> 960</td><td>22950</td><td>2483</td><td> 952</td><td>-1974</td><td>4625</td><td>-5512</td><td>9372</td></tr><tr><td>1132</td><td>-2067</td><td>22392</td><td>1884<td>-12276</td><td>8196</td><td>1949</td><td>-7148</td><td>5677</td></tr></table>   | matrixMultiplication |
| 47 | Cube Root | cuberoot of 771 upto 2 decimal places is: | 9.17 | CubeRoot |
| 48 | Power Rule Integration | 1x^3 + 8x^8 + 10x^10 | (1/3)x^4 + (8/8)x^9 + (10/10)x^11 + c | powerRuleIntegration |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 52 , 84, 154 = | 70 | fourthAngleOfQuadrilateral |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 51x^2+152x+80=0 | [-0.68, -2.3] | quadraticEquationSolve |
| 51 | HCF (Highest Common Factor) | HCF of 11 and 7 =  | 1 | hcf |
| 52 | Probability of a certain sum appearing on faces of dice | If 2 dice are rolled at the same time, the probability of getting a sum of 11 = | 2/36 | diceSumProbability |
| 53 | Exponentiation | 9^9 = | 387420489 | exponentiation |
| 54 | Confidence interval For sample S | The confidence interval for sample [291, 254, 274, 207, 253, 289, 268, 280, 225, 240, 278, 270, 247, 252, 211, 212, 295, 241, 290, 206, 222, 263, 264, 228, 229, 256, 209, 292] with 99% confidence is | (265.560249263099, 237.72546502261523) | confidenceInterval |
| 55 | Comparing surds | Fill in the blanks 16^(1/7) _ 67^(1/6) | < | surdsComparison |
| 56 | Fibonacci Series | The Fibonacci Series of the first 11 numbers is ? | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55] | fibonacciSeries |
| 57 | Trigonometric Values | What is cos(60)? | 1/2 | basicTrigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 5 sides =  | 540 | sumOfAnglesOfPolygon |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[38, 29, 43, 25, 7, 10, 13, 14, 43, 44, 30, 42, 48, 48, 42] | The Mean is 31.733333333333334 , Standard Deviation is 199.26222222222222, Variance is 14.116027140177303 | dataSummary |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 12m is | 1809.5573684677208 m^2 | surfaceAreaSphereGen |
| 61 | Volume of Sphere | Volume of sphere with radius 14 m =  | 11494.040321933857 m^3 | volumeSphere |
| 62 | nth Fibonacci number | What is the 17th Fibonacci number? | 1597 | nthFibonacciNumberGen |
| 64 | Binary to Hexidecimal | 00 | 0x0 | binaryToHex |
| 65 | Multiplication of 2 complex numbers | (13-8j) * (-7-5j) =  | (-131-9j) | complexNumMultiply |
| 66 | Geometric Progression | For the given GP [12, 48, 192, 768, 3072, 12288] ,Find the value of a,common ratio,9th term value, sum upto 11th term | The value of a is 12, common ratio is 4 , 9th term is 786432 , sum upto 11th term is 16777212.0 | geometricprogression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 2 numbers 42 and 40 =  | (42*40)^(1/2) = 40.98780306383839 | geometricMean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 4 numbers 53 , 62 , 72 , 35 =  |  4/((1/53) + (1/62) + (1/72) + (1/35)) = 51.64137311701554 | harmonicMean |