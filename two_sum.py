class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # 1. iterate
        # 2. look in the dictionary weather the num exists
            # 2.1 if exists return current index and strored index
        # 2. store the complement in a array with the index 
        
        compNums = {}
        for x in range(0, len(nums)):
            if nums[x] in compNums:
                return [compNums[nums[x]], x]
            
            
            # storing complement
            compNums[target - nums[x]] = x
