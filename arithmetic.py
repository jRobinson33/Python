"""
	rules of arithmetic in python
	5/30/2019
"""

x = 28 #int
y = 28.0 #float
z = 12 + 0j

#we can keep only the whole part of a float bytearray
a = int(y)
msg1 = "y before using int() " + str(y)
print(msg1)

msg2 = "and after using int(y) " + str(a)
print(msg2)

#you can convert floats to complex numbers but not the other way around
complexNum = y + 0j
complexNum2 = complex(y)

print(str(complexNum))
print(str(complexNum))

# Rule: Widen numbers so they're the same type
#Addition
intFloat = x + y# int + float
print(str(intFloat)) #end result is float

#Subtraction
floatInt = y - x
print(str(floatInt)) #end result is float

#Multiplication
floatComplex = y * z
print(str(floatComplex)) #end result is complex

#Division
complexFloat = z / y
print(str(complexFloat)) #end result is complex

#dividing 2 whole numbers in python 3 will result in a float
wholeDiv = 16/5
print(str(wholeDiv))

#to get just the remainder we can use the %
mod = 16%5
print(str(mod))

#to get the whole number we can use the // for division
div = 16 // 5
print(str(div))

