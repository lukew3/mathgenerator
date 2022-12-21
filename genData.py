import mathgenerator
import json

genList = mathgenerator.getGenList()

data = []
for gen in genList:
    samples = []
    for _ in range(10):
        p, s = mathgenerator.genById(gen[0])
        samples.append({"problem": p, "solution": s})
    data.append({
        "id": gen[0],
        "name": gen[1],
        "function_name": gen[3],
        "subject": gen[4],
        "kwargs": gen[5],
        "samples": samples
    })

out_file = open("data.js", "w")
out_file.write('const data = ')
json.dump(data, out_file)
out_file.close()