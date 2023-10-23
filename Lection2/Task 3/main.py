number = int(input('Write your number:\n'))
lst=[]
divisor=[]
divod=0
check=1
while check< (number+1):
    divod = divod+1
    lst.insert(check, divod)
    check=check+1
check=0
while check<len(lst):
    for i in range(1, len(lst)+1):
     if (lst[check]) % i == 0:
        divisor.append(i)
    print("{}" .format(check+1),divisor,)
    divisor.clear()
    check=check+1

print("Prime numbers in your interval:")
alphad = [check for check in range(number + 1)]
alphad[1] = 0
check = 2
while check <= number:
    if alphad[check] != 0:
        jet = check + check
        while jet <= number :
            alphad[jet] = 0
            jet = jet + check
    check += 1
alphad = set(alphad)
alphad.remove(0)
print(alphad)