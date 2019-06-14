#Example of using Random module
#6/14/2019

import random

print(help(random.random))

for i in range(10):
    print(random.random())

#Generate random numbers from interval[3,7)
#call random [0,1)
#scale number (multiply by 4): [0, 4)
#shift number (add 3) [3,7)

unimin=3
unimax=7
print("Using my_random(",unimin,",",unimax,")")
def my_random(lbound, ubound):
    # Random, scale, shift, return...
    return (ubound-lbound)*random.random() + lbound

for i in range(10):
    print(my_random(unimin, unimax))

print("Generating 10 numbers using random.uniform(",unimin,",",unimax,")")
print(help(random.uniform))

for i in range(10):
    print(random.uniform(unimin,unimax))

#generate 20 numbers from a standard bell curve
mean=0
standard_deviation=1
print("Generating 20 numbers of a standard bell curve with")
print("mean =",mean)
print("standard deviation =",standard_deviation)
for i in range(20):
    print(random.normalvariate(mean, standard_deviation))   

#generating random integers
minint = 1
maxint = 6

print("Generating random integers between ", minint, " and ", maxint)
for i in range(20):
    print(random.randint(minint, maxint))

print("Generating outcomes using random.choice(outcomes)")
print("where outcomes = ['rock', 'paper', 'scissors']")
outcomes = ['rock', 'paper', 'scissors']
for i in range(20):
    print(random.choice(outcomes))