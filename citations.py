class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        citations.sort()
        ciLen = len(citations)
        
        for i in range(ciLen):
            if citations[i] >= ciLen-i :
                return ciLen-i
            
        return 0
        
        
    
