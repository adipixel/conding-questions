def index_equals_value_search(arr):
  start = 0
  end = len(arr)-1
  result = -1
  while start <= end:
    mid = start+(end-start//2)
    if mid == arr[mid]:
      if mid < result or result == -1:
        result = mid
      end = mid - 1 
    elif mid > arr[mid]:
      start = mid + 1
    else:
      end = mid - 1
      
  return result
