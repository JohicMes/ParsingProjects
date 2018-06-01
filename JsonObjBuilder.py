# Johic Mes 2018\05\07
from ReferenceData import ReferenceData
import json

class JsonObjBuilder(object):
    OneJsonObject = '' # Default value
    
    def __init__(self, MatchData, colourTag):
        self.OneJsonObject = self.CreateDataTags(MatchData, colourTag)

    def CreateDataTags(self, M, colourTag):

        print("Pick your color theme!")

        #json_input = '{"d3V4Colours":[{"name":"YlGn","Colours":["rgb(255,255,229)","rgb(217,240,163)","rgb(120,198,121)","rgb(35,132,67)","rgb(0,69,41)"]},{"name":"YlGnBu","Colours":["rgb(255,255,217)","rgb(199,233,180)","rgb(65,182,196)","rgb(34,94,168)","rgb(8,29,88)"]},{"name":"BuPu","Colours":["rgb(247,252,253)","rgb(191,211,230)","rgb(140,150,198)","rgb(136,65,157)","rgb(77,0,75)"]},{"name":"PuRd","Colours":["rgb(247,244,249)","rgb(212,185,218)","rgb(223,101,176)","rgb(206,18,86)","rgb(103,0,31)"]},{"name":"YlOrRd","Colours":["rgb(255,255,204)","rgb(254,217,118)","rgb(253,141,60)","rgb(227,26,28)","rgb(128,0,38)"]},{"name":"Purples","Colours":["rgb(252,251,253)","rgb(218,218,235)","rgb(158,154,200)","rgb(106,81,163)","rgb(63,0,125)"]},{"name":"Blues","Colours":["rgb(247,251,255)","rgb(198,219,239)","rgb(107,174,214)","rgb(33,113,181)","rgb(8,48,107)"]},{"name":"Greens","Colours":["rgb(247,252,245)","rgb(199,233,192)","rgb(116,196,118)","rgb(35,139,69)","rgb(0,68,27)"]},{"name":"Oranges","Colours":["rgb(255,245,235)","rgb(253,208,162)","rgb(253,141,60)","rgb(217,72,1)","rgb(127,39,4)"]},{"name":"Reds","Colours":["rgb(255,245,240)","rgb(252,187,161)","rgb(251,106,74)","rgb(203,24,29)","rgb(103,0,13)"]},{"name":"Greys","Colours":["rgb(255,255,255)","rgb(217,217,217)","rgb(150,150,150)","rgb(82,82,82)","rgb(0,0,0)"]},{"name":"Dark2","Colours":["rgb(27,158,119)","rgb(117,112,179)","rgb(217,95,2)","rgb(102,102,102)","rgb(231,41,138)"]},{"name":"Set1","Colours":["rgb(228,26,28)","rgb(77,175,74)","rgb(255,127,0)","rgb(166,86,40)","rgb(153,153,153)"]},{"name":"Pastel1","Colours":["rgb(251,180,174)","rgb(204,235,197)","rgb(254,217,166)","rgb(229,216,189)","rgb(242,242,242)"]},{"name":"PuRd","Colours":["rgb(247,244,249)","rgb(212,185,218)","rgb(223,101,176)","rgb(206,18,86)","rgb(103,0,31)"]}]}'

        JsonFile = open('d3Colours.json', "r")
        json_input = ''
        for line in JsonFile:
            json_input += line

        try:
            decoded = json.loads(json_input)  # Access data
            z = 1
            for x in decoded['d3V4Colours']:
                print(str(z) + ":" + x['name'])
                z += 1
        except (ValueError, KeyError, TypeError):
            print("JSON format error")

        try:
            colourChoice = int(input('Your pick is... (please insert number)')) - 1  # Captures choice of colours
        except ValueError:
            print('Not a number')



        j = 0
        DataTagList = []

        while j < len(M):
            tagSection = ''
            tagColour = ''
            i = 0
            if M[j] != []:
                while i < len(M[j])- (2 * colourTag): #-2 because quintile plus min are at the tail of the method. (Only if they are present multiplication!)
                    if M[j][i+1] == 1: #Age -> age-STRING
                        tagSection += ('+age-' + M[j][i].getSortType())
                    if M[j][i+1] == 2: #Sex -> sex-M\F\O
                        tagSection += ('+sex-' + M[j][i].getSortType())
                    if M[j][i+1] == 3: #Disease -> date-STRING
                        tagSection += ('+d-' + M[j][i].getSortType())
                    if M[j][i+1] == 4: #Date -> d-DISEASE_TYPE
                        tagSection += ('+date-' + M[j][i].getSortType())
                    if M[j][i+1] == 5: #ID -> ID-IDVALUE
                        tagSection += ('+ID-' + M[j][i].getSortType())
                    if M[j][i+1] == 6: #ID -> rate
                        tagSection += ('+rate-' + M[j][i].getSortType())
                    i += 2

                tagSection = tagSection[1:]
                if colourTag == 1: # TEMPORARY only find the quintile colours when easy case
                    tagColour = self.CreateColourTags(M[j], decoded, colourChoice) # Finds the colour according to the quintile
                    quintiletag = '"data-fill-' + tagSection + '":"' + tagColour + '",'  # Build the obj w/ the quintile
                    DataTagList.append(quintiletag)
                    # Append to DataTagList the quintile Json obj
                  # remove the first '+' of the string
                final = '"' + tagSection + '":' + M[j][0].getData() + ',' # build the obj w/ the data
                DataTagList.append(final)  # Append to DataTagList the Data Json obj
                j += 1
            else:
                j += 1

        return DataTagList

    def CreateColourTags(self, matcharray, decoded, colourChoice): # Returns a colour tag depending on the quintile that it belongs to


        colourCode = '' # Colour code defualt value
        quintiles = []
        try:
            for x in range(0, 5): # Deals the quartiles and places them in an array
                quintiles.append(float(matcharray[len(matcharray)-1]) + (float(matcharray[len(matcharray)-2])) * x)
        except TypeError:
            return 'Broken MatchArray' # if something is screwed retrn the error message 

        data = float(matcharray[0].getData()) # Depending on the quintile returns a RGB string value
        if (quintiles[0] <= data) and (quintiles[1] > data):
            colourCode = self.getQuintileColour(decoded, 0, colourChoice)
        if quintiles[1] <= data and quintiles[2] > data:
            colourCode = self.getQuintileColour(decoded, 1, colourChoice)
        if quintiles[2] <= data and quintiles[3] > data:
            colourCode = self.getQuintileColour(decoded, 2, colourChoice)
        if quintiles[3] <= data and quintiles[4] > data:
            colourCode = self.getQuintileColour(decoded, 3, colourChoice)
        if quintiles[4] <= data:
            colourCode = self.getQuintileColour(decoded, 4, colourChoice)

        return colourCode

    def getObj(self): # Getter method to send the list of Json objects
        return self.OneJsonObject

    def getQuintileColour(self, json, quinVal, choice):
        v = 0
        for x in json['d3V4Colours']:
            if v == choice:
                l = 0
                for y in x['Colours']:
                    if l == quinVal:
                        return y
                    l += 1
            v += 1