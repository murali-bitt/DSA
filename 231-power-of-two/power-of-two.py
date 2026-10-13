class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n > 0 and n & (n - 1) == 0
        return a
        