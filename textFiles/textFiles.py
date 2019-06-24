#reading and writing text files
#6/24/2019

# 2 types of files, text files - plain text, xml, JSON, Source code
#                   Binary files - Compiled code, App data, Media files (images, audio, video)

"""
f = open("guido_bio.txt")
text = f.read()
f.close()
print(text)
"""
try:
    with open("guido_bio.txt") as fobj:
        bio = fobj.read()
except FileNotFoundError:
    text = None

print(bio)

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
"""
with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")

"""
with open("oceans.txt", "w") as f:
    for ocean in oceans:
        print(ocean, file=f)

#append mode
with open("oceans.txt", "a") as f:
    print(23*"=", file=f)
    print("These are the 5 oceans.", file=f)
