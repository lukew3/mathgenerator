# mathgenerator

A math problem generator, created for the purpose of giving self-studying students and teaching organizations the means to easily get access to random math problems to suit their needs.

To try out generators, go to <https://lukew3.github.io/mathgenerator>

See [CONTRIBUTING.md](https://github.com/lukew3/mathgenerator/blob/main/CONTRIBUTING.md) for information about how to contribute.

## Table of Contents
* [Installation](#installation)
* [Basic Usage](#basic-usage)
  * [More Complicated Usage](#more-complicated-usage)
* [Documentation](#documentation)
* [List of Generators](#list-of-generators)
  * [algebra](#algebra)
  * [basic_math](#basic_math)
  * [calculus](#calculus)
  * [computer_science](#computer_science)
  * [geometry](#geometry)
  * [misc](#misc)
  * [statistics](#statistics)

## Installation

The project can be install via pip

```bash
pip install mathgenerator
```

## Basic Usage
Here is an example of how you would generate an addition problem:

```python
from mathgenerator import mathgen

#generate an addition problem
problem, solution = mathgen.addition()

#another way to generate an addition problem using genById()
problem, solution = mathgen.genById(0)
```
### Creating a worksheet
If you wish to create a worksheet, you can use the [worksheetgen](https://github.com/lukew3/worksheetgen) package. Install this with `pip install worksheetgen`. Here is an example of how a worksheet would be generated.
```
from mathgenerator import mathgen
from worksheetgen.wg import Worksheet

worksheet = Worksheet("Worksheet title")
worksheet.add_instruction("Instructions")
# Writes 10 problems generated with id 1, [0] at the end specifies to take problem, and not solution.
for _ in range(10):
	worksheet.add_problem(mathgen.genById(1)[0])
worksheet.write_pdf()
```
This creates the pdf `ws.pdf` in your current directory

## Documentation
* `getGenList()` returns a list of all generators in the repository in the format `[id, title, self, funcname, subjectname]`

* `genById(id)` generates a problem, solution set with generator id `id` in the format `[problem, solution]`

* Pass the kwarg `format=latex` to return problem and solution set as latex. If latex is not available for that generator, the problem will return the string "Latex unavailable"

* Pass the kwarg `format=raw` to return just the raw data for each generator. An array of each variable necessary to the generator is returned.

## List of Generators
## algebra
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
## basic_math
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
## calculus
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
## computer_science
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
## geometry
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
## misc
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
## statistics
| Id   | Skill | Example problem | Example Solution | Function Name | Kwargs |
|------|-------|-----------------|------------------|---------------|--------|
