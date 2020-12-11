def check(num):
    while(num % 2 == 0):
        num = num / 2
    while(num % 3 == 0):
        num = num / 3
    while(num % 5 == 0):
        num = num / 5
    return num



n =int(input("введите число: "))
cal=1
i=1
while (cal<n):
    i=i+1
    if (check(i)==1):
        cal+=1
print(i)

