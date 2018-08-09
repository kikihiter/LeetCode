class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        本题有这样一个限制条件：
        You must not use any built-in BigInteger library or convert the inputs to integer directly.
        但是说实话，这个表述很笼统，我不认为有别的什么算法可以直接计算出答案而不将字符串转化为数字来进行处理，说到底是数的运算。
        就我理解来说，设计这样的算法，目的在于解决数字相乘时有可能带来的临界问题。
        我的解法也将按照这样的目的来设计。
        """
        if int(num1) == 0 or int(num2) == 0:
            return "0"
        
        #分别“按位”计算乘法
        answerList = []
        maxLen = 0
        for i in range(len(num2)-1,-1,-1):
            a = int(num2[i])
            jinWei = 0
            tempAns = [0] * (len(num2)-1-i)
            for j in range(len(num1)-1,-1,-1):
                b = int(num1[j])
                t = a * b + jinWei
                tempAns.append( t % 10)
                jinWei = t / 10
                if j == 0 and jinWei != 0:
                    tempAns.append(jinWei)
            maxLen = max(maxLen,len(tempAns))
            answerList.append(tempAns)
        #print max(answerList)
        
        #补全列表，防止超界
        for answer in answerList:
            l = len(answer)
            while l < maxLen:
                answer.append(0)
                l += 1
        #print answerList,maxLen
        
        #“按位”加法
        answerSum = []
        jinWei2 = 0
        for i in range(maxLen):
            n = 0
            for j in range(len(answerList)):
                n += answerList[j][i]
            n += jinWei2
            answerSum.append(n%10)
            jinWei2 = n/10
            if i == maxLen-1 and jinWei2 != 0:
                answerSum.append(jinWei2)
        #print answerSum
        
        num = ""
        for x in answerSum[::-1]:
            num += str(x)
        return num
