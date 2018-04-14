
def has_three_sum(A, t):
  A.sort()
  return any(has_two_sum(A, t-a, i) for i, a in enumerate(A))

def has_two_sum(A, t, i):
  start = 0
  end = len(A)-1
  while start < end:
    curSum = A[start] + A[end]
    if curSum == t:
      return True
    elif curSum < t:
      start += 1
    else:
      end -= 1

    if i == start:
      start += 1
    if i == end:
      end -= 1
      
  return False
        

def main():
  print(has_three_sum([11,2,5,7,3], 21))

main()
