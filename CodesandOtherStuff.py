# Strings
#     data that falls within " " marks

# Concatenation
# Put 2 or more strings together

firstName = "Fred"
lastName = "Flintstone"

fullName = firstName + " " + lastName

print(fullName)

# Repitition
#  repitition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
#   slicing operator: :
#   slicing lets  us make substrings

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name)+1):
    print(name[0:i])

# Searching inside of Strings

print("biv" in name)
print("v" not in name)

if "y" in name:
    print("The letter y is in the name")
else:
    print("The letter y is not in name")