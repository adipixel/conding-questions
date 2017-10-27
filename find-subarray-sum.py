# Given an unsorted array of nonnegative integers,
# find a continous subarray which adds to a given number.

def findSubSum(arr, sums):
    start = 0
    end = 1

    if arr[0] == sums:
        return [0,0]

    curSum = arr[0]+arr[1]
    
    while end<len(arr):
        if sums == curSum:
            return [start, end]
        
        elif curSum < sums:
            end = end+1
            curSum = curSum + arr[end]
        
        elif curSum > sums:
            curSum = curSum - arr[start]    
            start = start+1
            
            if start>end:
                end = start
                curSum = arr[start]
            
    return [None]
        
    
    
        
def main():
    arr = [1, 4, 20, 3, 10, 8]
    sums = 8
    res = findSubSum(arr, sums)
    print res
main()
