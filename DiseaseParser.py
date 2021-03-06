# Johic Mes 2018\05\07
from ReferenceData import ReferenceData
from DataMapper import DataMapper
import csv

class DiseaseParser(object):
    Disease = []
    quintilePlacement = []

    def __init__(self, rows, ID_Table):
        try:
            Col_Row = int(input('Are the disease seperated by columns(0) or rows(1)'))
        except ValueError:
            print('Not a number')
        try:
            MinVal = int(input('The diseases range from...')) - 1
        except ValueError:
            print('Not a number')
        try:
            MaxVal = int(input('To...')) - 1 
        except ValueError:
            print('Not a number')
        try:
            lenght = int(input('the lenght of the disease column/row is?')) - 1 
        except ValueError:
            print('Not a number')
        try:
            Header = int(input('Is there a header row or column? Yes(1) or No(0)'))
        except ValueError:
            print('Not a number')

        self.Disease = self.parseDisease(Col_Row, MaxVal, MinVal, Header, rows, ID_Table, lenght)
        self.Disease.append(self.quintilePlacement)
        #For debugging
        # i = 0
        # while i < len(self.Disease)-1:
        #     try:
        #         print(self.Disease[i].getData(), ' ', self.Disease[i].getID(), ' ', self.Disease[i].getSortType())
        #     except AttributeError:
        #         print(self.Disease[i])
        #     i += 1
            
    # Function that parses data by Disease
    def parseDisease(self, R_C, Max, Min, head, rowslist, Table, l):
        DiseaseDataList = []
        DecIndex = Min # Needed to find the array value and not overrun the array
        if head == 0:
                HeaderValues = input('List Diseases seperated by comas: ') # verify lenght 
                HeaderList = HeaderValues.split(',')
                print(HeaderList[1])
        if R_C == 0:
            while Min <= Max:
                j = 1
                RangeMax = 0
                RangeMin = rowslist[Min][j]
                quintile = 0
                while j < l:
                    if head == 0:
                        DiseaseDataList.append(ReferenceData(HeaderList[Min-DecIndex], rowslist[j][Min], Table.getID(j,Min)))
                        if float(DiseaseDataList[len(DiseaseDataList)-1].getData()) > float(RangeMax):
                            RangeMax = DiseaseDataList[len(DiseaseDataList)-1].getData()
                        if float(DiseaseDataList[len(DiseaseDataList)-1].getData()) < float(RangeMin):
                            RangeMin = DiseaseDataList[len(DiseaseDataList)-1].getData()
                    else:
                        DiseaseDataList.append(ReferenceData(rowslist[0][Min], rowslist[j][Min], Table.getID(j,Min)))
                        if float(DiseaseDataList[len(DiseaseDataList)-1].getData()) > float(RangeMax):
                            RangeMax = DiseaseDataList[len(DiseaseDataList)-1].getData()
                        if float(DiseaseDataList[len(DiseaseDataList)-1].getData()) < float(RangeMin):
                            RangeMin = DiseaseDataList[len(DiseaseDataList)-1].getData()
                    j += 1
                quintile = (float(RangeMax) - float(RangeMin))/5
                DiseaseDataList.append(RangeMin)
                DiseaseDataList.append(quintile) # Appends the quintile as the last element of the list
                # Debug
                #print(quintile)
                #print(RangeMin)
                self.quintilePlacement.append(len(DiseaseDataList)-1)
                Min += 1
        elif R_C == 1:
            while Min <= Max:
                j = 1
                RangeMax = 0
                RangeMin = rowslist[Min][j]
                quintile = 0
                while j < l:
                    if head == 0:
                        DiseaseDataList.append(ReferenceData(HeaderList[Min-DecIndex], rowslist[Min][j], Table.getID(Min,j)))
                        if float(DiseaseDataList[len(DiseaseDataList)-1].getData()) > float(RangeMax):
                            RangeMax = DiseaseDataList[len(DiseaseDataList)-1].getData()
                        if float(DiseaseDataList[len(DiseaseDataList)-1].getData()) < float(RangeMin):
                            RangeMin = DiseaseDataList[len(DiseaseDataList)-1].getData()
                    else:
                        DiseaseDataList.append(ReferenceData(rowslist[Min][0], rowslist[Min][j], Table.getID(Min,j)))
                        if float(DiseaseDataList[len(DiseaseDataList)-1].getData()) > float(RangeMax):
                            RangeMax = float(DiseaseDataList[len(DiseaseDataList)-1].getData())
                        if DiseaseDataList[len(DiseaseDataList)-1].getData() < RangeMin:
                            RangeMin = float(DiseaseDataList[len(DiseaseDataList)-1].getData())
                    j += 1
                quintile = (float(RangeMax) - float(RangeMin))/5
                # Debug
                #print(quintile)
                #print(RangeMin)
                DiseaseDataList.append(RangeMin)
                DiseaseDataList.append(quintile)# Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(DiseaseDataList)-1)
                Min += 1
        return DiseaseDataList

    def getRDO(self):
        return self.Disease
