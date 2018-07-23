class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxStr = []
        maxNum = 0
        for i in s:
            if i in maxStr:
                maxStr=maxStr[maxStr.index(i):]
                del maxStr[0]
            maxStr.append(i)
            maxNum = max(maxNum,len(maxStr))
        return maxNum
