#Recursion, fibonacci, and recursion
#6/13/2019

#used for a python style memoization caching feature, demonstrated 
# in the second fibonacci function
from functools import lru_cache
"""
fibonacci_cache = {}

def fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    #Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    #Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 1001):
    print(n, ":", fibonacci(n))
"""

#to use the lru_cache we write it like this
#it will default to a maxsize of 128 if we 
#don't specify a number
@lru_cache(maxsize = 1000)
def fibonacci(n):
    #Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise TypeError("n must be a positive int")

    #Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 5001):
    print(n, ":", fibonacci(n))
    print(fibonacci(n+1) / fibonacci(n))