from ReferenceData import ReferenceData
from max_Min_Methods import rangeMaxCalc, rangeMinCalc, quintileCalc

class incidenceMortalityPrevalenceRate(object):
    Rates = [] # Array of RDO
    quintilePlacement = [] # Array of placement of quintiles in Rates[]

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
            for x in range(0, 3): # Loops through the three types of datatypes to sort
                i = 1
                RangeMax = 0
                try:
                    if x == 0: # If 0 we treat incidence
                        RangeMin = rowlist[i][inci]
                        while i < len(rowlist):  # Cycles through the main array and build the objects
                            rateDataList.append(ReferenceData('Incidence', rowlist[i][inci], Table.getID(i, inci)))
                            i += 1
                    if x == 1: # If 1 we treat mortality
                        RangeMin = rowlist[i][mort]
                        while i < len(rowlist): # Cycles through the main array and build the objects
                            rateDataList.append(ReferenceData('Mortality', rowlist[i][mort], Table.getID(i, mort)))
                            i += 1
                    if x == 2: # If 2 we treat prevalence
                        RangeMin = rowlist[i][prev]
                        while i < len(rowlist): # Cycles through the main array and build the objects
                            rateDataList.append(ReferenceData('Prevalence', rowlist[i][prev], Table.getID(i, prev)))
                            i += 1

                    #print(rateDataList[len(rateDataList) - 1].getData())
                    RangeMax = rangeMaxCalc(rateDataList, RangeMax)
                    RangeMin = rangeMinCalc(rateDataList, RangeMin)

                except ValueError:
                    rateDataList.pop()
                    # Somehow python appends an empty value at the end of the array
                    # when we overrun the data into empty cells of the CSV
                    # so we just pop that crap out of the stratosphere
                    # print("break")
                    break # Break out of loop because we have gone to far in teh CSV

                quintile = quintileCalc(RangeMax, RangeMin)
                rateDataList.append(RangeMin)  # Appends the MinValue as the before last element of the list
                rateDataList.append(quintile)  # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(rateDataList) - 1)  # Appends the placement of the quintiles in the main array containing the DRO's
                # Will be necessary to navigate the array efficiently

        elif (R_C == 1): # This method works exactly the same way as above but inverts the column and rows while parsing.
            for x in range(0, 3):  # Loops through the three types of datatypes to sort
                i = 1
                RangeMax = 0
                try:
                    if x == 0:  # If 0 we treat incidence
                        RangeMin = rowlist[inci][i]
                        while i < len(rowlist):  # Cycles through the main array and build the objects
                            rateDataList.append(ReferenceData('Incidence', rowlist[inci][i], Table.getID(inci, i)))
                            i += 1
                    if x == 1:  # If 1 we treat mortality
                        RangeMin = rowlist[mort][i]
                        while i < len(rowlist):  # Cycles through the main array and build the objects
                            rateDataList.append(ReferenceData('Mortality', rowlist[mort][i], Table.getID(mort, i)))
                            i += 1
                    if x == 2:  # If 2 we treat prevalence
                        RangeMin = rowlist[prev][i]
                        while i < len(rowlist):  # Cycles through the main array and build the objects
                            rateDataList.append(ReferenceData('Prevalence', rowlist[prev][i], Table.getID(prev, i)))
                            i += 1

                    RangeMax = rangeMaxCalc(rateDataList, RangeMax)
                    RangeMin = rangeMinCalc(rateDataList, RangeMin)

                except ValueError:
                    rateDataList.pop()
                    print("break")
                    break

                quintile = quintileCalc(RangeMax, RangeMin)
                rateDataList.append(RangeMin)  # Appends the MinValue as the before last element of the list
                rateDataList.append(quintile)  # Appends the quintile as the last element of the list
                self.quintilePlacement.append(len(rateDataList) - 1)

        return rateDataList # Returns the list with the the newly created DRO's
        #  At the end is the min val quintile value and

    def getRDO(self):
        return self.Rates # Returns the rates array built previously in the constructor
