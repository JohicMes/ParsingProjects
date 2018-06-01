# Johic Mes 2018\05\07
import copy
#Builds a shadow array exactly the same dimmensions of the original array but creates an id in the place of the data
class DataMapper(object):

    #Initialise a new table and calls the function to replace the values with the ID
    def __init__(self, table):
        self.IDTable = copy.deepcopy(table)
        self.MapTable()

    #Inserts the new values in the table
    def MapTable(self):
        i = 0
        while i < len(self.IDTable):
            j = 0
            while j < len(self.IDTable[i]):
                self.IDTable[i][j] = (i+(j*len(self.IDTable))) # Replaces the value by a ID value w/ the formula 
                j += 1
            i += 1
        return self.IDTable

    #Getters that will be needed when assigning the ID to the RDO
    def getID(self,i,j): # Gets the ID at a certrain place.
        x = 0
        x = self.IDTable[i][j] # No out of bounds checking!
        return x
        
    def getYLenght(self): # Returns the lenght in the Y direction
        return len(self.IDTable)

    def getXLenght(self): # Returns the lenght in the X direction
        return len(self.IDTable[1]) # Not perfect because the lenght of a column can varry but meh good enough for now