# Contributing

This project wouldn't be possible without the generosity of contributors like you. Thank you!

## How You Can Help
* Add a generator idea to github issues.
* Fix bugs in existing generators. Check out the issues tab of the Github to see what bugs exist and need to be fixed.
* Write a generator. Write a function that generates a problem string and solution string. Use latex formatting for math, with `$` being on either side of latex expressions. Then, add a tuple `(<generator_name>, <subject>)` to the `mathgenerator/_gen_list.py` file. Follow the pattern in [the template](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/template.py) and the [template with comments](https://github.com/lukew3/mathgenerator/blob/main/mathgenerator/funcs/template_comments.py). 
* Improve demo/documentation site. The source code for the mathgenerator website is in the `demo` branch.

If you find something else that you'd like to work on, leave an issue or make a pr, and I'll be sure to review it!

## First Time Contributors
If you have never contributed to open source before here is a quick explanation of how to contribute.

* Fork this repository on Github. This creates a copy of the current code that you can edit and make changes to.
* Navigate to your fork and make your changes. This could be done by cloning and making changes locally on your computer. You can find many tutorials on this online. You could also edit directly on Github if you don't have access to a text editor but doing this, you will not be able to test your function.
* To test your changes, open a terminal and from the project root, run `pip install -e .` to install a locally editable version of the mathgenerator package. Then, run a python terminal with `python`, `import mathgenerato` and call the method you worked on.
* Commit and create a pull request. Navigate to [the math generator repository pull request tab](https://github.com/Todarith/mathGenerator/pulls) and click New Pull Request. Then click compare accross forks. Select your fork and branch as the head branch and leave a description. Then click Create Pull Request.
* If all goes well, your request will be approved and your generator added. Congratulations!
