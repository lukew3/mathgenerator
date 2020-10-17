# Contributing

This project was created with contributions at it's core. We need your help to expand the reach of this project and open-source the generation of math problems.

## How You Can Help

### Coding Generators
As of right now, all of our generators are being coded in python. Your generator will be an object of the Generator class and will have a function created seperately.
Your object instantiation should follow this format:
```
#<title> = Generator("<Title>", <id>, <generalized problem>, <generalized solution>, <function name>)

```
The Object generator reperesentign something like this would be considered:
```
addition = Generator("Addition", 2, "a+b=", "c", additionFunc)
```
Your function should look something like the following:
```
def additionFunc(maxSum, maxAddend):
    a = random.randint(0, maxAddend)
    b = random.randint(0, min((maxSum-a), maxAddend)) #The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    c = a+b
    problem = str(a) + "+" + str(b) + "="
    solution = str(c)
    return problem, solution
```

Before coding, please check README.md to see if someone has already created the generator you plan to make.
Skillid is determined by the next available id as can be determined in the table.

### Provide Ideas
If you have an idea for a generator but don't have the time or know-how to create it, you can add it as an issue. If you have a lot of ideas, I would suggest adding them to the table in README.md so that they are easier for our team to manage. Idea providing must not be duplicate as it may raise concerns over originality.

## First Time Contributors
If you have never contributed to open source before here is a quick explanation of how to contribute.

* Fork this repository on Github. This creates a copy of the current code that you can edit and make changes to.
* Navigate to your fork and make your changes. This could be done by cloning and making changes locally on your computer. You can find many tutorials on this online. You could also edit directly on github if you don't have access to a text editor but doing this, you will not be able to test your function.
* Create a pull request. Navigate to (the math generator repository pull request tab)[https://github.com/Todarith/mathGenerator/pulls] and click New Pull Request. Then click compare accross forks. Select your fork and branch as the head branch and leave a description. Then click Create Pull Request.
* If all goes well, your request will be approved and your generator added. Congratulations!
