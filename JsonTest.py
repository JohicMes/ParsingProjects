import json

# RANDOM CRAP FOR TESTING PURPOSES - NOT PART OF THE PROJECT #

x = 'I love apples'
y = 'to eat '
z = 7

print(x.find('a' or 'l'))

def insert(OGstring, index, toInsert): # Method to insert a string at any index
        OGstring = OGstring[:index] + toInsert + OGstring[index:]
        return OGstring

x = insert(x,z,y)
print(x)

JsonFile = open('OriginalTopo.json', "r")
JsonString = ''
for line in JsonFile:
        JsonString += line
JsonFile.close()

JsonString += 'YAAAAAAAS'

JsonFile = open('OriginalTopo.json', "w")
json.dump(JsonString, JsonFile)
JsonFile.close()

JsonFile = open('OriginalTopo.json', "r")
JsonString = ''
for line in JsonFile:
        JsonString += line

print(JsonString)

JsonFile.close()