import math
num1 = int(input('Please write the first number:\n'))
num2 = int(input('Also the second number:\n'))
match input('Select your command\n/,*,+,-,root,power\n'):
      case "/":
            print(num1/num2)
      case"*":
            print(num1*num2)
      case"+":
            print(num1+num2)
      case "-":
            print(num1-num2)
      case "power":
            print(num1**num2)
      case "root":
            print(num1**(1/num2))