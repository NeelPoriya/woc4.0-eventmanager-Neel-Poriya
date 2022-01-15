from random import *

filenames = ['texts\A day at zoo.txt', 'texts\At the arcade.txt', 'texts\The first day of school.txt', 'texts\The fun park.txt']
n = len(filenames)

file = open(filenames[randint(0, n-1)], 'r').read()

inputs = dict()
temp, startAdding = '', False
for c in file:
    if c == '}':
        startAdding = False
        if temp not in inputs.keys(): inputs[temp] = 1
        else: inputs[temp] += 1
        temp = ''

    if startAdding:
        temp += c

    if c == '{':
        startAdding = True

print('\nWelcome to MadLibs Game\nProivde comma separated inputs in case of more than 1 inputs asked\n')
input_count = inputs.copy()

for key in inputs:
    invalid = False
    while True:
        val = input(f'Enter {inputs[key]} {key} : ').split(',')
        invalid = False
        for v in val: 
            v = v.lstrip().rstrip()
            if v == '':
                invalid = True

        if (len(val) != inputs[key]) or invalid:
            print('Please provide correct number of inputs🥺')
            continue
        else:
            break

    inputs[key] = val

for key in inputs:
    for _ in range(0, input_count[key]):
        ind = randint(0, len(inputs[key])-1)
        file = file.replace(('{'+f"{key}"+'}'), inputs[key][ind], 1)
        inputs[key].remove(inputs[key][ind])

print('\n', file, '\n')
