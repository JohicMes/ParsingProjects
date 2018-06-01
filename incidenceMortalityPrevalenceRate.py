from ReferenceData import ReferenceData

class incidenceMortalityPrevalenceRate(object):
    Rates = []
    quintilePlacement = []

    # Constructor that gets the parameters form the user and then calls the function to parse the data
    def __init__(self, rows, ID_Table):

            try:
                incidence = int(input('Where is the incidence column or row?')) - 1  # -1 because index starts at 0 but whoever enters does not know that kind of crap
            except ValueError:
                print('Not a number')

            try:
                mortality = int(input('Where is the mortality column or row?')) - 1  # -1 because index starts at 0 but whoever enters does not know that kind of crap
            except ValueError:
                print('Not a number')

            try:
                prevalence = int(input('Where is the prevalence column or row?'))-1
            except ValueError:
                print('Not a number')
            try:
                Col_Row = int(input('Is the data for the section in a column(0) or row(1)'))
            except ValueError:
                print('Not a number')

            # Function call to parse
            self.Rates = self.parseRates(Col_Row, rows, incidence , mortality, prevalence, ID_Table)
            self.Rates.append(self.quintilePlacement)

            # Print for debuging
            #i = 0
            #while i < len(self.Rates)-1:
                #try:
                   # print(self.Rates[i].getData(), ' ', self.Sex[i].getID(), ' ', self.Sex[i].getSortType())
                #except AttributeError:
                    #print(self.Rates[i])
                #i += 1

    def parseRates(self, R_C, rowlist, inci, mort, prev, Table):
        rateDataList = []
        if (R_C == 0):  # Does not treat the case of a wrong value that is not 0 or 1!
            for x in range(0, 3):
                i = 1
                RangeMax = 0
                if x == 0:
                    RangeMin = rowlist[i][inci]
                if x == 1:
                    RangeMin = rowlist[i][mort]
                if x == 2:
                    RangeMin = rowlist[i][prev]
                quintile = 0

                while i < len(rowlist):  # Cycles through the main array and build the objects
                    try:
                        if x == 0:
                            rateDataList.append(ReferenceData('Incidence', rowlist[i][inci], Table.getID(i, inci)))
                        if x == 1:
                            rateDataList.append(ReferenceData('Mortality', rowlist[i][mort], Table.getID(i, mort)))
                        if x == 2:
                            rateDataList.append(ReferenceData('Prevalence', rowlist[i][prev], Table.getID(i, prev)))

                        print(rateDataList[len(rateDataList) - 1].getData())
                        if float(rateDataList[len(rateDataList) - 1].getData()) > float(RangeMax):
                            RangeMax = rateDataList[len(rateDataList) - 1].getData()
                        if float(rateDataList[len(rateDataList) - 1].getData()) < float(RangeMin):
                            RangeMin = rateDataList[len(rateDataList) - 1].getData()
                        i += 1
                    except ValueError:
                        rateDataList.pop()
                        print("break")
                        break

                quintile = (float(RangeMax) - float(RangeMin)) / 5
                rateDataList.append(RangeMin)  # Appends the MinValue as the before last element of the list
                rateDataList.append(quintile)  # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(rateDataList) - 1)  # Appends

        elif (R_C == 1):
            for x in range(0, 3):
                i = 1
                RangeMax = 0
                if x == 0:
                    RangeMin = rowlist[inci][i]
                if x == 1:
                    RangeMin = rowlist[mort][i]
                if x == 2:
                    RangeMin = rowlist[prev][i]
                quintile = 0

                while i < len(rowlist)-1:  # Cycles through the main array and build the objects
                    try:
                        if x == 0:
                            rateDataList.append(ReferenceData('Incidence', rowlist[inci][i], Table.getID(inci, i)))
                        if x == 1:
                            rateDataList.append(ReferenceData('Mortality', rowlist[mort][i], Table.getID(mort, i)))
                        if x == 2:
                            rateDataList.append(ReferenceData('Prevalence', rowlist[prev][i], Table.getID(prev, i)))

                        if float(rateDataList[len(rateDataList) - 1].getData()) > float(RangeMax):
                            RangeMax = rateDataList[len(rateDataList) - 1].getData()
                        if float(rateDataList[len(rateDataList) - 1].getData()) < float(RangeMin):
                            RangeMin = rateDataList[len(rateDataList) - 1].getData()
                        i += 1
                    except ValueError:
                        rateDataList.pop()
                        print("break")
                        break

                quintile = (float(RangeMax) - float(RangeMin)) / 5
                rateDataList.append(RangeMin)  # Appends the MinValue as the before last element of the list
                rateDataList.append(quintile)  # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(rateDataList) - 1)

        return rateDataList

    def getRDO(self):
        return self.Rates

