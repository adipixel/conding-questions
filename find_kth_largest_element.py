
def findKthElement(arr, k):
    if k > len(arr) or k<1:
        return -1
    return findKthLargestElement(arr, 0, len(arr)-1, k)

def findKthLargestElement(arr, start, end, k):
    first = start
    last = end
    pivot = (first+last)//2
    
    while first <= last:
        while first<=last and arr[first] <= arr[pivot]:
            first += 1
        while last >= first and arr[last] >= arr[pivot]:
            last -= 1
        if first < last:
            arr = swap(arr, first, last)
    
    arr= swap(arr, last, pivot)

    if k == last +1:
        return arr[last]
    elif k < last+1:
        return findKthLargestElement(arr, start, last-1, k)
    else:
        return findKthLargestElement(arr, last+1, end, k)

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

def main():
    arr = [4,6,7,1,-3]
    k = 2
    kthLargest = len(arr) - k + 1
    print(findKthElement(arr, kthLargest))

main()
