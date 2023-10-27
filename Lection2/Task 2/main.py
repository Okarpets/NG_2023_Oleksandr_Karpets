User_string = input('Write your list:\n').split(" ")
i = 0
while i < len(User_string):  
    if str.isnumeric(User_string[i]):
        print(User_string[i] + " - Number, index - {}".format (i))
        i+=1
    else:
        print(User_string[i] + " - It isn't number, index - {}".format (i))
        i+=1