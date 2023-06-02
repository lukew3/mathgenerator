import os

print(
    "You are about to add a new generator to the table in futureGenerators.md")
print("Please fill out the following:")
title = input("> Title: ")
example_problem = input("> Example Problem: ")
example_solution = input("> Example Solution: ")
further_explanation = input("> Further explanation (optional): ")

if os.getcwd()[-7:] == 'scripts':
    file = '../futureGenerators.md'
else:
    file = './futureGenerators.md'

with open(file, 'a') as f:
    f.writelines(
        f'| {title} | {example_problem} | {example_solution} | {further_explanation} |\n'
    )
