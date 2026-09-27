class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        water,lmax,rmax=0,0,0

        while left < right:
            if(height[left]<height[right]):
                lmax = max(lmax,height[left])
                water += lmax - height[left]
                left +=1
            else:
                rmax = max(rmax,height[right])
                water += rmax-height[right]
                right -= 1
        return water
        