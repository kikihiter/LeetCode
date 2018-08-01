class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            lIndex = nums.index(target)
        except:
            lIndex = -1
        
        try:
            rIndex = len(nums) - nums[::-1].index(target) -1
        except:
            rIndex = -1
            
        return [lIndex,rIndex]
