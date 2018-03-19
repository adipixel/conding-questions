# Complete the function below.

def getMinimumDifference(a, b):
    result = []
    for i in range(len(a)):
        p = a[i]
        q = b[i]
        
        if len(p) != len(q):
            result.append(-1)
        else:
            amap = dict()
            for x in p:
                if x in amap:
                    amap[x] += 1
                else:
                    amap[x] = 1

            count = 0 
            for x in q:
                if x in amap and amap[x] > 0:
                    amap[x] -= 1
                else:
                    count += 1

            result.append(count)
    return result


