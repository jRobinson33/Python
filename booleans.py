#python booleans
#6/3/2019

#both True and False are capatalized 

a = 3
b = 5

print("Showing the boolean output of comparisons")
print(a == b)
print(a != b)
print(a > b)
print(a < b)

print("Showing type of True and False")
print(type(True))
print(type(False))

print("Showing that False is 0 and everything else is true when it comes to numbers")
print(bool(28))
print(bool(-2.71828))
print(bool(0))

print("Only the empty string is seen as False, otherwise it's True")
print(bool("Turing"))
print(bool(" "))
print(bool(""))


print("converting True and False to strings")
print(str(True))
print(str(False))


print("converting True and False to ints")
print(int(True))
print(int(False))

print("you can use the values of True and False in arithmetic")
print(5 + True)
print(10 * False)

