# Given an unsorted array of nonnegative integers,
# find a continous longest subarray which adds to a given number or fever than it.

def findSubSum(arr, sums):
    start = 0
    end = 1

    if arr[0] == sums:
        return [0,0]

    curSum = arr[0]+arr[1]
    
    tempSum = 0
    tempLen = 2
    tempRes = [0,1,2]
    
    tempResult = None
    
    while end<len(arr):
#        if sums == curSum:
#            tempLen = end-start+1
#            tempRes = [start, end, tempLen]
#            break
          
        if curSum <= sums:
            if end+1 >= len(arr):
              return tempRes
            end = end+1
            curSum = curSum + arr[end]
            if tempLen<end-start+1 and curSum <= sums:
              tempLen = end-start+1
              tempRes = [start, end, tempLen]
        
        elif curSum > sums:
            curSum = curSum - arr[start]    
            start = start+1
            
            if start>end:
                end = start
                curSum = arr[start]
            
    return tempRes[2]
        
    
    
        
def main():
    arr = [74, 659, 931, 273, 545, 879, 924, 710, 441, 166, 493, 43, 988, 504, 328, 730, 841, 613, 304, 170, 710, 158, 561, 934, 100, 279, 817, 336, 98, 827, 513, 268, 811, 634, 980, 150, 580, 822, 968, 673, 394, 337, 486, 746, 229, 92, 195, 358, 2, 154, 709, 945, 669, 491, 125, 197, 531, 904, 723, 667, 550]
    sums = 22337
    arr1 = [1,2,3]
    sums1 = 3
    #res = findSubSum(arr, sums)
    res = findSubSum(arr1, sums1)
    print res
main()
