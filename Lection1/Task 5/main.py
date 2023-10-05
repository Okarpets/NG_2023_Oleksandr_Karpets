print ("As you already know, the quadratic equation is given by the formula: ax^2+bx=c\n Specify the coefficients in the equation for calculations\n Specify the coefficient a:")
a = int(input())
print ("Specify coefficient b:")
b = int(input())
print ("Specify coefficient c:")
c = int(input())
D = (b*b)-(4*a*c)
if D < 0:
    print ("There are two roots\n х1: {}".format (-(b-pow(D, 0.5))/(2*a)))
    print ("x2: {}".format (-(b-pow(D, 0.5))/(2*a)))
elif D == 0:
    print ("There is only one root: {}".format (-(b)/(2*a)))
elif D > 0:
    print ("There are two roots\n х1: {}".format (-(b-pow(D, 0.5))/(2*a)))
    print ("x2: {}".format (-(b+pow(D, 0.5))/(2*a)))

    
