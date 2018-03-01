# given 3 coins (1,3,5) 
# find the minimum number of coins required to make N dollars
# For N = 19, result: 5

def getMinCoins(total):
  curTotal = 0
  coins = [1,3,5]
  count = 0
  while total != curTotal:
    for x in reversed(coins):
      if total - curTotal >= x:
        curTotal += x
        count +=1
        break
  return count
  
  
  
print getMinCoins(3)
