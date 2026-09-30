class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mid = int(((len(nums) - 1)/2))
        a = nums[mid]
        b = len(nums) 
        c = 0
        for i in range(0,b):
            if(nums[i] == a):
                c += 1
        return(c == 1)