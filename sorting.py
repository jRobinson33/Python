#Python sorting
#6/24/2019

#sorting alphabetically 
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
earth_metals.sort()
print("Earth metals alphabetically:", earth_metals)

#reverse alphabetic order
earth_metals.sort(reverse=True)
print("Earth metals reverse alphabetically:", earth_metals)

#We can't sort a tuple, because they are immutable objects
#list.sort has L.sort(key=None, reverse=false) as default arguments
#key is a function

#planets tuple format = (name, radius at equator in kilometers, density g/cm^3, distance to sun in AUs)
#AU = astronomical unit, roughly distance from earth to sun
planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
    ]
# to sorty them by size
size = lambda planets: planets[1]
planets.sort(key=size, reverse=True)
print("Planets sorted in reverse size order: ", planets)

#sorting by density
density = lambda planet: planet[2]
planets.sort(key=density)
print("Planets sorted by density: ", planets)

#the sorted method can returns a new list containing all items from the iterable in ascending order
sorted_earth_metals = sorted(earth_metals)
print("sorted_earth_metals: ", sorted_earth_metals)
print("earth_metals: ", earth_metals)

data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
sorted_data = sorted(data)
print("data sorted: ", sorted_data)
print("data: ", data)