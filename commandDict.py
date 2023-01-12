import json

def init():
    jsonFile = open('commandJson.json','w')
    



jsonFile = open('commandJson.json','r')

cmdDict = json.loads(jsonFile.read())




print(cmdDict)