# Johic Mes 2018\05\07
# Builds the list of RDO and places them in a list
from ReferenceData import ReferenceData
from max_Min_Methods import rangeMaxCalc, rangeMinCalc


class DateParser(object):
    Date = []
    quintilePlacement = []
    
    def __init__(self, rows, ID_Table):
        try:
            Row_Col = int(input('Are the dates placed in a column(0) or row(1)?'))
        except ValueError:
            print('Not a number')
        try:
            SortTypePLace = int(input('What row/column are the dates placed?'))-1
        except ValueError:
            print('Not a number')
        try:
            MinBound = int(input('The dates range from... '))-1
        except ValueError:
            print('Not a number')
        try:
            MaxBound = int(input('To... '))
        except ValueError:
            print('Not a number')
        try:
            startdata = int(input('What row/column does the data start?')) - 1
        except ValueError:
            print('Not a number')
            
        self.Date = self.parseDate(Row_Col, MaxBound, MinBound, SortTypePLace, rows, ID_Table, startdata)
        self.Date.append(self.quintilePlacement)
        
        #For debugging
        #i = 0
        #while i < len(self.Date):
            #print(self.Date[i].getData(), ' ', self.Date[i].getID(), ' ', self.Date[i].getSortType())
            #i += 1

    # Function that parses data by Region ID
    def parseDate(self, R_C, Max, Min, place, rowslist, Table, DataBeginIndex):
        dateDataList = []
        if (R_C == 1):  # Column
            while Max > Min:
                j = DataBeginIndex
                RangeMax = 0
                RangeMin = float(rowslist[Min][j])
                quintile = 0
                while j < len(rowslist) - 1:
                    dateDataList.append(ReferenceData(rowslist[place][Min], rowslist[j][Min], Table.getID(j, Min)))
                    RangeMax = rangeMaxCalc(dateDataList, RangeMax)
                    RangeMin = rangeMinCalc(dateDataList, RangeMin)
                    j += 1
                quintile = (float(RangeMax) - float(RangeMin)) / 5
                dateDataList.append(RangeMin)
                dateDataList.append(quintile)  # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(dateDataList) - 1)
                Min += 1
        elif (R_C == 0):  # Rows
            while Max > Min:
                j = DataBeginIndex
                RangeMax = 0
                RangeMin = rowslist[Min][j]
                quintile = 0
                while j < len(rowslist[Min]) - 1:
                    dateDataList.append(ReferenceData(rowslist[Min][place], rowslist[Min][j], Table.getID(Min, j)))
                    RangeMax = rangeMaxCalc(dateDataList, RangeMax)
                    RangeMin = rangeMinCalc(dateDataList, RangeMin)
                    j += 1
                quintile = (float(RangeMax) - float(RangeMin)) / 5
                dateDataList.append(RangeMin)
                dateDataList.append(quintile)  # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(dateDataList) - 1)
                Min += 1
        return dateDataList
        
    def getRDO(self):
        return self.Date

    