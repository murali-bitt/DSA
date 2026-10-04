class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
        # a = str(x)
        # left = 0
        # right = len(a)-1
        # while left < right:
        #     if(a[left]==a[right] or x == 0):
        #         left += 1
        #         right -=1
        #         return True

        #     else:
        #         return False

        