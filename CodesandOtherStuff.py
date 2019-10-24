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
