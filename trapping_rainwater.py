class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        left_max=0
        right_max=0
        res=0
        while l<r:
            if height[l]<height[r]:
                if height[l]>=left_max:
                    left_max=height[l]
                else:
                    res+=left_max - height[l]
                l+=1
            else:
                if height[r]>=right_max:
                    right_max=height[r]
                else:
                    res+=right_max - height[r]
                r-=1
        return res
