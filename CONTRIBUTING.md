# Contributing

This project wouldn't be possible without the generosity of contributors like you. Thank you!

## How You Can Help
Currently, there are 4 main types of contributions

1. Add a generator idea to `futureGenerators.md`. You can add a row to the table manually or run the `addFuture.py` file inside the scripts folder to add your generator idea to the file automatically. Just fill out the prompts!
2. Fix bugs in existing generators. Check out the issues tab of the Github to see what bugs exist and need to be fixed.
3. Add latex output formatting to a current generator. To see which generators need latex formatting, run `needsLatex.py` inside of the scripts folder and choose a generator to add latex formatting to.
4. Write a generator. A template and a template with comments is provided in the `mathgenerator/funcs` directory. Make sure to place your generator function into the correct subject folder of `mathgenerator/funcs/`

If you find something else that you'd like to work on, leave an issue or make a pr, and I'll be sure to review it!

## First Time Contributors
If you have never contributed to open source before here is a quick explanation of how to contribute.

* Fork this repository on Github. This creates a copy of the current code that you can edit and make changes to.
* Navigate to your fork and make your changes. This could be done by cloning and making changes locally on your computer. You can find many tutorials on this online. You could also edit directly on Github if you don't have access to a text editor but doing this, you will not be able to test your function.
* Create a pull request. Navigate to (the math generator repository pull request tab)[https://github.com/Todarith/mathGenerator/pulls] and click New Pull Request. Then click compare accross forks. Select your fork and branch as the head branch and leave a description. Then click Create Pull Request.
* If all goes well, your request will be approved and your generator added. Congratulations!
