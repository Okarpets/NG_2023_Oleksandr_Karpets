n = int(input('Write your interval:\n'))
print("Just list of number:")
check = 0
for i in range(n):
  check = check + 1
  if n % check == 0:
    print(check, check)
  else:
     print(check, "-")


print("Prime numbers in your interval:")
a = [check for check in range(n + 1)]
a[1] = 0
check = 2
while check <= n:
    if a[check] != 0:
        j = check + check
        while j <= n :
            a[j] = 0
            j = j + check
    check += 1
a = set(a)
a.remove(0)
print(a)