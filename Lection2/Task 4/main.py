import re
without = re.findall(r"[a,e,i,o,u,y]", input('Write your lst:\n').lower())
print("It's your list without consonants vowels: {}".format(without))