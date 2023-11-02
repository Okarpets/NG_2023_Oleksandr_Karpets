import json
from jsonpath_ng import parse
jsonfile = open((input('Write what a file we should to open:\n')), "r")
jsondata = json.loads(jsonfile.read()) #Loading Json to us program
userorder = str(input('Print what key value you want to see:\n'))
userstory = [m.value for m in parse('$..{}'.format(userorder)).find(jsondata)] #Parising user order and find it on that json file
for userorder in (userstory): #Searching for a query from data collected on the basis of this JSON-FILE
    print(userorder)#Output