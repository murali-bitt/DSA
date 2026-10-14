class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()
        for ptr in range(len(nums)-2):
            if ptr > 0 and nums[ptr] == nums[ptr-1]:
                continue
            left = ptr + 1
            right = len(nums) - 1

            while left < right:
                summ = nums[ptr] + nums[left]+ nums[right]
                if (summ == 0):
                    result.append([nums[ptr], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while(left < right and nums[left]==nums[left-1]):
                        left += 1
                    while(left < right and nums[right]==nums[right+1]):
                        right -= 1
                elif(summ<0):
                    left += 1
                else:
                    right -= 1
        return result
                

        