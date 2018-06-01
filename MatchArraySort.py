from JsonObjBuilder import JsonObjBuilder
from tqdm import tqdm
from ReferenceData import ReferenceData

class MatchArraySort(object):
    mlist = []
    def __init__(self, mlist):
        self.mlist = self.quintileFinder(mlist)

    def quintileFinder(self, matches):
        matchFound = [] # Array of already treated MatchArray

        i = 0
        for i in tqdm(range(len(matches))): # Goes through the entire list
            if matches[i] != [] and i not in matchFound: # if the lust of Sorted ID's is not an empty cell and is not already sorted
                #Find matching Match Arrays
                x = 0


        return matches
    
    def getFinalBuild(self):
        return self.mlist