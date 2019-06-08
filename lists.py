

example = list()
example2 = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)

print("Primes ", primes)

print("First prime ", primes[0])

print("Last prime", primes[-1])

print("Slicing with elements 2 through 5",primes[2:5])
print("Slicing with elements 0 through 6",primes[0:6])

example3 = [128, True, "Alpha", 1.732, [64, False]]
print("Lists can have multiple data types in them ", example3)

rolls = [4, 7, 2, 7, 12, 4, 7]
print("Unlike sets, lists can have duplicate data values ", rolls)

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print("We can also concatenate lists numbers + letters: ",  numbers + letters)
