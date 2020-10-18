# To use, paste at bottom of mathgen.py code, change line variable and remove all table rows in README.md except for the top 2 and run mathgen.py

wList = getGenList()
allRows = []
f = open('mathgen.py')
lines = f.readlines()
line = 720  # This has to be changed depending on which line the first generator appears on
for item in wList:
    myGen = item[2]
    prob, sol = myGen()
    prob = str(prob).rstrip("\n")
    sol = str(sol).rstrip("\n")
    instName = lines[line]
    def_name = instName[:instName.find('=')].strip()
    row = [myGen.id, myGen.title, prob, sol, def_name]
    line += 1
    allRows.append(row)

g = open('../README.md', "a")
for row in allRows:
    tableLine = "| " + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " | " + str(row[3]) + " | " + str(row[4]) + " |\n"
    g.write(tableLine)
g.close()

print("New README.md table generated")
