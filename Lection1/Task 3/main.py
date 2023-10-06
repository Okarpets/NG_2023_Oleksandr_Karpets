print ("Select number system:")
print ("If you want to convert to Celsius, write - 1.")
print ("If you want to convert to Fahrenheit, write - 2.")
a = int(input())
print ("Okay, write down the temperature.")
b = int(input())
print ("If the temperature written was in Celsius, write - 1, if Fahrenheit - 2.")
c = int(input())
if a == 1 and c == 1:
    print ("Your temperature is{}".format (b))
if a == 2 and c == 1:
    print ("Your temperature is{}".format ((b * 9/5) + 32))
if a == 1 and c == 2:
    print ("Your temperature is{}".format ((b - 32) * 5/9))
if a == 2 and c == 2:
    print ("Your temperature is{}".format (b))