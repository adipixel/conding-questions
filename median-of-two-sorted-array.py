class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        
        # 1. Check boundary conditions
        # 2. init start pointers
        # 3. Compare and shift
        # 4. if empty, paste remaining of other array
        # 5. find median
        
        res = []
        #resPointer = 0
        s1 = 0
        s2 = 0
        
        for x in range(0, len(nums1)+len(nums2)):
            if not nums1 or len(nums1)<=s1: #nums1 is empty
                res = res + nums2[s2:]
                break
            elif not nums2 or len(nums2)<=s2: #nums2 is empty
                res = res + nums1[s1:]
                break
            elif nums1[s1] <= nums2[s2]:
                res.append(nums1[s1])
                s1 = s1 + 1
            else:
                res.append(nums2[s2])
                s2 = s2 + 1
        
        resLen = len(res)
        if resLen % 2 == 0:
            return (float(res[resLen/2]+ res[resLen/2-1])/2)
        else:
            return res[resLen//2] # adjust to the left of the number line
