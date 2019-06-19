#examples of mapping filtering and reducing
#6/18/2019

import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method
areas = []
for r in radii:
    a = area(r)
    areas.append(a)
print("Direct method areas: ", areas)

# Method 2: use 'map' function
# map takes in a function and a list map(function, list)
print(map(area, radii)) #returns an iterater according to output

print(list(map(area, radii)))

# temps is a list of tuples of form (city, temp in celcius)
temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19),
        ("Los Angeles", 26), ("Tokyo",27), ("New York", 28),
        ("London", 22), ("Beijing", 32)]

# We want ot convert celcius to farenheit
c_to_f = lambda data: (data[0], (9/5)*data[1]+32)
print("Temps from C to F: ", list(map(c_to_f, temps)))

# filtering
import statistics
import decimal

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(data," average amounts of fuel: ", avg)

# filter(function, list) which returns a filter object, an iterator over the results
print("Data above average: ", list(filter(lambda x: x > avg, data)))
print("Data below average: ", list(filter(lambda x: x < avg, data)))

# Remove missing data
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]

# we want to filter out the missing data
# some things you can use in the function for empty data
# "", 0, 0.0, 0j, [], (), {}, False, None, instances which signal they are empty
print("Countries in South America: ",list(filter(None, countries)))

# Reduce function
# data: [a1, a2, a3...]
# Function: f(x,y)
# reduce(f, data)
#   Step 1: val1 = f(a1, a2)
#   Step 2: val2 = f(val1, a3)
#   Step 3: val3 = f(val2, a4)
#   ...
#   Return val(n-1)

from functools import reduce
# Multiply all numbers in a list
data = [2,3,5,7,11,13,17,19,23,29]
multiplier = lambda x, y: x*y 
print("Product of prime numbers data list: ", reduce(multiplier, data))