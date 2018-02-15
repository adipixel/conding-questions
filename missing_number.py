# Question: example
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # total = (n*(n+1))/2
        max = 0
        count = 0
        zeroFlag = False
        for x in nums:
            count += x
            if x > max:
                max = x
            if x == 0:
                zeroFlag = True
                
        total = (max*(max+1))/2
        res = total - count
        print total , count
        if res == 0:
            if zeroFlag:
                return max+1
            else:
                return 0
        else:
            return res
