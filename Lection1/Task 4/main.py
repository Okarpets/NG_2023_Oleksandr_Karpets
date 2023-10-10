import math
print ("Wirte a your number 1")
num1 = int(input())
print ("Wirte also a number 2!")
num2 = int(input())
print ("Choose a command, who we should do\n /,*,+,-,root,power")
cmd = input()
match cmd:
       case "/":
            print("That's what you divided = {}".format(num1/num2))
       case "*":
            print("Take your multiplication and go away = {}".format(num1*num2))
       case "+":
             print("Numbers after plus = {}".format(num1+num2))
       case "-":
             print("Your minuses = {}".format(num1-num2))
       case "power":
             print("The first number is considered a number and the second is a power")
             print("Root of this numbers = {}".format(num1**num2))
       case "root":
             print("The first number - number, the second is a root")
             print("Root of this numbers = {}".format(pow(num1, (1/num2)))) 
       case _:
            print("Command doesn't exist")