#list comprehensions
#6/18/2019

# List: [ 1, 2, "a", 3.14]
# List Comprehensions: [expr for val in collection] or for certain pieces of data to be added
#[expr for val in collection if <test>] or with multile tests
#[expr for val in collection if <test1> and <test2>] and you can loop over more than 1 collection
#[expr for val1 in collection1 and val2 in collection2]

#first example is traditional way without python list comprehensions
squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

#same thing as above but with 1 line in place of 3
squares2 = [i**2 for i in range(1, 101)]
print(squares2)

remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)


#We can do this over strings as well
movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story",
    "Gone with the Wind", "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz",
    "Gattaca", "rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting",
    "2001: A Space Odyssey", "Raiders of the Lost Ark", "Groundhog Day", "Close Encounters of the Third Kind"]

gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)

# We can also do this to extract the value in a tuple
gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2)

movies2 = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946),
    ("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1954), 
    ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("Groundhog Day", 1993), 
    ("Close Encounters of the Third Kind", 1977), ("The Royal Tenenbaums", 2001), 
    ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]

pre2k = [title for (title, year) in movies2 if year < 2000]
print(pre2k)

#example using scalar multiplication
v = [2, -3, 1]
w = [ 4*x for x in v]
print(w)

#cartesian product of sets
# If A and B are sets, then the Cartesian product is the set of pairs (a, b)
# where 'a' is in A and 'b' is in B
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)