#if then else tutorial
#6/5/2019

#collect string / test length

#input = raw_input("Please enter a test string: ")
iput = input("Please enter a test string: ")

#indentation, not braces, designate a code block in python
if (len(iput)) < 6:
	print("Your string is too short.")
	print("Please enter a string with at least 6 characters.")
	
	
#rather than starting a new file for the video, i'll just keep going in the same file

#prompt user to enter number / test if even or odd
iput2 = input("Please enter an integer: ")
number = int(iput2)

if number % 2 == 0:
	print("Your number is even.")
else:
	print("Your number is odd.")
	


#Scalene triangle: all sides have different lengths
#isosceles triangles: two sides have the same length
#equilateral triangle: all sides are equal

a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))

if a != b and b != c and a != c:
	print("This is a scalene triangle.")
elif a == b and b == c:
	print("This is an equilateral triangle.")
else:
	print("This is an isosceles triangle.")