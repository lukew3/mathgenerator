import os

file = ""
with open("mathgen.py", 'r') as f:
    file = f.read()

file = file.split("\n\n")[8:]

i=0

imports_string = ""
for listing in file:
    listing = listing[1:]
    if listing[:3] == "def":
        name = listing[4:listing.find("(")]
        imports_string+="import funcs."+name+"\n"
        with open("funcs/"+name+".py", 'w') as f:            
            f.write("from funcs.imports import *\n\n\n"+listing+"\n")
            print("Saved!", i, "-", name)
        i+=1

with open("funcs/imports.py", 'w') as imports_file:
    imports_file.write(imports_string+"\n")

# print(file)