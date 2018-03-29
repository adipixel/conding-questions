def isPalindrome(s):
	start = 0
	end = len(s)-1
	while start < end:
		if s[end] != s[start]:
			return False
		else:
			start += 1
			end -= 1

	return True

def main():
	arr = [“racecar”,”abdd”]
	for s in arr:
		print(isPalindrome(s))

main()
