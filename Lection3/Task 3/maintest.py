import json
with open("tar.json", "r", encoding="utf-8") as fileObject:
   my_dict = json.loads(fileObject.read())
   newdict = set
   for k, v in my_dict.items():
        my_dict[k] = v
        newdict.update(k,v)
        k = v
        

def dad(k):
    for k, v in newdict.items():
        newdict[k] = v
        k = v
        if k == ad:
            return k
        else: dad(k)

ad = str(input())
print(dad(ad))





