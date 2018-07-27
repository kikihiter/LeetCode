from itertools import combinations
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #把这个问题转化成排列组合的问题，例如当n=3时，就是（ _ _ _ _ ）中4选2的问题，选中的地方为‘（’，未选择的为‘）’。这样子得出来的结果可能不符合括号规范，最后加一个检测机制，删除不符的即可。
        if n==1:
            return ["()"]
        combins = [c for c in  combinations(range(n*2-2), n-1)]
        #[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        #print combins
        answerList = []
        answerStr = []
        for lift in combins:
            tempList = ['('] + [')'] * (n-1) * 2 + [')']
            for leftIndex in lift:
                tempList[leftIndex+1] = '('
            answerList.append(tempList)
        #print answerList
       
        #之前做过一道类似的题，判断是否符合规范，可以看从左到右的第一个‘）’，它的左边必须是‘（’，找到这样一对括号，进行不断的删除操作即可判定
        for i in range(len(answerList))[::-1]:
            testList = []
            astr = ""
            for istr in answerList[i]:
                testList.append(istr)
                astr = astr + istr
                
            j = 0
            while testList != None and j<len(testList):
                if testList[j] == ')':
                    if j>0 and testList[j-1] == '(':
                        del testList[j],testList[j-1]
                        j -= 2
                    else:
                        del answerList[i]
                        break
                j += 1
            else:
                answerStr.append(astr)
        return answerStr
