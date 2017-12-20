def binSearch(arr, num, left, right):
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

def main():
	arr = [1,2,4,6,8,9]
	print(binSearch(arr, 10, 0, len(arr)-1))

main()
