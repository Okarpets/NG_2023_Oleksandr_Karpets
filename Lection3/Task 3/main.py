import json
from jsonpath_ng import parse
file = open((input('Write what a file we should to open:\n')), "r")
order = str(input('Print what key value you want to see:\n'))
result = [m.value for m in parse('$..{}'.format(order)).find(json.loads(file.read()))]#Parising user order and find it on that json file
for order in (result):
    print(result)