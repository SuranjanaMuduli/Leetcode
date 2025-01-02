class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxs = max(candies)
        res = []
        for i in candies:
            new = i + extraCandies
            if new >= maxs:
                res.append(True)
            else:
                res.append(False)
        return res
