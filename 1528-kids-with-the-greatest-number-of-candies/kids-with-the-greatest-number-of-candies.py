class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_kid = max(candies)
        arr = []
        for i in range(len(candies)):
            if(candies[i]+extraCandies >= max_kid):
                arr.append(2>1)
            else:
                arr.append(1>2)
        return arr