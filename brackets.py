#https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

#time: O(n)
from sets import Set
def is_matched(expression):
    stack = []
    lenExp = len(expression)
    for x in expression:
        if x == '{':
            stack.append('}')
        elif x == '[':
            stack.append(']')
        elif x == '(':
            stack.append(')')
        else:
            if stack != []: 
                if stack[-1] == x:
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack == []:
        return True
    else:
        return False
            
            

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
