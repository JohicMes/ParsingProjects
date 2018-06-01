# Johic Mes 2018\05\07
import copy
import csv
import json
from ReferenceData import ReferenceData
from DataMapper import DataMapper
from SexParser import SexParser
from IDParser import IDParser
from DiseaseParser import DiseaseParser
from DateParser import DateParser
from AgeParser import AgeParser
from JsonObjListGenerator import JsonObjListGenerator
from insertJson import insertJson

#... just a couple of things needed 

# Buildig the parsable array from the CSV
rows = [] # Main array that will be parsed
size = 0
with open('DementiaData.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        rows.append(row) #Builds an array of the CSV file
        size += len(row)

# Building the ID object
ID_Table = DataMapper(rows)


# Start of the user facing main section of program
# Launches the parsing depending on type by calling the right parsing function
# Depending on the type of data being parsed certain questions are asked of the user to determine how to parse the CSV
Loop = True
Counter = 0
DataList = []
quintileList = [] # Need to build

print('First lets begin with the ID')
IDObject = IDParser(rows,ID_Table).getRDO() #Builds the objects and returns the list of RDO objects
IDObject.append(5)
DataList.append(IDObject)

print('What kind of data is being parsed')
print('Enter: 1 for AGE, 2 for SEX, 3 for DISEASE, 4 for DATE, 5 for REGION ID')

try:
    DataType = int(input('')) # Captures the kind of data that will be parsed
except ValueError:
    print('Not a number')

while(Loop == True and Counter < 4):
    if DataType == 1:
        print('Picked 1')
        AgeObject = AgeParser(rows,ID_Table).getRDO()
        AgeObject.append(1)
        DataList.append(AgeObject)
        Counter += 1

    elif DataType == 2: 
        print('Picked 2')
        SexObject = SexParser(rows,ID_Table).getRDO() #Builds the objects and returns the list of RDO objects
        SexObject.append(2)
        DataList.append(SexObject)
        Counter += 1

    elif DataType == 3:
        print('Picked 3')
        DiseaseObject = DiseaseParser(rows, ID_Table).getRDO() #Builds the objects and returns the list of RDO objects
        DiseaseObject.append(3)
        DataList.append(DiseaseObject)
        Counter += 1

    elif DataType == 4:
        print('Picked 4')
        DateObject = DateParser(rows, ID_Table).getRDO() #Builds the objects and returns the list of RDO objects
        DateObject.append(4)
        DataList.append(DateObject)
        Counter += 1
    else:
        print('I see you want the hidden option... too bad it does not exist!')

    try:
        DataType = int(input('Insert next type of data to parse or 0 to build GEOJson(end)')) # Captures the kind of data that will be parsed
    except ValueError:
        print('Not a number')

    if DataType == 0:
        Loop = False

# Once outside the loop we need to build the Json objects
JsonObjects = JsonObjListGenerator(DataList, size).GetJsonObj()
print('JsonObjGenerated')
#For debugging to view the Json objects created
# r = 0
# while r < len(JsonObjects):
#     print(JsonObjects[r])
#     r += 1
    
# Opens the topo Json that will need to be dumped in to\ gets strilng to work on
JsonFile = open('emptycanadamap.json', "r")
JsonString = ''
for line in JsonFile:
        JsonString += line
JsonFile.close()

#Pass it to the method that will return the final string with everything in it that we dump in the Json
JsonString = insertJson(JsonObjects, JsonString).getJsonFile()

#Debugging
print(JsonString)

# #Writes string back in topoJson
JsonFile = open('dataCanada.json', "w")
JsonFile.write(JsonString)
JsonFile.close()

#To test output debugging
# JsonFile = open('OriginalTopo.json', "r")
# JsonString = ''
# for line in JsonFile:
#         JsonString += line
# print(JsonString)
# JsonFile.close()

# End of program
print('Donezo!')
