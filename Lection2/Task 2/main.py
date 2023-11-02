User_string = input('Write your list:\n').split(" ")
index = 0
while index < len(User_string):  
    if str.isnumeric(User_string[index]):
        print(User_string[index] + " - Number, index - {}".format (index))
        index+=1
    else:
        print(User_string[index] + " - It isn't number, index - {}".format (index))
        index+=1