# Johic Mes 2018\05\07
# This class builds the array of RDO seperated by sex
from ReferenceData import ReferenceData
from DataMapper import DataMapper

class SexParser(object):
    Sex = []
    quintilePlacement = []

    #Constructor that gets the parameters form the user and then calls the function to parse the data
    def __init__(self, rows, ID_Table):
        try:
            mixed = int(input('are the sexes all mixed up in a column or row yes(1) no(0)?')) 
        except ValueError:
                print('Not a number')

        if mixed == 0:
            try:
                MaleColumn_Row = int(input('Where is the male column or row?')) - 1 # -1 because index starts at 0 but whoever enters does not know that kind of crap
            except ValueError:
                print('Not a number')
    
            try:
                FemaleColumn_Row = int(input('Where is the Female column or row?')) - 1 # -1 because index starts at 0 but whoever enters does not know that kind of crap
            except ValueError:
                print('Not a number')
    
            try:
                Other = int(input('An other section? 0 or 1'))
            except ValueError:
                print('Not 0 or 1')
    
            if Other == 1:
                OtherColumn_Row = int(input('Where is it')) - 1 # -1 because index starts at 0 but whoever enters does not know that kind of cra
            else:
                OtherColumn_Row = 0
    
            try:
                Col_Row = int(input('Is the data for the section in a column(0) or row(1)'))
            except ValueError:
                print('Not a number')
            #Function call to parse
            self.Sex = self.parseSex(Col_Row, rows, MaleColumn_Row, FemaleColumn_Row, Other, OtherColumn_Row, ID_Table) 
            self.Sex.append(self.quintilePlacement)
            
        else:
            try:
                Col_Row = int(input('Is the sex in a column(0) or row(1)'))
            except ValueError:
                print('Not a number')
            try:
                SortTypePLace = int(input('What row/column are the sex placed?'))-1
            except ValueError:
                print('Not a number')
            try:
                startdata = int(input('What row/column does the data start?'))-1
            except ValueError:
                print('Not a number')
            try:
                MinBound = int(input('The sex range from... '))-1
            except ValueError:
                print('Not a number')
            try:
                MaxBound = int(input('To... '))-1
            except ValueError:
                print('Not a number')
    
            self.Sex = self.parseSexRow(Col_Row, MaxBound, MinBound, SortTypePLace, rows, ID_Table, startdata)
            self.Sex.append(self.quintilePlacement)
            
        # Print for debuging
        # i = 0
        # while i < len(self.Sex)-1:
        #     try:
        #         print(self.Sex[i].getData(), ' ', self.Sex[i].getID(), ' ', self.Sex[i].getSortType())
        #     except AttributeError:
        #         print(self.Sex[i])
        #     i += 1

    # Function that parses data by sex and creates the ReferenceData objects.
    def parseSex(self, R_C, rowlist, M, F, OChoice, O, Table):
        sexDataList = []
        if(R_C == 0): # Does not treat the case of a worng value that is not 0 or 1!
            for x in range(0, 3):
                i = 1
                RangeMax = 0
                if x == 0:
                    RangeMin = rowlist[i][M]
                if x == 1:
                    RangeMin = rowlist[i][F]
                if x == 2:
                    RangeMin = rowlist[i][O]
                quintile = 0
                
                if OChoice == 0 and x == 2:
                    break
                while i < len(rowlist): # Cycles through the main array and build the objects
                    if x == 0:
                        sexDataList.append(ReferenceData('M', rowlist[i][M], Table.getID(i,M)))
                    if x == 1:
                        sexDataList.append(ReferenceData('F', rowlist[i][F], Table.getID(i,F)))
                    if x == 2:
                        sexDataList.append(ReferenceData('O', rowlist[i][O], Table.getID(i,O)))
                        
                    if int(sexDataList[len(sexDataList)-1].getData()) > int(RangeMax):
                        RangeMax = sexDataList[len(sexDataList)-1].getData()
                    if int(sexDataList[len(sexDataList)-1].getData()) < int(RangeMin):
                        RangeMin = sexDataList[len(sexDataList)-1].getData()
                        
                    i += 1
                quintile = (int(RangeMax) - int(RangeMin))/5
                sexDataList.append(RangeMin) # Appends the MinValue as the before last element of the list
                sexDataList.append(quintile) # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(sexDataList)-1) # Appends 

        elif(R_C == 1):
            for x in range(0, 3):
                i = 1
                RangeMax = 0
                if x == 0:
                    RangeMin = rowlist[M][i]
                if x == 1:
                    RangeMin = rowlist[F][i]
                if x == 2:
                    RangeMin = rowlist[O][i]
                quintile = 0
                if OChoice == 0 and x == 2:
                    break
                while i < len(rowlist): # Cycles through the main array and build the objects
                    if x == 0:
                        sexDataList.append(ReferenceData('M', rowlist[M][i], Table.getID(M,i)))
                    if x == 1:
                        sexDataList.append(ReferenceData('F', rowlist[F][i], Table.getID(F,i)))
                    if x == 2:
                        sexDataList.append(ReferenceData('O', rowlist[O][i], Table.getID(O,i)))

                    if int(sexDataList[len(sexDataList)-1].getData()) > int(RangeMax):
                        RangeMax = sexDataList[len(sexDataList)-1].getData()
                    if int(sexDataList[len(sexDataList)-1].getData()) < int(RangeMin):
                        RangeMin = sexDataList[len(sexDataList)-1].getData()

                    i += 1
                quintile = (int(RangeMax) - int(RangeMin))/5
                sexDataList.append(RangeMin) # Appends the MinValue as the before last element of the list
                sexDataList.append(quintile) # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(sexDataList)-1)
                
        return sexDataList


    def parseSexRow(self, R_C, Max, Min, place, rowslist, Table, DataBeginIndex):
        SexDataList = []
        if(R_C == 1): # Column
            while Max > Min: 
                j = DataBeginIndex
                RangeMax = 0
                RangeMin = float(rowslist[Min][j])
                quintile = 0
                while j < len(rowslist)-1:  
                    SexDataList.append(ReferenceData(rowslist[place][Min], rowslist[j][Min], Table.getID(j,Min)))
                    if float(SexDataList[len(SexDataList)-1].getData()) > float(RangeMax):
                        RangeMax = SexDataList[len(SexDataList)-1].getData()
                    if float(SexDataList[len(SexDataList)-1].getData()) < float(RangeMin):
                        RangeMin = SexDataList[len(SexDataList)-1].getData()
                    j += 1
                quintile = (float(RangeMax) - float(RangeMin))/5
                SexDataList.append(RangeMin)
                SexDataList.append(quintile) # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(SexDataList)-1)
                Min += 1
        elif(R_C == 0): # Rows
            while Max > Min:
                j = DataBeginIndex
                RangeMax = 0
                RangeMin = rowslist[Min][j]
                quintile = 0
                while j < len(rowslist[Min])-1:
                    SexDataList.append(ReferenceData(rowslist[Min][place], rowslist[Min][j], Table.getID(Min,j)))
                    if float(SexDataList[len(SexDataList)-1].getData()) > float(RangeMax):
                        RangeMax = SexDataList[len(SexDataList)-1].getData()
                    if float(SexDataList[len(SexDataList)-1].getData()) < float(RangeMin):
                        RangeMin = SexDataList[len(SexDataList)-1].getData()
                    j += 1
                quintile = (float(RangeMax) - float(RangeMin))/5
                SexDataList.append(RangeMin)
                SexDataList.append(quintile) # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(SexDataList)-1)
                Min += 1
        return SexDataList

    # Getter to return the array
    def getRDO(self):
        return self.Sex