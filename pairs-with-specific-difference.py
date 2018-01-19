def find_pairs_with_given_difference(arr, k):
  return [[x, x-k] for x in set(arr) if x-k in set(arr)]  
