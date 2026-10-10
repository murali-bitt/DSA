
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for r in range(len(nums)):

            # 1. Remove indices outside the window
            if dq and dq[0] <= r - k:
                dq.popleft()

            # 2. Remove smaller or equal values
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            # 3. Add current index
            dq.append(r)

            # 4. Record maximum when window is full
            if r >= k - 1:
                result.append(nums[dq[0]])

        return result
