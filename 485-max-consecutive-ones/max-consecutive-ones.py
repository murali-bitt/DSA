class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        max_a = 0
        i = 0
        n = len(nums)
        while i < n:
            if(nums[i]==1):
                a += 1
            else:
                max_a = max(max_a,a)
                a = 0
            i += 1
        return max(max_a,a)