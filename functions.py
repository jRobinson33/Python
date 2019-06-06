#Python functions example
#6/6/2019

import math

# : colon starts new code block in python
# we also need to indent to keep code as part of the same code block

def ping():
	return "Ping!"
		
x = ping()
print(x)

def volume(r):
	"""returns the voluem of a sphere with radius r."""
	v = (4.0/3.0) * math.pi * r**3
	return v
	
def triangle_area(b, h):
	"""Returns the area of a triangle with base b and height h."""
	return 0.5 * b * h
	
#keyword arguments can be used in the arguments
# = 0 means that we are giving default values
# to call this function we have to use the variable names
# example: cm(feet = 6), cm(inches = 9), cm(feet = 2, inches = 3), cm(inches = 3, feet = 2)
def cm(feet = 0, inches = 0):
	"""Converts a length from feet and inches to centimeters."""
	inches_to_cm = inches * 2.54
	feet_to_cm = feet * 12 * 2.54
	return inches_to_cm + feet_to_cm
	
# If we mix and match default arguments with non-default arguments
# we must first put the non-default aruments def g(y, x = 0):
# In this case the y in the arguments section is called a required argument
def g(y, x = 0):
	"""Adds returns the sum of the required argument y, and the default argument x"""
	return y + x
	

	
