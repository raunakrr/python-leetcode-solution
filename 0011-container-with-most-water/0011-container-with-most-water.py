class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum=0
        l,r=0,len(height)-1
        while l<r:
            area=min(height[l],height[r])*(r-l)
            maximum=max(maximum,area)
            if height[l]<height[r]:
                l+=1
            elif height[l]>=height[r]:
                r-=1
        
        return maximum