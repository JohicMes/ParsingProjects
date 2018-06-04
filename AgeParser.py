# Johic Mes 2018\05\07
from ReferenceData import ReferenceData
from max_Min_Methods import rangeMaxCalc, rangeMinCalc

class AgeParser(object):
    Disease = []
    quintilePlacement = []

    def __init__(self, rows, ID_Table):
        try:
            Col_Row = int(input('Are ages seperated by columns(0) or rows(1)'))
        except ValueError:
            print('Not a number')
        try:
            MinVal = int(input('The ages range from...')) -1
        except ValueError:
            print('Not a number')
        try:
            MaxVal = int(input('To...')) -1
        except ValueError:
            print('Not a number')
        try:
            Header = int(input('Is there a header row or column? Yes(1) or No(0)'))
        except ValueError:
            print('Not a number')

        self.Age = self.parseAge(Col_Row, MaxVal, MinVal, Header, rows, ID_Table)
        self.Age.append(self.quintilePlacement)
        
        #For debugging
        #i = 0
        #while i < len(self.Age):
            #print(self.Age[i].getData(), ' ', self.Age[i].getID(), ' ', self.Age[i].getSortType())
            #i += 1
    # Function that parses data by Region ID
    def parseAge(self, R_C, Max, Min, head, rowslist, Table):
        AgeDataList = []
        DecIndex = Min # Needed to find the array value and not overrun the array
        if head == 0:
                HeaderValues = input('List ages seperated by comas: ') # verify lenght 
                HeaderList = HeaderValues.split(',')
                print(HeaderList[1])
        if R_C == 1:
            while Min < Max:
                j = 1
                RangeMax = 0
                RangeMin = rowslist[Min][j]
                quintile = 0
                while j < len(rowslist):
                    if head == 0:
                        AgeDataList.append(ReferenceData(HeaderList[Min-DecIndex], rowslist[j][Min], Table.getID(j,Min)))
                        RangeMax = rangeMaxCalc(AgeDataList, RangeMax)
                        RangeMin = rangeMinCalc(AgeDataList, RangeMin)
                    else:
                        AgeDataList.append(ReferenceData(rowslist[0][Min], rowslist[j][Min], Table.getID(j,Min)))
                        RangeMax = rangeMaxCalc(AgeDataList, RangeMax)
                        RangeMin = rangeMinCalc(AgeDataList, RangeMin)
                    j += 1
                quintile = (int(RangeMax) - int(RangeMin))/5
                AgeDataList.append(RangeMin)
                AgeDataList.append(quintile) # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(AgeDataList)-1)
                Min += 1
        elif R_C == 0:
            while Min < Max:
                j = 1
                RangeMax = 0
                RangeMin = rowslist[Min][j]
                quintile = 0
                while j < len(rowslist[Min]):
                    if head == 0:
                        AgeDataList.append(ReferenceData(HeaderList[Min-DecIndex], rowslist[Min][j], Table.getID(Min,j)))
                        RangeMax = rangeMaxCalc(AgeDataList, RangeMax)
                        RangeMin = rangeMinCalc(AgeDataList, RangeMin)
                    else:
                        AgeDataList.append(ReferenceData(rowslist[Min][0], rowslist[Min][j], Table.getID(Min,j)))
                        RangeMax = rangeMaxCalc(AgeDataList, RangeMax)
                        RangeMin = rangeMinCalc(AgeDataList, RangeMin)
                    j += 1
                quintile = (int(RangeMax) - int(RangeMin))/5
                AgeDataList.append(RangeMin)
                AgeDataList.append(quintile) # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(AgeDataList)-1)
                Min += 1
                
            return AgeDataList

    def getRDO(self):
        return self.Disease
