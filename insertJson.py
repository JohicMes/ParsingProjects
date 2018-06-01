# Johic Mes 2018-05-24

class insertJson(object):
    jsonString = '' # Default val
    
    def __init__(self, jsonObjList, jsonfile): # Initialising method
        self.jsonString = jsonfile # The json file that has been pushed to a string allowing it to be modified and played with
        
        startPoint = 0
        while True:
            insertPoint = self.jsonString.find('UID', startPoint) # find the next potential id to insert data
            if insertPoint == -1: # if no more ID break and done
                break
            else: # if not add the data with the corresponding ID
                insertPoint = self.jsonString.find('"', insertPoint)
                IDVal = int(self.jsonString[insertPoint+3:self.jsonString.find('"', insertPoint+3)]) #In the TopoJson find the ID value that we are dealing w/
                
                i = 0
                stringToAdd = ''
                while i < len(jsonObjList): # check all the Json object generated form the data
                    try:
                        JsonID = int(jsonObjList[i][jsonObjList[i].find('ID')+3:jsonObjList[i].find('+' or '"', jsonObjList[1].find('ID')+3)]) # For every Json obj get the ID it is associated w/
                        if IDVal == JsonID: # If the two ID's match
                            stringToAdd += jsonObjList[i] # Add the json obj to the string to add at that specific place
                        i += 1
                    except ValueError:
                        i += 1
                insertPoint = self.jsonString.find(',',insertPoint) + 1 #Find where to insert after the ID in the Json file (string)
                self.jsonString = self.insert(self.jsonString, insertPoint, stringToAdd) # Use the insert function to place it in the Json file (that right now is simply a massive string)
                startPoint = insertPoint + len(stringToAdd) # update where we've already searched so we find the next ID on the next iteration 

    def insert(self, OGstring, index, toInsert): # Method to insert a string at any index
        OGstring = OGstring[:index] + '"stroke":"#000",' + '"fill":"#F34",' + toInsert + OGstring[index:] # takes the json string and plops in at the index place the string to insert
        return OGstring
    
    def getJsonFile(self): # Getter to return the final string with all the calculations done
        return self.jsonString