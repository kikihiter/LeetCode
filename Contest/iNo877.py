class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        m,n,imark,memo = 0,len(piles)-1,True,{}
        #i,j为下标，mark用来判断是否先行，True代表轮到己方行动，False表示后手，memo为动态规划记忆模块
        def maxSum(i,j,mark):
            try:
                return memo[i,j,mark]
            except:
                #先手
                if mark == True:
                    #只剩一堆的时候，直接拿走
                    if i == j:
                        return piles[j]
                    memo[i,j,mark] = max( piles[i]+maxSum(i+1,j,False) , piles[j]+maxSum(i,j-1,False) )
                    return memo[i,j,mark]
                #后手
                elif mark == False:
                    #只剩一堆的时候，无法获取，返回0
                    if i == j:
                        return 0
                    #这一步判断敌方行动方式，敌方会选择最大的策略，己方能获得的是，敌方拿走一堆之后的情况
                    if piles[i]+maxSum(i+1,j,True) >= piles[j]+maxSum(i,j-1,True):
                        memo[i,j,mark] = max( piles[i+1]+maxSum(i+2,j,False) , piles[j]+maxSum(i+1,j-1,False) )
                        return memo[i,j,mark]
                    if piles[i]+maxSum(i+1,j,True) < piles[j]+maxSum(i,j-1,True):
                        memo[i,j,mark] = max( piles[i]+maxSum(i+1,j-1,False) , piles[j-1]+maxSum(i,j-2,False) )
                        return memo[i,j,mark]
        
        pilesSum = 0
        for num in piles:
            pilesSum += num
        Alex = maxSum(m,n,imark)
        return Alex > pilesSum -Alex
