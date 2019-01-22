class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mark = [i for i in range(1,len(nums)+1)]
        nums = set(nums)
        # i don't know list to set cost how many time
        for num in mark:
            if num not in nums:
            # O(1)
                return num
        return len(nums)+1
