#Lists tutorial
#6/8/2019

#2 ways of declaring lists
example = list()
example2 = []

#adding elements to a list while declaring the list
primes = [2, 3, 5, 7, 11, 13]

#appending items to the end of the list
primes.append(17)
primes.append(19)
print("Primes ", primes)

#We can access the elements of a list like in other programming languages
print("First prime ", primes[0])

#we can even access the elents in reverse, but we can only go in reverse once
print("Last prime", primes[-1])

#slicing displays from the first element given to n-1 such that n is the last element given
#example primes[2:5] will give [5, 7, 11]
print("Slicing with elements 2 through 5",primes[2:5])
print("Slicing with elements 0 through 6",primes[0:6])

#showing that we can have multiple data types in a single list, even other lists
example3 = [128, True, "Alpha", 1.732, [64, False]]
print("Lists can have multiple data types in them ", example3)

#showing an important difference between lists and sets
rolls = [4, 7, 2, 7, 12, 4, 7]
print("Unlike sets, lists can have duplicate data values ", rolls)

#example of concatenating, remember order matters with lists, unlike sets
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print("We can also concatenate lists numbers + letters: ",  numbers + letters)
