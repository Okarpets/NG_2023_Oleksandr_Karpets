number = int(input("Write your interval:\n"))
lst = []
prime = []
divisor = []
divod=0
check=1
while check < (number+1):
    divod+=1
    lst.insert(check, divod)
    check+=1
check=0
while check<len(lst):
    for index in range(1, len(lst)+1): 
     if (lst[check]) % index == 0: #Looking for a number which are divided without remainder
        divisor.append(index)
    print("{}".format(check+1),divisor) 
    if int(len(divisor)) == 2: #Looking for a prime numbers
       prime.append(check+1)
    divisor.clear() #Cleaning the cycle for reuse
    check+=1
print("Prime numbers in your interval:{}".format(prime))       