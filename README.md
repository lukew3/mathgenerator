# mathgenerator
A math problem generator, created for the purpose of giving self-studying students and teaching organizations the means to easily get access to random math problems to suit their needs.

To try out generators, go to https://todarith.ml/generate/

If you have an idea for a generator, please add it as an issue and tag it with the "New Generator" label.

## Usage
The project can be install via pip
```
pip install mathgenerator
```
Here is an example of how you would generate an addition problem:
```
from mathgenerator import mathgen

#generate an addition problem
problem, solution = mathgen.addition()
```
## List of Generators

| Id   | Skill                      | Example problem | Example Solution  | Function Name            | Status      |
|------|----------------------------|-----------------|-------------------|--------------------------|-------------|
| 2    | Addition                   | 1+5=            | 6                 | addition                 | Complete    |
| 3    | Subtraction                | 9-4=            | 5                 | subtraction              | Complete    |
| 4    | Multiplication             | 4*6=            | 24                | multiplication           | Complete    |
| 5    | Division                   | 4/2=            | 2                 | division                 | Complete    |
| 6    | Binary Complement 1s       | 1010=           | 0101              | binaryComplement1s       | Complete    |
| 7    | Modulo Division            | 10%3=           | 1                 | moduloDivision           | Complete    |
| 8    | Square Root                | sqrt(a)=        | b                 | squareRootFunction       | Complete    |
| 9    | Power Rule Differentiation | nx^m            | (n*m)x^(m-1)      | powerRuleDifferentiation | Complete    |
