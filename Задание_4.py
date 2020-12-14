def cal(coinValueSet,change,Results):
   minCoins = change
   if change in coinValueSet:
      Results[change] = 1
      return 1
   elif Results[change] > 0:
      return Results[change]
   else:
       for i in [c for c in coinValueSet if c <= change]:
         numCoins = 1 + cal(coinValueSet, change-i,
                              Results)
         if numCoins < minCoins:
            minCoins = numCoins
            Results[change] = minCoins
   return minCoins
   
def filling_set(tmp_set):
    new_variable=''
    while True:
        new_variable = input("Please enter veriable, or press enter to finish: ")
        if new_variable == '':
                return 
        tmp_set.add(int(new_variable))

   
num=int(input("Please enter sum: "))

set1=set()
filling_set(set1)

print(cal(set1,num,[0]*(num+1)))
