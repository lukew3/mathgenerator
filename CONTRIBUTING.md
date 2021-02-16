# Contributing

This project wouldn't be possible without the generosity of contributors like you. Thank you!

## How You Can Help

### Coding Generators
Before coding, please check README.md to see if someone has already created the generator you plan to make.
You can find a simple example of a generator in the [addition file](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/basic_math/addition.py)
To start, create a new file with the name of your generator in the subject folder of best fit, which is inside the `funcs` folder of `mathgenerator`. The name of the file must be all lowercase with underscores seperating words.

Here's what needs to be included in a new generator:
* `from .__init__ import *`
  * Imports `Generator` class from `__init__.py` in the mathgenerator directory.
* Generator function with kwargs
  * This function is where the output is generated.
  * Should have at least one kwarg.
  * Returns a pair of string values, `problem` and `solution`
* Generator object instantiation
  * Object should have the same name as file name
  * Must have the following arguments (title, id, example problem, example solution, function, list of kwargs)
    * Most of these are ways of keeping track of generators and providing documentation.
    * skillid should be the number of the lowest unassigned id.
      * Use this id: <!--Start next id-->113<!--End next id-->. (This is updated automatically after a new generator is added)
    * function should be the name of the function defined above without quotes
    * List of kwargs should be a list of the kwargs that the function takes as strings. Used in documentation.

You also need to import the module in the `__init__.py` file of the subject folder.
* To do this, add `from .<your_generator_file> import *` to the end of the `__init__` file of the subject that your generator is stored in.


Finally, make sure that your generator passes the github actions tests. If it doesn't, make the changes requested in a new commit.
### Provide Ideas
If you have an idea for a generator but don't have the time or know-how to create it, you can add it as an issue.

## First Time Contributors
If you have never contributed to open source before here is a quick explanation of how to contribute.

* Fork this repository on Github. This creates a copy of the current code that you can edit and make changes to.
* Navigate to your fork and make your changes. This could be done by cloning and making changes locally on your computer. You can find many tutorials on this online. You could also edit directly on github if you don't have access to a text editor but doing this, you will not be able to test your function.
* Create a pull request. Navigate to (the math generator repository pull request tab)[https://github.com/Todarith/mathGenerator/pulls] and click New Pull Request. Then click compare accross forks. Select your fork and branch as the head branch and leave a description. Then click Create Pull Request.
* If all goes well, your request will be approved and your generator added. Congratulations!
