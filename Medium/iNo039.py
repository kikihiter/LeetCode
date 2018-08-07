class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        本来想用numpy直接计算多元一次方程组的，但是好像必须是矩阵，作罢。这里借鉴了别人的想法，主要是递归。
        """
        def tempSum(candidates, target):
            answer = []
            for i,temp in enumerate(candidates):
                
                if temp > target:
                    break
                elif temp == target:
                    answer.append([target])
                    break
                else:
                    for tempAnswer in tempSum(candidates[i:], target-temp):
                        answer.append([temp] + tempAnswer)
                        #print tempAnswer
            return answer
        return tempSum(sorted(candidates), target) 
        
