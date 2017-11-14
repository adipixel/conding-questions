#https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

#solution 1: O(n)
def is_matched(expression):
    openDic = {'{': 1, '(':1, '[':1}
    closeDic = {'}': 1, ')':1, ']':1}
    mainDic = {'{}': 1, '()':1, '[]':1}
    strStack = []
    for x in expression:
        if(x in openDic):
            strStack.append(x)
        else:
            temp = strStack[-1] + x
            if temp in mainDic:
                strStack.remove(strStack[-1])
                pass
            else:
                return False
    if strStack == []:
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
