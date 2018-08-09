#之前写的，查找下一个字典序的算法
def nextPer(num):
    #之前写的算法是直接在原列表上进行修改，并没有使用额外辅助空间，导致最终结果perList中元素全部指向同一位置，在这里进行修改，新生成一个列表并进行返回。
    nums = []
    for yuansu in num:
        nums.append(yuansu)
    
    for i in range(len(nums)-1,0,-1):
        #从后向前寻找第一个非逆序数对
        if nums[i] > nums[i-1]:
            #一个中间变量，为比nums[i-1]大的数
            temp = nums[i]
            #在i后面寻找比nums[i-1]大的数中的最小的数值
            for j in range(len(nums)-1,i,-1):
                if nums[j] > nums[i-1]:
                    temp = min(temp,nums[j])
            #找到这个数的序号，应当注意，应该从后往前找到这个序号，不能直接从前开始找，因为可能前方有相同的值的元素
            iIndex = len(nums) - nums[::-1].index(temp) - 1                        
            nums[i-1],nums[iIndex] = nums[iIndex],nums[i-1]
            nums[i:] = sorted(nums[i:])
            break
    else:
        nums[:] = sorted(nums[:])
    return nums

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perList = []
        nums[:] = sorted(nums[:]) 
        perList.append(nums)
        nums = nextPer(nums)
        while nums != sorted(nums):
            perList.append(nums)
            nums = nextPer(nums)
            #print nums
        return perList
