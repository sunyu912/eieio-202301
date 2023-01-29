# Air Cownditioning II
# http://usaco.org/index.php?page=viewproblem&cpid=1264

from operator import sub
import itertools as iter

cowCount, acCount = [int(n) for n in input().split()]

# calculate the current temperature array based on the cow's input
temperatures = [0] * 100
for i in range(cowCount):
    start, end, currTemp = [int(n) for n in input().split()]
    start -= 1
    for j in range(start, end):
        temperatures[j] = currTemp
        
# create the air conditioner dictionary lookup table
char = 97
ac = {} # [cost, [reduced temperature profile]]
for i in range(acCount):
    start, end, reducedTemp, cost = [int(n) for n in input().split()]
    start -= 1
    end -= 1
    temp = [0] * 100
    for j in range(start, end + 1):
        temp[j] = reducedTemp
    ac[chr(char)] = [cost, temp]
    char += 1
acNames = list(ac.keys())

# generate all possible combinations for the air conditioners
nCr = [''.join(e) for i in range(len(acNames)) for e in iter.combinations(acNames, i + 1)]

# initialize the lookup table.
records = {} # [cost, current temperature profile after adding these ACs]
for i in range(len(acNames)):
    records[acNames[i]] = [ac[acNames[i]][0], \
                            list(map(sub, temperatures, ac[acNames[i]][1]))]

# Helper function: check whether this temperature profile has cooled enough
def isDone(temperature):
    for t in temperature:
        if (t > 0):
            return False
    return True

# check if the first pass gets the answer
for i in range(len(acNames)):
    if (isDone(records[acNames[i]][1])):
        records[acNames[i]][0] = records[acNames[i]][0] * -1

# go through every combination and combine the current with the previous.
for i in range(len(acNames), len(nCr)):
    if (nCr[i][:-1] in records and nCr[i][-1] in records):
        prefix = records[nCr[i][:-1]]
        postfix = ac[nCr[i][-1]]
    else:
        continue
    if (prefix[0] < 0 or postfix[0] < 0):
        continue
    currTemp = list(map(sub, prefix[1], postfix[1]))
    if (isDone(currTemp)):
        records[nCr[i]] = [(prefix[0] + postfix[0]) * -1, currTemp]
    else:
        records[nCr[i]] = [prefix[0] + postfix[0], currTemp]       

answer = -10000
for key, value in records.items():
    if (value[0] < 0):
        answer = max(value[0], answer)

print(answer * -1)
