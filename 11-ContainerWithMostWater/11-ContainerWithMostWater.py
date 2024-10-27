class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Optimized approach
        res = 0
        n = len(height)
        l,r = 0, n-1
        while l<r:
            area = (r-l) * min(height[r],height[l])
            res = max(area,res)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res


        # brute force approach
        # res=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area = (j-i) * min(height[i],height[j])
        #         res = max(area,res)
        # return res
        # TC: O(n**2)