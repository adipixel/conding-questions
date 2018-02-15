def bs(arr, left, right):
  while(right>=left):
    if right == left:
      if arr[right-1] == arr[right]-1:
        return right + 1
      else:
        return right
      
    mid = left + (right-left)//2
    
    if arr[mid] == mid:
      left = mid + 1
    else:
      right = mid - 1
      
      





arr = [0,1,2,3,4,5,6,7,8,9]

print bs(arr, 0, len(arr)-1)
