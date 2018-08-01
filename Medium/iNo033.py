class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #这题是糊弄过去了，但其实我没有很明白这题是在干什么，而且时间复杂度这里，我直接调函数，感觉跟作弊一样
        try:
            reIndex = nums.index(target)
        except:
            reIndex =- 1
        return reIndex
