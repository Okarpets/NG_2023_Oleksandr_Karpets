lst = []
while True:
    print("Input your text")
    a = input()
    lst.append(a)
    print("{}".format(lst))
    if str.isnumeric(a) == True:
        print("You wirte a number")
    else:
        print("It isn't a number. I'm think it's a string")
    print("-"*75) 