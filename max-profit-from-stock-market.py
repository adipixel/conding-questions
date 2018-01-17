def main():
  arr = [10, 7, -3, -10, 4, 2, 8, -2, 4, -5, -2]
  print getMaxBenifit(arr)
  
def getMaxBenifit(arr):
  global_sum = 0
  cur_sum = 0
  for x in arr:
    
    if cur_sum+x > x:
      cur_sum += x
    else:
      cur_sum = x
    
    if cur_sum > global_sum:
      global_sum = cur_sum
  
  return global_sum
  
main()
