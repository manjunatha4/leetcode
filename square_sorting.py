class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0
        n=len(nums)
        r=n-1
        res=[0]*n
        pos=n-1
        while l<=r:
            if nums[l]*nums[l]>nums[r]*nums[r]:
                res[pos]=nums[l]*nums[l]
                l+=1
            else:
                res[pos]=nums[r]*nums[r]
                r-=1
            pos-=1
        return res
    
      