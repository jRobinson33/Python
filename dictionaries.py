#Dictionary tutorial
#6/10/2019

#Python dictionaries are like maps
#dictionary inputs are called keys, and outputs are called values

#this is a dictionary with 5 pieces of data called post
# "input":output  or  "key":value
post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"English",
        "datetime":"20230215T124231Z", "location":(44.590533, -104.715556)}

print("type(post): ", type(post))

post2 = dict(message="SS Cotopaxi", language="English")
print(post2)

#we use brackets to add new pieces of data to a dictionary
post2["user_id"] = 209
post2["datetime"] = "1771116T093001Z"

print("post2: ", post2)

#we also use brackets to access data in a dictionary
print(post['message'])

#if we try to access data in a post that doesn't exist, then we get an error
#we can use th 'in' operator to check if the data exists in the structure

if 'location' in post2:
    print(post2['location'])
else:
    print("The post does not contain a location value.")


#This is also our first example of pythong's version of try catch
try:
    print(post2['location'])
except KeyError:
    print("The post does not have a location.")

loc = post2.get('location', None)
print("Using get on post2 to try and get the location: ", loc)

#a couple examples of using for loops to go throughand print
#all of the key value paires from our post dictionary
print("printing key value paires")
for key in post.keys():
    value = post[key]
    print(key, "=", value)

for key, value in post.items():
    print(key, "=", value)

""