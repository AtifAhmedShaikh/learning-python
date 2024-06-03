# "r" Reed default value. open a file for reading and if file not exists then this throw error
# "w" only open a file for wrinting create if not exists then create one
# "a" Append open a file for wrinting and append given content to a file, if file not exists then create new one
# "x" Creates the specified file, returns an error if the file already exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

import json


myFile = open("example.txt")  # default "rt"
myJsonFile = open("example.json")  # default "rt"
jsonData = json.load(myJsonFile)
# print(myFile.read())  # print the file content e.g hello example file
print(myJsonFile.read())  # print the file content e.g hello example file
