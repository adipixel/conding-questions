def binSearch(arr, left, right, num):
	if right >= left:
		mid = left + (right-left)//2
		if arr[mid] == num:
			return "Found"
		elif num < arr[mid]:
			return binSearch(arr, num, left, mid-1)
		else:
			return binSearch(arr, num, mid+1, right)
	else:
		return "Not found"
	
	
def binarySearch(arr, begin, end, num):
    while (begin <= end):
        mid = begin + (end - begin)//2
        if (arr[mid] < num):
            begin = mid + 1
        elif (arr[mid] == num):
            return mid
        else:
            end = mid - 1

    return -1

def main():
	arr = [1,2,4,6,8,9]
	print(binSearch(arr, 0, len(arr)-1), 10)

main()
