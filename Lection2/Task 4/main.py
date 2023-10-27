import re
without = re.findall(r"[A,a,E,e,I,i,O,o,U,u,Y,y]", input('Write your lst:\n'))
print("It's your list without consonants vowels: {}".format(without))