class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        比上一题简单，多一个去重
        """
        def tempSum2(candidates, target):
            answer = []
            for i,temp in enumerate(candidates):
                if temp > target:
                    break
                elif temp == target:
                    answer.append([target])
                    break
                else:
                    for tempAnswer in tempSum2(candidates[i+1:], target-temp):
                        answer.append([temp] + tempAnswer)
            return answer
        answerList  = tempSum2(sorted(candidates), target)
        answerList[:] = sorted(answerList[:])
        for i in range(len(answerList)-1,0,-1):
            if answerList[i] == answerList[i-1]:
                del answerList[i]
        return answerList
