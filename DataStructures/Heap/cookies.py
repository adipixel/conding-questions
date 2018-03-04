#https://www.hackerrank.com/challenges/jesse-and-cookies/problem

from heapq import heapify, heappush, heappop, heapreplace

n, sweet = 0, 0
[n, sweet] = [int(x) for x in input().split()]

cookies = [int(x) for x in input().split()]
heapify(cookies)
res = 0
printFlag = True
while cookies[0] < sweet:
    if len(cookies) > 1:
        newCookie = heappop(cookies) + (heappop(cookies)*2)
        heappush(cookies, newCookie)
        res += 1
    else:
        printFlag = False
        break
if printFlag:
    print(res)
else:
    print(-1)
