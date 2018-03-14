def isXOfaKind(arr):
  if len(arr)<1:
    return False

  hm = dict()
  for x in arr:
    if x in hm:
      hm[x] += 1
    else:
      hm[x] = 1
  for x in hm:
    if hm[x] < 2:
      return False
  return True


def main():
  arr= [3, 5,3,5,3,3, 1]
  print(isXOfaKind(arr))
main()
