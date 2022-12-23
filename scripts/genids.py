import mathgenerator

with open('../mathgenerator/ids.txt', 'w') as f:
    f.write('\n'.join([f'{g[4]}/{g[3]}' for g in mathgenerator.getGenList()]))
