file1 = open(input('Write a file, what we have to open:\n'), "r")
Ulst = file1.read()
print("Char's in your file:", + len(Ulst))
lst = {}
index = 0
while index < len(Ulst):
    lst[Ulst[index]] = (Ulst.count("{}".format(Ulst[index])))
    index+=1
print("It's a value what you want to see:", + lst[input('Write a key what value you want to see:\n')])