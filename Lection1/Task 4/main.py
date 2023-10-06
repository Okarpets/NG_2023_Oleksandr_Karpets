print ("Input a number a")
a = int(input())
print ("Input a number b")
b = int(input())
print ("Choose a command\n /,*,+,-")
cmd = input()
match cmd:
       case "/":
            print("Your number is {}".format(a/b))
       case "*":
            print("Your number is {}".format(a*b))
       case "+":
             print("Your number is {}".format(a+b))
       case "-":
             print("Your number is {}".format(a-b))
       case _:
            print("Command doesn't exist")
