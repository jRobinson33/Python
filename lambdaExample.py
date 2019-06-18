# example of how to use lambda expression
#6/18/2019
#common uses for lambda are sorting and filtering data

lambda x: 3*x + 1

g = lambda x: 3*x+1
print(g(2))

# Combine first name and last name into a single "Full Name"
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   leonhard", "EULER"))

# lambda x1, x2... : <expression>   we can't use lambda for multiline functions

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clark",
        "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

print(help(scifi_authors.sort))

# Sorting the list of scifi_authors accodring to last name
# We use a lambda expression for the key
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)
print("f(0): ", f(0))
print("f(1): ", f(1))
print("f(2): ", f(2))

print("3x^2 + 1 for x = 2 : ",build_quadratic_function(3,0,1)(2)) # 3x^2 + 1 for x = 2