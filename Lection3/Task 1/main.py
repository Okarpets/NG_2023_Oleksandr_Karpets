file1 = open(input('Write a file, what we have to open:\n'), "r")
Ulst = file1.read()
print("Char's in your file:", + len(Ulst))
lst = {}
i = 0
while i < len(Ulst):
    lst[Ulst[i]] = (Ulst.count("{}".format(Ulst[i])))
    i = i + 1
print("It's a value what you want to see:", + lst[input('Write a key what value you want to see:\n')])