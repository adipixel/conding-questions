#https://www.hackerrank.com/contests/w35/challenges/3d-surface-area

#Sample Input 1
#3 3
#1 3 4
#2 2 3
#1 2 4

#Sample Output 1
#60

#!/bin/python

import sys

def surfaceArea(A, h ,w):
    # Complete this function
    area = 2*(h*w)
    for i in range(0, h):
        for j in range(0,w-1):
            area= area + abs(A[i][j]-A[i][j+1])
            
    for i in range(0, h-1):
        for j in range(0,w):
            area= area + abs(A[i][j]-A[i+1][j])

    for i in range(0, w):
        area = area + A[0][i]
        area = area + A[h-1][i]
        
    for i in range(0, h):
        area = area + A[i][0]
        area = area + A[i][w-1]
    
    return area
            
if __name__ == "__main__":
    H, W = raw_input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in xrange(H):
        A_temp = map(int,raw_input().strip().split(' '))
        A.append(A_temp)
    result = surfaceArea(A, H, W)
    print result
