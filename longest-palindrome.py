def lps(a):
	a = a.lower()
	palindromes = []
	for i in range(0, len(a)):
		for j in range(0, i):
			subStr = a[j:i+1]
			if subStr == subStr[::-1]:
				palindromes.append(subStr)
	return max(palindromes, key=len)

def main():
	print("Longest Palindrome: "),
	print(lps("adityaaytodssdot"))

main()
