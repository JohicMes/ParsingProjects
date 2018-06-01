# Johic Mes 2018\05\07
# Reference data: The objects the parsing will create and will be used to build the Json objects. 


class ReferenceData(object):
    SortType = 'None'
    Data = 0
    ID = -1

    # Constructor builds the object with the three parameters it needs
    def __init__(self, SortType, Data, ID):
        """ Make an object for a category: Param SortType, Data, ID """
        self.SortType = SortType
        self.Data = Data
        self.ID = ID
        
    #Getters to retreive the information.
    def getSortType(self):
        return self.SortType

    def getData(self):
        return self.Data

    def getID(self):
        return self.ID