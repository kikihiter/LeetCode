class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        由于不是很明白字典序是什么，所以简单了解了一下，看到了一片讲解的，参考了他的策略，但是具体算法是自己写的
        https://blog.csdn.net/chaoweilanmaohhh/article/details/79690453
        假设此时给出的状态时5 2 4 3 1，那么下一个状态要如何确定呢？首先从人的视角来看，绝对会从序列末尾向前开始查找，例如如果给的状态时1 2 3 4 5，则很容易发现下一个状态应该是1 2 3 5 4，这样就给出了一个策略，第一步应该先找从末尾开始向前第一对非逆序数对，这当然有理由，因为如果是逆序的，说明该种情况一定是已经进行过交换了，则绝对不会是下一种情况交换的候选位置，因此会发现5 2 4 3 1中第一个非逆序数对是2 4，所以交换的候选对象应该是2（2是较小的那一个）；紧接着继续思考，应该和后面的哪一个进行交换。首先显而易见的是，2后面的子序列一定是逆序的。那么如果要和2交换并且使结果是字典序的下一个的话，那么与2交换的一定是2后面的比2大的最小的哪一个数，因此第二步就是从序列末尾开始向前查找第一个比2大的数，与2进行交换（此时为 5 3 4 2 1），那么下一步也是显而易见的，3后面的序列应该是由5 3开始的字典序最小的一个序列，因此要将3后面的序列逆置。最后得到答案5 3 1 2 4。
        
        我写得比他简介多了，不知道他的运行效率怎样
        """
        
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
