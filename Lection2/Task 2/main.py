User_string = input('Write your list:\n').split(" ")
i = 0
while i < len(User_string):  
    elem = User_string[i]
    if str.isnumeric(elem):
        print(elem + " - Number, index - {}".format (i))
        i+=1
    else:
        print(elem + " - It isn't number, index - {}".format (i))
        i+=1
        dead = input()