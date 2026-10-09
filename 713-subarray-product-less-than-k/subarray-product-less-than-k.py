class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0 
        pro = 1
        cout = 0
        if k <= 1:
            return 0
        for r in range (len(nums)):
            pro *= nums[r]
            while l<=r and pro >=k:
                pro = pro // nums[l]
                l += 1
            cout += r-l+1
        return cout
        