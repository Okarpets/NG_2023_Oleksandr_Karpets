print ("If you want get a Celsius, write - 1.\n If Fahrenheit already you must get 2.")
syst = int(input())
print ("Okay, write down the temperature.")
temp = int(input())
print ("If the temperature written was in Celsius, write - 1, if Fahrenheit - 2.")
whatsys= int(input())
if whatsys == 2 and syst == 1:
    print ("Your Celsius = {}".format ((temp * 9/5) + 32))
if whatsys == 1 and syst == 2:
    print ("Your Fahrenheitius temperatorius = {}".format ((temp - 32) * 5/9))
else:
    print ("You wirte a worst something, guy...")