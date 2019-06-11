#tuples examples
#6/11/2019

import sys
import timeit

#list example
prime_numbers = [2,3,5,7,11,13,17]

#Tuple example
perfect_squares = (1,4,9,16,25,36)

#display lengths
print('# Primes = ', len(prime_numbers))
print("# Squares = ", len(perfect_squares))

#iteration
for p in prime_numbers:
    print("Prime ", p)
for s in perfect_squares:
    print("Square ", s)

print("List methods")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods")
print(dir(perfect_squares))

#lists occupy more memory
print(dir(sys))
print(help(sys.getsizeof))

list_eg = [1,2,3,"a","b","c",True,3.14159]
tuple_eg = (1,2,3,"a","b","c",True,3.14159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

"""
    list
        add data
        remove data
        change data

    tuples
        cannot be changed
        Immutable
        Made quickly
"""

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List time: ", list_test)
print("Tuple time: ", tuple_test)

empty_tuple = ()
test1 = ("a") #<- this one is just a string really
test1_2 = ("a",) #<- this actually makes a tupple of one element
test2 = ("a","b")
test3 = ("a","b","c")

print(empty_tuple)
print(test1)
print(test1_2)
print(test2)
print(test3)

#alternatively we can create a tuple without using any grouping symbol
test4 = 1,
test5 = 1,2
test6 = 1,2,3

print("test4: ", test4," type: ", type(test4))
print("test5: ", test5," type: ", type(test5))
print("test6: ", test6," type: ", type(test6))

#(age,country,knows_python)
survey=(27,"Vietnam",True)

#we can access data elements of a tuple using indicies
print("Age= ", survey[0]," Country= ", survey[1], " Knows_Python= ", survey[2])


survey2 = 21, "Switzerland", False

#we can mass initialize variables with a tuple like this
#but there has to be the correct number of variables to accept all the 
#tuple indicies
age, country, knows_python = survey2
print("Survey 2")
print("Age= ", age)
print("Country= ",country)
print("Knows Python?= ",knows_python)