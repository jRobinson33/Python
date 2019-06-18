#using JSON files example
#6/18/2019

import json

#Had to add -sig to utf-8 at the end.
#The python interpreter gave an error suggesting this change in a 
#json.decoder.JSONDecodeError
json_file = open("C:/Users/Turing/Desktop/Python/jsonExample/movie_1.txt","r", encoding="utf-8-sig")
movie = json.load(json_file)
json_file.close()

print(type(movie))
print(movie["actors"])

value = """
        {"title": "Tron: Legacy",
         "composer": "Daft Punk",
         "budget": 170000000,
         "actors" : null,
         "won_oscar" : false
        }"""

tron = json.loads(value)
print(tron)


print(json.dumps(movie)) #this adds the unicode code to the special character
print(json.dumps(movie, ensure_ascii=False)) #This correctly displays the special character

movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski"

file2 = open("C:/Users/Turing/Desktop/Python/jsonExample/movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False)
file2.close