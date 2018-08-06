"""
"y959q969u3hb22odq595"
222280369
"""
class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        """reS = ""
        i,l = 0,0
        while l<K and i<len(S):
        
            try:
                num = int(S[i])
                reS *= num
                l *= num 
            except:
                reS += S[i]
                l+=1
            i += 1
        
        return reS[K-1]"""
        
        i,l = 0,0
        while i<len(S):
        
            try:
                num = int(S[i])
                #reS *= num
                l *= num 
            except:
                #reS += S[i]
                l+=1
            i += 1
        print l
        
        for str_t in S[::-1]:
