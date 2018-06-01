# Johic Mes 2018\05\07
from ReferenceData import ReferenceData
from JsonObjBuilder import JsonObjBuilder
from MatchArraySort import MatchArraySort
from tqdm import tqdm

class JsonObjListGenerator(object):
    jsonObjects = []
    def __init__(self, parsedDatardo_List, biggestIDSize):
        #print('in JsonObjListGenerator')
        #print(len(ParsedDatardo_List[0]))
        self.jsonObjects = self.Create(parsedDatardo_List, biggestIDSize)

    def Create(self, rdo_List, biggestIDSize): # Alright here we go... if you haven't written this GLHF :)
        finaList = []
        jObj = [[] for unitoftimeandlenghtoflifethatdoesthings in range(biggestIDSize)]
        searchedIDs = []
        i = 0
        #print('Made it to CREATE')
        
        while i < len(rdo_List): # Cycle through the different RDO lists
            j = 0
            #print('In first loop portion!')
            #while j < (len(rdo_List[i]) - 2): # Cycles through an entire list: -2 because there's the data type int at the end of the list + the rdo_List of quintiles
            for j in tqdm(range(len(rdo_List[i]) - 2)):
                if (j not in rdo_List[i][len(rdo_List[i])-2]) and ((j+1) not in rdo_List[i][len(rdo_List[i])-2]): # If we reach a quintile value we skip it
                    RGB = 1
                    jObj[rdo_List[i][j].getID()].append(rdo_List[i][j]) # Appends RDO
                    jObj[rdo_List[i][j].getID()].append(rdo_List[i][len(rdo_List[i])-1]) # Appends data type

                    if len(rdo_List) == 2 and i > 0:  # If only ID and one other sort type and not sorting ID's
                        # print('Quintile TIME!')
                        # Get Quintile pos and append value + min value to Matchrdo_List
                        z = 0
                        while z < len(rdo_List[i][len(rdo_List[i]) - 2]):  # Find the right quintile to append by referencing the quintile position rdo_List
                            # print((rdo_List[k][len(rdo_List[k])-2][z])-1)
                            # print(l)
                            if float((rdo_List[i][len(rdo_List[i]) - 2][z]) - 1) > j:
                                jObj[rdo_List[i][j].getID()].append(rdo_List[i][(rdo_List[i][len(rdo_List[i]) - 2][z])])  # Appends quintile
                                # print('Min Value + Quintile')
                                # print(Matchrdo_List[len(Matchrdo_List)-1])
                                jObj[rdo_List[i][j].getID()].append(rdo_List[i][(rdo_List[i][len(rdo_List[i]) - 2][z]) - 1])  # Appends min value
                                # print(Matchrdo_List[len(Matchrdo_List)-1])
                                break
                            z += 1
                    else:
                        RGB = 0

                j += 1
            i += 1
        
        #if len(rdo_List) > 2: Need to build
            #obj = MatchArraySort(jObj).getFinalBuild()
                
        finaList = JsonObjBuilder(jObj, RGB).getObj() # Call to get the complete objects list

        return finaList

    def GetJsonObj(self):
        return self.jsonObjects