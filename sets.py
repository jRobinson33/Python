#Python sets tutorial
#6/7/2019
#more on sets can be found at https://www.w3schools.com/python/python_sets.asp

#declaring a variable to be for a set
example = set()

#adding things to our set
#what we add to the set doesn't have to all be the same type
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

#When displaying, we may see that it doesn't show in the same order we add
print(example)

#we can't have duplicates in a set
example.add(42)
print("We can't have duplicates in a set ",example)

#we can see the length of our set
print("The length of our set is: ", len(example))

#we can remove things from our set
print("removing element 42 ")
example.remove(42)
print("The length of our set is: ", len(example))
print(example)

#we can't remove things that aren't in the set
#using discard is a good alternative to remove
#if the data is not in the set and you use remove, you will get an error
#if the data is not in the set and you use discard, then no error is thrown
example.discard(50)


#Another way to create a set
example2 = set([28, True, 2.71828, "Helium"])

print("The size of our new set is: ", len(example2))
print(example2)

#we can delete everything in the set quickly
example2.clear()
print("The size of our new set after using clear: ", len(example2))
print(example2)

#we can use union and intersect on sets
odds = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10])

print("odds union evens ", odds.union(evens))
print("evens union odss ", evens.union(odds))
print("odds intersect primes ", odds.intersection(primes))
print("primes intersetct evens ", primes.intersection(evens))
print("primes union composites ", primes.union(composites))

# we can see if an item is in a set or if it is not in a set
print("2 in primes: ", 2 in primes)
print("6 in odds: ", 6 in odds)
print("9 not in evens: ", 9 not in evens)


