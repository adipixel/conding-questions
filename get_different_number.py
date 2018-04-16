def get_different_number(arr):
  length = len(arr)
  curVal = 0
  for i in range(length):
    curVal = arr[i]
    while curVal < length and arr[curVal] != curVal:
      temp = arr[curVal]
      arr[curVal] = curVal
      curVal = temp
              
  for i in range(length):
    if i != arr[i]:
      return i
    
  return length
  
  
  
def get_different_number1(arr):
  lookup = set(arr)
  max_num = max(arr) 
  
  for i in range(max_num):
    if i not in lookup:
      return i
  
  return max_num+1
