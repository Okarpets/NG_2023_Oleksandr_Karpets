import math
def pr(str):
 print("You must enter two numbers, if you will chose a root or power - only one number.")
print ("Select your command\n/,*,+,-,root,power")
match input():
      case "/":
            pr(str)
            print(format(int(input())/int(input())))
      case"*":
            pr(str)
            print(format(int(input())*int(input())))
      case"+":
            pr(str)
            print("{}".format(int(input())+int(input())))
      case "-":
            pr(str)
            print("{}".format(int(input())-int(input())))
      case "power":
            pr(str)
            print(format(int(input())**2))
      case "root":
            pr(str)
            print(format(math.sqrt(int(input())))) 