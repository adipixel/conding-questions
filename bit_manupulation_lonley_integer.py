#!/bin/python3
#A+B ^ A = B
#A+B ^ B = A
#3 ^ 1 = 2
#3 ^ 2 = 1
#Basically if A+B, then A+B ^ B


import sys
from functools import reduce
from operator import xor

def lonely_integer(a):
    return reduce(xor, a)

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
