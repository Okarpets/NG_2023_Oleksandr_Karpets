print ("Please, write your temperature:")
temp = int(input())
print ("If you want to convert from Fahrenheit to Celsius, write C. Otherwise - F.")
match input():
       case "C":
            print("That's your temp. = {} (C)".format((temp-32)*5/9))
       case "F":
            print("That's your temp. = {} (F)".format((temp*9/5)+32))