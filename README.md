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
| 0    | Addition                          | 1+5=               | 6                     | addition                 |
| 1    | Subtraction                       | 9-4=               | 5                     | subtraction              |
| 2    | Multiplication                    | 4*6=               | 24                    | multiplication           |
| 3    | Division                          | 4/3=               | 1.33333333            | division                 |
| 4    | Binary Complement 1s              | 1010=              | 0101                  | binaryComplement1s       |
| 5    | Modulo Division                   | 10%3=              | 1                     | moduloDivision           |
| 6    | Square Root                       | sqrt(25)=          | 5                     | squareRootFunction       |
| 7    | Power Rule Differentiation        | 4x^3               | 12x^2                 | powerRuleDifferentiation |
| 8    | Square                            | 4^2                | 16                    | square                   |
| 9    | LCM (Least Common Multiple)       | LCM of 14 and 9 =  | 126                   | lcm                      |
| 10   | GCD (Greatest Common Denominator) | GCD of 18 and 18 = | 18                    | gcd                      |
| 11   | Basic Algebra                     | 9x + 7 = 10        | 1/3                   | basicAlgebra             |
| 12   | Logarithm                         | log3(3)            | 1                     | log                      |
| 13   | Easy Division                     | 270/15 =           | 18                    | intDivision              |
| 14   | Decimal to Binary                 | Binary of a=       | b                     | decimalToBinary          |
| 15   | Binary to Decimal                 | Decimal of a=      | b                     | binaryToDecimal          |
| 16   | Fraction Division                 | (a/b)/(c/d)=       | x/y                   | fractionDivision         |
| 17   | Int 2x2 Matrix Multiplication     | k * [[a,b],[c,d]]= | [[k*a,k*b],[k*c,k*d]] | intMatrix22Multiplication|
