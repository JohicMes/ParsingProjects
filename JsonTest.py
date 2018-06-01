import json

# RANDOM CRAP FOR TESTING PURPOSES - NOT PART OF THE PROJECT #

# x = 'I love apples'
# y = 'to eat '
# z = 7
#
# print(x.find('a' or 'l'))
#
# def insert(OGstring, index, toInsert): # Method to insert a string at any index
#         OGstring = OGstring[:index] + toInsert + OGstring[index:]
#         return OGstring
#
# x = insert(x,z,y)
# print(x)
#
# JsonFile = open('OriginalTopo.json', "r")
# JsonString = ''
# for line in JsonFile:
#         JsonString += line
# JsonFile.close()
#
# JsonString += 'YAAAAAAAS'
#
# JsonFile = open('OriginalTopo.json', "w")
# json.dump(JsonString, JsonFile)
# JsonFile.close()
#
# JsonFile = open('OriginalTopo.json', "r")
# JsonString = ''
# for line in JsonFile:
#         JsonString += line
#
# print(JsonString)
#

import json

json_input = '{"d3V4Colours": [{"name": "YlGn", "Colours": ["rgb(255, 255, 229)", "rgb(217, 240, 163)", "rgb(120, 198, 121)", "rgb(35, 132, 67)", "rgb(0, 69, 41)"]}, {"name": "YlGnBu", "Colours": ["rgb(255, 255, 217)", "rgb(199, 233, 180)", "rgb(65, 182, 196)", "rgb(34, 94, 168)", "rgb(8, 29, 88)"]}, {"name": "BuPu", "Colours": ["rgb(247, 252, 253)", "rgb(191, 211, 230)", "rgb(140, 150, 198)", "rgb(136, 65, 157)", "rgb(77, 0, 75)"]}, {"name": "PuRd", "Colours": ["rgb(247, 244, 249)", "rgb(212, 185, 218)", "rgb(223, 101, 176)", "rgb(206, 18, 86)", "rgb(103, 0, 31)"]}, {"name": "YlOrRd", "Colours": ["rgb(255, 255, 204)", "rgb(254, 217, 118)", "rgb(253, 141, 60)", "rgb(227, 26, 28)", "rgb(128, 0, 38)"]},{"name": "Purples", "Colours": ["rgb(252, 251, 253)", "rgb(218, 218, 235)", "rgb(158, 154, 200)", "rgb(106, 81, 163)", "rgb(63, 0, 125)"]},{"name": "Blues", "Colours": ["rgb(247, 251, 255)", "rgb(198, 219, 239)", "rgb(107, 174, 214)", "rgb(33, 113, 181)", "rgb(8, 48, 107)"]},{"name": "Greens", "Colours": ["rgb(247, 252, 245)", "rgb(199, 233, 192)", "rgb(116, 196, 118)", "rgb(35, 139, 69)", "rgb(0, 68, 27)"]},{"name": "Oranges", "Colours": ["rgb(255, 245, 235)", "rgb(253, 208, 162)", "rgb(253, 141, 60)", "rgb(217, 72, 1)", "rgb(127, 39, 4)"]},{"name": "Reds", "Colours": ["rgb(255, 245, 240)", "rgb(252, 187, 161)", "rgb(251, 106, 74)", "rgb(203, 24, 29)", "rgb(103, 0, 13)"]},{"name": "Greys", "Colours": ["rgb(255, 255, 255)", "rgb(217, 217, 217)", "rgb(150, 150, 150)", "rgb(82, 82, 82)", "rgb(0, 0, 0)"]},{"name": "Dark2", "Colours": ["rgb(27, 158, 119)", "rgb(117, 112, 179)", "rgb(217, 95, 2)", "rgb(102, 102, 102)", "rgb(231, 41, 138)"]},{"name": "Set1", "Colours": ["rgb(228, 26, 28)", "rgb(77, 175, 74)", "rgb(255, 127, 0)", "rgb(166, 86, 40)", "rgb(153, 153, 153)"]},{"name": "Pastel1", "Colours": ["rgb(251, 180, 174)", "rgb(204, 235, 197)", "rgb(254, 217, 166)", "rgb(229, 216, 189)", "rgb(242, 242, 242)"]},{"name": "PuRd", "Colours": ["rgb(247, 244, 249)", "rgb(212, 185, 218)", "rgb(223, 101, 176)", "rgb(206, 18, 86)", "rgb(103, 0, 31)"]}]}'


choice = 1
quinVal = 3
decoded = json.loads(json_input)

v = 0
for x in decoded['d3V4Colours']:
	if v == choice:
		l = 0
		for y in x['Colours']:
			if l == quinVal:
				print(y)
			l += 1
	v += 1

