#A string S of lowercase letters is given. We want to partition this string into as many parts as possible 
#so that each letter appears in at most one part, 
#and return a list of integers representing the size of these parts.


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        a = dict()
        start = 0
        end = 0
        subStr = []

        for i in range(0,len(S)):
            x = S[i]
            if x not in a:
                a[x] = [i, i]
            else:
                a[x] = [a[x][0], i]

        print a

        for idx, val in enumerate(a):
            if a[val][0] == 0:
                start = 0
                end = a[val][1]
                break


        while True:

            tempList = []
            
            i = 0
            while i < len(a):
                if a.values()[i][0] >= start and a.values()[i][0] <= end:
                    #tempList.append(a.values()[i][1])
                    if a.values()[i][1] > end:
                        end = a.values()[i][1]
                        #print a.keys()[i], a.values()[i]
                        i = 0
                    else:
                        i += 1
                else:
                    i += 1
                
            print start, end
            
            subStr.append(end-start+1)
            start = end + 1
        
            for idx, val in enumerate(a):
                if a[val][0] == start:
                    end = a[val][1]
                    break
                    
            #end = len(S)

            if end > len(S)-1 or start > len(S)-1:
                break


            #print start, end

        return subStr
