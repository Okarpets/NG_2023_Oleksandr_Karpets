import json
from jsonpath_ng import parse
jsonfile = open(str(input('Write what a file we should to open:\n')), "r")
json_data = json.loads(jsonfile.read()) #Loading Json to us program
userorder = str(input('Print what key value you want to see:\n'))
userstory = [m.value for m in parse('$..{}'.format(userorder)).find(json_data)] #Parising user order and find it on that json file
for userorder in (zip(userstory)): #Searching for a query from data collected on the basis of this JSON-FILE
    print(userorder)#Output