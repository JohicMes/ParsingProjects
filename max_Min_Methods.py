#Johic Mes 04/06/2018
#These methods return a new max value if its bigger than the current max value
from ReferenceData import ReferenceData #Hmmmm interesting!

def rangeMaxCalc(DiseaseDataList, RangeMax): # Method for the max value
    if float(DiseaseDataList[len(DiseaseDataList) - 1].getData()) > float(RangeMax): # is the element just appended to the list bigger than the max val?
        return float(DiseaseDataList[len(DiseaseDataList) - 1].getData()) #  yes -> return new Max value
    else: # No
        return RangeMax # Return same old value (not really necessary but just to be safe)

def rangeMinCalc(DiseaseDataList, RangeMin): # method for the min value
    if DiseaseDataList[len(DiseaseDataList) - 1].getData() < RangeMin:  # is the element just appended to the list bigger than the min val?
        return float(DiseaseDataList[len(DiseaseDataList) - 1].getData()) # return new min value
    else: # No
        return RangeMin # Return same old value (not really necessary but just to be safe)