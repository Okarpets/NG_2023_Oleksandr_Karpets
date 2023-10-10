print ("If you want to convert from Fahrenheit to Celsius, write 1.\n Otherwise - 2.")
syst = int(input())
print ("Okay, write down the temperature.")
temp = int(input())
if syst == 1:
    print ("Your Celsius = {}".format ((temp * 9/5) + 32))
if syst == 2:
    print ("Your Fahrenheitius temperatorius = {}".format ((temp - 32) * 5/9))
else:
    print ("You wrote something worse, guy...")