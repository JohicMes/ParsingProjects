# Johic Mes 2018\05\07
from ReferenceData import ReferenceData
from DataMapper import DataMapper

class IDParser(object):
    ID = []
    quintilePlacement = []
    
    def __init__(self, rows, ID_Table):
        try:
            Col_Row = int(input('Is the HRUID\PRUID in a column(0) or row(1)'))
        except ValueError:
            print('Not a number')
        try:
            SortTypePLace = int(input('What row/column are the ID placed?'))-1
        except ValueError:
            print('Not a number')
        try:
            startdata = int(input('What row/column does the data start?'))-1
        except ValueError:
            print('Not a number')
        try:
            MinBound = int(input('The ID range from... '))-1
        except ValueError:
            print('Not a number')
        try:
            MaxBound = int(input('To... '))-1
        except ValueError:
            print('Not a number')

        self.ID = self.parseID(Col_Row, MaxBound, MinBound, SortTypePLace, rows, ID_Table, startdata)
        self.ID.append(self.quintilePlacement)
        #For debugging
        # i = 0
        # while i < len(self.ID)-1:
        #     try:
        #         print(self.ID[i].getData(), ' ', self.ID[i].getID(), ' ', self.ID[i].getSortType())
        #     except AttributeError:
        #         print(self.ID[i])
        #     i += 1

    # Function that parses data by Region ID
    def parseID(self, R_C, Max, Min, place, rowslist, Table, DataBeginIndex):
        IDDataList = []
        if(R_C == 1): # Column
            while Max > Min: 
                j = DataBeginIndex
                RangeMax = 0
                RangeMin = float(rowslist[Min][j])
                quintile = 0
                while j < len(rowslist)-1:  
                    IDDataList.append(ReferenceData(rowslist[place][Min], rowslist[j][Min], Table.getID(j,Min)))
                    RangeMax = self.rangeMaxCalc(IDDataList, RangeMax)
                    RangeMin = self.rangeMinCalc(IDDataList, RangeMin)
                    j += 1
                quintile = (float(RangeMax) - float(RangeMin))/5
                IDDataList.append(RangeMin)
                IDDataList.append(quintile) # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(IDDataList)-1)
                Min += 1
        elif(R_C == 0): # Rows
            while Max > Min:
                j = DataBeginIndex
                RangeMax = 0
                RangeMin = rowslist[Min][j]
                quintile = 0
                while j < len(rowslist[Min])-1:
                    IDDataList.append(ReferenceData(rowslist[Min][place], rowslist[Min][j], Table.getID(Min,j)))
                    l = IDDataList[len(IDDataList)-1].getData()
                    RangeMax = self.rangeMaxCalc(IDDataList, RangeMax)
                    RangeMin = self.rangeMinCalc(IDDataList, RangeMin)
                    j += 1
                quintile = (float(RangeMax) - float(RangeMin))/5
                IDDataList.append(RangeMin)
                IDDataList.append(quintile) # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(IDDataList)-1)
                Min += 1
        return IDDataList

    def getRDO(self):
        return self.ID

    def rangeMaxCalc(self, List, RangeMax):
        if float(List[len(List) - 1].getData()) > float(RangeMax):
            return float(List[len(List) - 1].getData())

    def rangeMinCalc(self, List, RangeMin):
        if List[len(List) - 1].getData() < RangeMin:
            return float(List[len(List) - 1].getData())
